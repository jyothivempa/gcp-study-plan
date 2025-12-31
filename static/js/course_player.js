document.addEventListener('DOMContentLoaded', () => {
    initQuizzes();
    initFlashcards();
});

function initQuizzes() {
    const totalQuestions = quizCards.length;
    let correctAnswersCount = 0;

    quizCards.forEach(card => {
        const correctOptionIndex = parseInt(card.dataset.correct);
        const feedbackDiv = card.querySelector('.quiz-feedback');
        const options = card.querySelectorAll('.quiz-option');

        // State to prevent double counting
        let answeredCorrectly = false;

        options.forEach(optionBtn => {
            optionBtn.addEventListener('click', () => {
                // Determine if this is the correct option
                const selectedOptionIndex = parseInt(optionBtn.dataset.option);
                const isCorrect = selectedOptionIndex === correctOptionIndex;

                // Reset all options in this card
                options.forEach(btn => {
                    btn.disabled = true; // Disable after selection
                    btn.classList.remove('hover:bg-slate-50', 'hover:border-slate-300');
                    btn.classList.add('cursor-default');
                });

                // Style the selected option
                if (isCorrect) {
                    optionBtn.classList.remove('border-slate-200');
                    optionBtn.classList.add('bg-green-50', 'border-green-500', 'text-green-900');
                    optionBtn.querySelector('.w-2.5').classList.remove('bg-brand-600', 'opacity-0');
                    optionBtn.querySelector('.w-2.5').classList.add('bg-green-500', 'opacity-100');
                    optionBtn.querySelector('.w-5').classList.remove('border-slate-300');
                    optionBtn.querySelector('.w-5').classList.add('border-green-600');

                    showFeedback(feedbackDiv, true, "Correct! Great job.");

                    if (!answeredCorrectly) {
                        answeredCorrectly = true;
                        correctAnswersCount++;

                        // Check for 100% Completion
                        if (correctAnswersCount === totalQuestions) {
                            triggerConfetti();
                        }
                    }

                } else {
                    optionBtn.classList.remove('border-slate-200');
                    optionBtn.classList.add('bg-red-50', 'border-red-500', 'text-red-900');

                    // Also highlight the correct one so they learn
                    const correctBtn = card.querySelector(`button[data-option="${correctOptionIndex}"]`);
                    if (correctBtn) {
                        correctBtn.classList.add('bg-green-50', 'border-green-500', 'text-green-900');
                        correctBtn.querySelector('.w-5').classList.add('border-green-500');
                    }

                    showFeedback(feedbackDiv, false, "Incorrect. The correct answer is highlighted green.");
                }
            });
        });
    });
}

function triggerConfetti() {
    // School Pride Effect
    const end = Date.now() + 3 * 1000;
    const colors = ['#0284c7', '#ffffff'];

    (function frame() {
        confetti({
            particleCount: 2,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: colors
        });
        confetti({
            particleCount: 2,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: colors
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());
}

function showFeedback(element, isSuccess, message) {
    element.classList.remove('hidden', 'bg-green-100', 'text-green-800', 'bg-red-100', 'text-red-800');

    if (isSuccess) {
        element.classList.add('bg-green-100', 'text-green-800');
        element.innerHTML = `<i class="fa-solid fa-check-circle mr-2"></i> ${message}`;
    } else {
        element.classList.add('bg-red-100', 'text-red-800');
        element.innerHTML = `<i class="fa-solid fa-circle-xmark mr-2"></i> ${message}`;
    }

    element.classList.remove('hidden');
}

// ---------------------------------------------------------
//  FLASHCARD MANAGER
// ---------------------------------------------------------
function initFlashcards() {
    console.log("Starting Flashcard Initialization v3...");
    const flashcardSection = document.getElementById('flashcards');
    const grid = document.getElementById('flashcard-grid');
    if (!flashcardSection || !grid) {
        console.error("Flashcard DOM elements not found");
        return;
    }

    let allCards = [];

    // Strategy 1: TreeWalker (Best for traversing DOM nodes including comments)
    try {
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_COMMENT,
            null,
            false
        );

        let node;
        while (node = walker.nextNode()) {
            const value = node.nodeValue.trim();
            if (value.includes('FLASHCARDS') && value.includes('[')) {
                console.log("Found Flashcard Comment via TreeWalker");
                const parsed = parseFlashcardJSON(value);
                if (parsed) allCards = allCards.concat(parsed);
            }
        }
    } catch (e) {
        console.error("TreeWalker failed:", e);
    }

    // Strategy 2: Fallback Regex on Body HTML (If TreeWalker misses weirdly placed comments)
    if (allCards.length === 0) {
        console.log("TreeWalker found nothing. Trying Regex fallback...");
        const regex = /<!--\s*FLASHCARDS\s*(\[\s*\{[\s\S]*?\}\s*\])\s*-->/g;
        let match;
        // Search entire body just in case
        while ((match = regex.exec(document.body.innerHTML)) !== null) {
            if (match[1]) {
                console.log("Found Flashcard Comment via Regex");
                try {
                    const cardsData = JSON.parse(match[1]);
                    if (Array.isArray(cardsData)) allCards = allCards.concat(cardsData);
                } catch (e) { console.error("Regex JSON parse error", e); }
            }
        }
    }

    if (allCards.length > 0) {
        console.log(`Rendered ${allCards.length} flashcards.`);
        renderFlashcards(grid, allCards);
        flashcardSection.classList.remove('hidden');
    } else {
        console.warn("No flashcards found in the page source.");
        flashcardSection.classList.add('hidden');
    }
}

function parseFlashcardJSON(str) {
    try {
        const jsonStart = str.indexOf('[');
        const jsonEnd = str.lastIndexOf(']') + 1;
        if (jsonStart !== -1 && jsonEnd !== -1) {
            return JSON.parse(str.substring(jsonStart, jsonEnd));
        }
    } catch (e) {
        console.error("JSON parsing helper failed:", e);
    }
    return null;
}

function renderFlashcards(container, cards) {
    container.innerHTML = ''; // Clear fallback content

    cards.forEach((card, index) => {
        const cardHtml = `
            <div class="flashcard group perspective-1000 h-48 cursor-pointer" onclick="this.classList.toggle('flipped')">
                <div class="relative w-full h-full text-center transition-transform duration-500 transform-style-3d group-[.flipped]:rotate-y-180">
                    <!-- Front -->
                    <div class="absolute w-full h-full backface-hidden bg-white border-2 border-slate-200 rounded-xl shadow-sm flex flex-col items-center justify-center p-6 hover:border-brand-300">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-2">Term</span>
                        <h3 class="text-xl font-bold text-slate-800">${card.term}</h3>
                        <p class="text-xs text-slate-400 mt-4 font-medium uppercase tracking-wider text-brand-600">Click to Flip <i class="fa-solid fa-rotate ml-1"></i></p>
                    </div>
                    <!-- Back -->
                    <div class="absolute w-full h-full backface-hidden bg-slate-900 rounded-xl shadow-lg rotate-y-180 flex flex-col items-center justify-center p-6 text-white transform rotate-y-180">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-2">Definition</span>
                        <p class="font-medium text-slate-200 leading-relaxed">${card.def}</p>
                    </div>
                </div>
            </div>
        `;
        container.insertAdjacentHTML('beforeend', cardHtml);
    });
}
