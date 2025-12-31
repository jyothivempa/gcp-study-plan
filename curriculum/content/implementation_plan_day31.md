# Implementation Plan - Day 31: Advanced Exam Questions

## Goal
Add a new "Day 31" to the curriculum titled "Bonus: Advanced Exam Scenarios". This day will contain a massive quiz of 179 scenario-based questions provided by the user.

## User Review Required
> [!IMPORTANT]
> The user provided **Questions Only**. I will be **generating** plausible Options (A, B, C, D) and the Correct Answer for all 179 questions based on my knowledge of GCP. This is a best-effort approximation of an actual exam dump.

## Proposed Changes

### Scripting
#### [NEW] `create_day_31.py`
*   Fix the Django setup (setup `DJANGO_SETTINGS_MODULE`).
*   Create `Week 5` ("Beyond the Horizon").
*   Create `Day 31` linked to Week 5.

#### [NEW] `populate_day_31_quiz.py`
*   A Python script containing the dictionary of 179 questions.
*   Each question entry will have:
    *   `q`: The text provided by the user.
    *   `o1`, `o2`, `o3`, `o4`: AI-generated plausible options.
    *   `ans`: The AI-determined correct option (1-4).
*   The script will iterate through this data and create `QuizQuestion` objects for Day 31.

## Verification Plan

### Automated Tests
*   Run the population script and check for "Successfully created 179 questions" output.
*   Check `QuizQuestion.objects.filter(day__number=31).count()` equals 179.

### Manual Verification
*   Open Browser to `http://127.0.0.1:8000/curriculum/day/31/`.
*   Verify the "Interactive Flashcards" (if any) and "Knowledge Check" section.
*   Take the quiz and verify the feedback makes sense.
