function studySession(config) {
    return {
        cards: config.cards,
        urls: config.urls,
        csrfToken: config.csrfToken,
        currentIndex: 0,
        isFlipped: false,
        finished: false,
        explaining: false,
        explanation: null,

        get currentCard() {
            return this.cards[this.currentIndex] || { front: '', back: '' };
        },

        async explain() {
            if (this.explanation) return;
            this.explaining = true;

            try {
                const response = await fetch(this.urls.explain, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': this.csrfToken
                    },
                    body: JSON.stringify({
                        question: this.currentCard.front,
                        answer: this.currentCard.back,
                        context: 'GCP Exam Study'
                    })
                });

                const data = await response.json();
                this.explanation = data.explanation || "Sorry, I couldn't explain this right now.";
            } catch (e) {
                this.explanation = "Error connecting to AI brain.";
                console.error(e);
            } finally {
                this.explaining = false;
            }
        },

        async submitResult(difficulty) {
            const cardIndex = this.currentIndex;
            this.isFlipped = false;

            // Optimistic UI
            setTimeout(() => {
                this.explanation = null;
                if (this.currentIndex < this.cards.length - 1) {
                    this.currentIndex++;
                } else {
                    this.finished = true;
                    if (typeof confetti !== 'undefined') {
                        confetti({ particleCount: 200, spread: 100, origin: { y: 0.6 } });
                    }
                }
            }, 300);

            // Send to Backend
            try {
                await fetch(this.urls.submit, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': this.csrfToken
                    },
                    body: JSON.stringify({
                        day_number: config.dayNumber,
                        card_index: cardIndex,
                        result: difficulty
                    })
                });
            } catch (e) {
                console.error("Failed to save progress", e);
            }
        }
    }
}
