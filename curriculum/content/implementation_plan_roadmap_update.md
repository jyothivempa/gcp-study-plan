# Implementation Plan: Roadmap Update

## Goal
Add "Week 5: Bonus Quizzes" to the Roadmap timeline UI to reflect the newly created 7-Day Advanced Exam content.

## Proposed Changes

### UI Update
#### [MODIFY] `templates/roadmap.html`
*   Add a new `<li>` element after Phase 4.
*   Style it as **Phase 5** (or "Bonus") using a distinct color (Rose/Red).
*   Title: "Bonus: Advanced Scenarios (Days 31-37)".
*   Description: "The ultimate challenge. 7 days of intense scenario-based exams to test your architectural limits."

## Verification
*   Open `/roadmap/` in the browser.
*   Verify the vertical line connects correctly.
*   Verify the new "Phase 5" card appears at the bottom.
