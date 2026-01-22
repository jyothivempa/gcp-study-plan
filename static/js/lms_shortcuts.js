/**
 * LMS Keyboard Shortcuts & Interactivity
 * Provides keyboard navigation, focus mode, and mark-complete functionality
 */
(function () {
    'use strict';

    // ================================================
    // 1. KEYBOARD SHORTCUTS
    // ================================================
    const shortcuts = {
        '/': focusSearch,
        'n': goToNextLesson,
        'p': goToPrevLesson,
        'm': toggleFocusMode,
        '?': toggleShortcutsModal,
        'Escape': closeModals
    };

    document.addEventListener('keydown', function (e) {
        // Ignore if typing in input/textarea
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
            if (e.key === 'Escape') {
                e.target.blur();
            }
            return;
        }

        const handler = shortcuts[e.key];
        if (handler) {
            e.preventDefault();
            handler();
        }
    });

    function focusSearch() {
        const searchInput = document.querySelector('#search-input, input[name="q"]');
        if (searchInput) {
            searchInput.focus();
            searchInput.select();
        }
    }

    function goToNextLesson() {
        const nextLink = document.querySelector('a[href*="next"], a:has(.fa-arrow-right)');
        if (nextLink) {
            nextLink.click();
        } else {
            // Fallback: look for "Day X" pattern
            const links = document.querySelectorAll('a[href*="/curriculum/"]');
            // Navigate to next if available
        }
    }

    function goToPrevLesson() {
        const prevLink = document.querySelector('a:has(.fa-arrow-left)');
        if (prevLink) {
            prevLink.click();
        }
    }

    // ================================================
    // 2. FOCUS MODE
    // ================================================
    function toggleFocusMode() {
        document.body.classList.toggle('focus-mode');
        localStorage.setItem('focusMode', document.body.classList.contains('focus-mode'));
    }

    // Restore focus mode on load
    if (localStorage.getItem('focusMode') === 'true') {
        document.body.classList.add('focus-mode');
    }

    // ================================================
    // 3. SHORTCUTS MODAL
    // ================================================
    function toggleShortcutsModal() {
        let modal = document.getElementById('shortcuts-modal');
        if (!modal) {
            modal = createShortcutsModal();
            document.body.appendChild(modal);
        }
        modal.classList.toggle('open');
    }

    function closeModals() {
        const modal = document.getElementById('shortcuts-modal');
        if (modal) modal.classList.remove('open');
    }

    function createShortcutsModal() {
        const modal = document.createElement('div');
        modal.id = 'shortcuts-modal';
        modal.className = 'shortcuts-modal';
        modal.innerHTML = `
            <div class="shortcuts-modal-content">
                <h3 style="margin: 0 0 20px; font-size: 20px; font-weight: 700;">
                    <i class="fa-solid fa-keyboard" style="margin-right: 8px; color: #635bff;"></i>
                    Keyboard Shortcuts
                </h3>
                <div class="shortcut-row">
                    <span>Focus search</span>
                    <span class="shortcut-key">/</span>
                </div>
                <div class="shortcut-row">
                    <span>Next lesson</span>
                    <span class="shortcut-key">N</span>
                </div>
                <div class="shortcut-row">
                    <span>Previous lesson</span>
                    <span class="shortcut-key">P</span>
                </div>
                <div class="shortcut-row">
                    <span>Toggle focus mode</span>
                    <span class="shortcut-key">M</span>
                </div>
                <div class="shortcut-row">
                    <span>Show shortcuts</span>
                    <span class="shortcut-key">?</span>
                </div>
                <div class="shortcut-row">
                    <span>Close modal</span>
                    <span class="shortcut-key">Esc</span>
                </div>
                <button onclick="this.closest('.shortcuts-modal').classList.remove('open')" 
                    style="margin-top: 20px; width: 100%; padding: 12px; background: #f3f4f6; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    Close
                </button>
            </div>
        `;
        modal.addEventListener('click', function (e) {
            if (e.target === modal) closeModals();
        });
        return modal;
    }

    // ================================================
    // 4. MARK AS COMPLETE BUTTON
    // ================================================
    function initMarkCompleteButton() {
        // Only on lesson pages
        if (!document.querySelector('article.reader-container, #content-body')) return;

        const fab = document.createElement('button');
        fab.className = 'mark-complete-fab';
        fab.innerHTML = '<i class="fa-solid fa-check"></i> Mark Complete';

        // Check if already completed (look for data attribute or class)
        const isCompleted = document.body.dataset.lessonCompleted === 'true';
        if (isCompleted) {
            fab.classList.add('completed');
            fab.innerHTML = '<i class="fa-solid fa-check-double"></i> Completed';
        }

        fab.addEventListener('click', function () {
            if (fab.classList.contains('completed')) return;

            // Get lesson/day info from URL or data attribute
            const pathParts = window.location.pathname.split('/');
            const dayNumber = pathParts.find(p => !isNaN(p) && p.length > 0);

            if (!dayNumber) {
                console.warn('Could not determine day number');
                return;
            }

            // AJAX call to mark complete
            fetch(`/curriculum/api/v2/progress/${dayNumber}/complete/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({})
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success || data.status === 'ok') {
                        fab.classList.add('completed');
                        fab.innerHTML = '<i class="fa-solid fa-check-double"></i> Completed';
                        showXPPopup(data.xp_earned || 50);
                    }
                })
                .catch(err => {
                    console.error('Failed to mark complete:', err);
                });
        });

        document.body.appendChild(fab);
    }

    function showXPPopup(xp) {
        const popup = document.createElement('div');
        popup.className = 'xp-popup';
        popup.textContent = `+${xp} XP`;
        document.body.appendChild(popup);
        setTimeout(() => popup.remove(), 1000);
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // ================================================
    // 5. PROGRESS DOTS
    // ================================================
    function initProgressDots() {
        const contentBody = document.getElementById('content-body');
        if (!contentBody) return;

        const hasLabs = document.getElementById('labs') || document.querySelector('section:has(.fa-flask)');
        const hasQuiz = document.getElementById('quiz') || document.querySelector('section:has(.fa-brain)');

        const dotsContainer = document.createElement('div');
        dotsContainer.className = 'progress-dots';
        dotsContainer.innerHTML = `
            <div class="progress-dot-item active" id="dot-concepts">
                <div class="progress-dot"><i class="fa-solid fa-book"></i></div>
                <span>Concepts</span>
            </div>
            <div class="progress-connector" id="conn-1"></div>
            <div class="progress-dot-item ${hasLabs ? '' : 'hidden'}" id="dot-labs">
                <div class="progress-dot"><i class="fa-solid fa-flask"></i></div>
                <span>Labs</span>
            </div>
            ${hasLabs ? '<div class="progress-connector" id="conn-2"></div>' : ''}
            <div class="progress-dot-item ${hasQuiz ? '' : 'hidden'}" id="dot-quiz">
                <div class="progress-dot"><i class="fa-solid fa-brain"></i></div>
                <span>Quiz</span>
            </div>
        `;

        // Insert after breadcrumbs or at top
        const breadcrumbs = document.querySelector('nav.flex');
        if (breadcrumbs && breadcrumbs.nextElementSibling) {
            breadcrumbs.parentNode.insertBefore(dotsContainer, breadcrumbs.nextElementSibling);
        }

        // Update on scroll
        const mainScroll = document.getElementById('main-scroll') || window;
        mainScroll.addEventListener('scroll', updateProgressDots);
    }

    function updateProgressDots() {
        const labsSection = document.getElementById('labs');
        const quizSection = document.getElementById('quiz');
        const scrollTop = (document.getElementById('main-scroll') || document.documentElement).scrollTop;

        const dotConcepts = document.getElementById('dot-concepts');
        const dotLabs = document.getElementById('dot-labs');
        const dotQuiz = document.getElementById('dot-quiz');
        const conn1 = document.getElementById('conn-1');
        const conn2 = document.getElementById('conn-2');

        // Reset
        [dotConcepts, dotLabs, dotQuiz].forEach(d => {
            if (d) d.classList.remove('active', 'completed');
        });
        [conn1, conn2].forEach(c => {
            if (c) c.classList.remove('completed');
        });

        // Determine current section
        if (quizSection && scrollTop >= quizSection.offsetTop - 200) {
            if (dotConcepts) dotConcepts.classList.add('completed');
            if (dotLabs) dotLabs.classList.add('completed');
            if (dotQuiz) dotQuiz.classList.add('active');
            if (conn1) conn1.classList.add('completed');
            if (conn2) conn2.classList.add('completed');
        } else if (labsSection && scrollTop >= labsSection.offsetTop - 200) {
            if (dotConcepts) dotConcepts.classList.add('completed');
            if (dotLabs) dotLabs.classList.add('active');
            if (conn1) conn1.classList.add('completed');
        } else {
            if (dotConcepts) dotConcepts.classList.add('active');
        }
    }

    // ================================================
    // 6. FOCUS MODE TOGGLE BUTTON
    // ================================================
    function initFocusModeButton() {
        if (!document.querySelector('article.reader-container, #content-body')) return;

        const btn = document.createElement('button');
        btn.className = 'focus-mode-btn';
        btn.title = 'Toggle Focus Mode (M)';
        btn.innerHTML = '<i class="fa-solid fa-expand"></i>';
        btn.addEventListener('click', toggleFocusMode);
        document.body.appendChild(btn);
    }

    // ================================================
    // 7. MOBILE SIDEBAR TOGGLE
    // ================================================
    function initMobileSidebar() {
        const sidebar = document.querySelector('#sidebar, aside:first-of-type');
        if (!sidebar || window.innerWidth > 1280) return;

        // Create toggle button
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'mobile-sidebar-toggle';
        toggleBtn.innerHTML = '<i class="fa-solid fa-bars"></i>';
        document.body.appendChild(toggleBtn);

        // Create overlay
        const overlay = document.createElement('div');
        overlay.className = 'mobile-sidebar-overlay';
        document.body.appendChild(overlay);

        toggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
            overlay.classList.toggle('open');
        });

        overlay.addEventListener('click', () => {
            sidebar.classList.remove('open');
            overlay.classList.remove('open');
        });
    }

    // ================================================
    // INIT
    // ================================================
    document.addEventListener('DOMContentLoaded', function () {
        initMarkCompleteButton();
        initProgressDots();
        initFocusModeButton();
        initMobileSidebar();
    });

})();
