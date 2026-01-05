document.addEventListener('DOMContentLoaded', () => {
    console.log("Course Player v4 Loaded");
    initQuizzes();
    initFlashcards();
});

function initQuizzes() {
    const quizCards = document.querySelectorAll('.quiz-card');
    if (!quizCards.length) return;

    const totalQuestions = quizCards.length;
    let correctAnswersCount = 0;

    quizCards.forEach(card => {
        const correctOptionIndex = parseInt(card.dataset.correct);
        const feedbackDiv = card.querySelector('.quiz-feedback');
        const options = card.querySelectorAll('.quiz-option');
        let answeredCorrectly = false;

        options.forEach(optionBtn => {
            optionBtn.addEventListener('click', () => {
                const selectedOptionIndex = parseInt(optionBtn.dataset.option);
                const isCorrect = selectedOptionIndex === correctOptionIndex;

                options.forEach(btn => {
                    btn.disabled = true;
                    btn.classList.remove('hover:bg-slate-50', 'hover:border-slate-300');
                    btn.classList.add('cursor-default');
                });

                if (isCorrect) {
                    optionBtn.classList.remove('border-slate-200');
                    optionBtn.classList.add('bg-green-50', 'border-green-500', 'text-green-900');

                    // Fix nested elements: circle and inside dot
                    const outerCircle = optionBtn.querySelector('div.w-5'); // The circle border
                    const innerDot = optionBtn.querySelector('div.w-2\\.5'); // The dot

                    if (outerCircle) {
                        outerCircle.classList.remove('border-slate-300');
                        outerCircle.classList.add('border-green-600');
                    }
                    if (innerDot) {
                        innerDot.classList.remove('bg-brand-600', 'opacity-0');
                        innerDot.classList.add('bg-green-500', 'opacity-100');
                    }

                    showFeedback(feedbackDiv, true, "Correct! Great job.");
                    if (!answeredCorrectly) {
                        answeredCorrectly = true;
                        correctAnswersCount++;
                        if (correctAnswersCount === totalQuestions) triggerConfetti();
                    }
                } else {
                    optionBtn.classList.remove('border-slate-200');
                    optionBtn.classList.add('bg-red-50', 'border-red-500', 'text-red-900');

                    // Highlight correct answer
                    const correctBtn = card.querySelector(`button[data-option="${correctOptionIndex}"]`);
                    if (correctBtn) {
                        correctBtn.classList.add('bg-green-50', 'border-green-500', 'text-green-900');
                    }
                    showFeedback(feedbackDiv, false, "Incorrect. The correct answer is highlighted green.");
                }
            });
        });
    });
}

function triggerConfetti() {
    const end = Date.now() + 3 * 1000;
    const colors = ['#0284c7', '#ffffff'];
    (function frame() {
        confetti({ particleCount: 2, angle: 60, spread: 55, origin: { x: 0 }, colors: colors });
        confetti({ particleCount: 2, angle: 120, spread: 55, origin: { x: 1 }, colors: colors });
        if (Date.now() < end) requestAnimationFrame(frame);
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
//  FLASHCARD MANAGER V4
// ---------------------------------------------------------
function initFlashcards() {
    console.log("Starting Flashcard Initialization v4...");
    const flashcardSection = document.getElementById('flashcards');
    const grid = document.getElementById('flashcard-grid');

    if (!flashcardSection || !grid) {
        console.error("Flashcard DOM elements not found. Stopping.");
        return;
    }

    let allCards = [];

    // Attempt 1: Tree Walker
    // Walks through every comment node in the body to find the JSON
    try {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_COMMENT, null, false);
        let node;
        while (node = walker.nextNode()) {
            const val = node.nodeValue.trim();
            if (val.includes('FLASHCARDS') && val.includes('[')) {
                console.log("Flashcards found in comment (TreeWalker)");
                const parsed = parseFlashcardJSON(val);
                if (parsed) allCards = allCards.concat(parsed);
            }
        }
    } catch (e) {
        console.error("TreeWalker Error:", e);
    }

    // Attempt 2: Fallback Regex on InnerHTML
    if (allCards.length === 0) {
        console.log("TreeWalker found zero cards. Trying Regex...");
        const regex = /<!--\s*FLASHCARDS\s*(\[\s*\{[\s\S]*?\}\s*\])\s*-->/g;
        let match;
        // Search in main tags to avoid huge body search if possible
        const searchArea = document.querySelector('main')?.innerHTML || document.body.innerHTML;

        while ((match = regex.exec(searchArea)) !== null) {
            if (match[1]) {
                console.log("Flashcards found via Regex");
                const parsed = parseFlashcardJSON(match[0]); // match 0 is full tag, wait we need group 1
                // Actually my helper parses flexible strings containing []
                // match[1] is the array string
                try {
                    const cardsData = JSON.parse(match[1]);
                    if (Array.isArray(cardsData)) allCards = allCards.concat(cardsData);
                } catch (e) { console.error("Regex JSON Parse Error", e); }
            }
        }
    }

    if (allCards.length > 0) {
        console.log(`Rendered ${allCards.length} flashcards.`);
        renderFlashcards(grid, allCards);
        flashcardSection.classList.remove('hidden');
    } else {
        console.warn("No flashcards found. Hiding section.");
        // If we found nothing, we HIDE the section so the user doesn't see the fallback text
        flashcardSection.classList.add('hidden');
    }
}

function parseFlashcardJSON(str) {
    try {
        const start = str.indexOf('[');
        const end = str.lastIndexOf(']') + 1;
        if (start !== -1 && end !== 0) {
            const json = str.substring(start, end);
            return JSON.parse(json);
        }
    } catch (e) {
        console.error("JSON Parsing failed", e);
    }
    return null;
}

function renderFlashcards(container, cards) {
    container.innerHTML = ''; // Wipe fallback content
    cards.forEach(card => {
        const html = `
            <div class="flashcard group perspective-1000 h-48 cursor-pointer" onclick="this.classList.toggle('flipped')">
                <div class="relative w-full h-full text-center transition-transform duration-500 transform-style-3d group-[.flipped]:rotate-y-180">
                    <div class="absolute w-full h-full backface-hidden bg-white border-2 border-slate-200 rounded-xl shadow-sm flex flex-col items-center justify-center p-6 hover:border-brand-300">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-2">Term</span>
                        <h3 class="text-xl font-bold text-slate-800">${card.term}</h3>
                        <p class="text-xs text-slate-400 mt-4 font-medium uppercase tracking-wider text-brand-600">Click to Flip <i class="fa-solid fa-rotate ml-1"></i></p>
                    </div>
                    <div class="absolute w-full h-full backface-hidden bg-slate-900 rounded-xl shadow-lg rotate-y-180 flex flex-col items-center justify-center p-6 text-white transform rotate-y-180">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-2">Definition</span>
                        <p class="font-medium text-slate-200 leading-relaxed">${card.def}</p>
                    </div>
                </div>
            </div>
        `;
        container.insertAdjacentHTML('beforeend', html);
    });
}
