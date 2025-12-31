# Implementation Plan - Split Day 31 into 7 Bonus Days

## Goal
Redistribute the 179 advanced questions from a single "Day 31" into 7 separate days (Day 31 to Day 37) to create a "Bonus Exam Week".

## Proposed Changes

### Database Setup
#### [NEW] `create_bonus_days.py`
*   Define a helper function.
*   Update `Day 31` title to "Bonus Exam 1".
*   Create `Day 32` through `Day 37` with titles "Bonus Exam 2" to "Bonus Exam 7".
*   Clear ALL existing `QuizQuestions` for these days (clean slate).

### Content Population
#### [MODIFY] `populate_day_31_part*.py`
*   Update each script to target a unique Day number:
    *   Part 1 -> Day 31 (25 Qs)
    *   Part 2 -> Day 32 (30 Qs)
    *   Part 3 -> Day 33 (30 Qs)
    *   Part 4 -> Day 34 (30 Qs)
    *   Part 5 -> Day 35 (30 Qs)
    *   Part 6 -> Day 36 (30 Qs)
    *   Part 7 -> Day 37 (4 Qs)
*   Remove the `day.quiz_questions.all().delete()` from Part 1 (since the setup script handles it globally).

## Verification Plan
*   Run the setup script.
*   Run all 7 population scripts.
*   Verify in browser that Days 31-37 exist and contain the correct number of questions.
