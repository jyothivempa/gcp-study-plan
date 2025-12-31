# Implementation Plan: Technical Polish & ACE Enhancements

## Goal
Address critical technical debt (broken images, flashcard parsing) and add a high-value "ACE Cheat Sheet" resource requested by the user's focus on exam prep.

## Technical Debt Fixes

### 1. Fix Markdown Image Paths
Currently, course content images are referenced via local `file:///` paths, which browsers block.
*   **Action:** Create `d:\ultimateCode\gcp_study_plan\static\img\course_content`.
*   **Action:** Copy the following images from the Artifacts directory to the new static folder:
    *   `gcp_create_bucket_mockup_*.png`
    *   `gcp_create_vm_mockup_*.png`
    *   `gcp_budget_alert_mockup_*.png`
*   **Action:** Bulk update `section_*.md` files to point to `/static/img/course_content/<filename>`.

### 2. Fix Flashcard Parsing
The current regex in `course_player.js` is greedy and only finds the first block.
*   **Action:** Update `initFlashcards` in `static/js/course_player.js`.
*   **Change:** Use a loop with non-greedy regex `args` or `matchAll` to find *all* `<!-- FLASHCARDS ... -->` blocks in the content.
*   **Change:** Merge multiple JSON arrays into a single deck.

## Enhancements

### 3. ACE Cheat Sheet
Add a "Rapid Review" page for common `gcloud` commands and limits.
*   **New Page:** `templates/resources/ace_cheat_sheet.html`.
*   **URL:** `/resources/ace-cheat-sheet/`.
*   **Content:**
    *   Key `gcloud compute` commands.
    *   Key `gcloud storage` commands.
    *   IAM Roles reference.
*   **Navigation:** Link from the sidebar of the **ACE Guide**.

## Verification Plan
1.  **Images:** Open Day 6 (Cloud Storage) in browser. Verify the "Console Walkthrough" images load (no broken icon).
2.  **Flashcards:** Open Day 1 (which has flashcards). Verify they still load. Open a day with *multiple* blocks (if any created) to test merging.
3.  **Cheat Sheet:** Navigate to `/curriculum/ace-guide/` -> Click "Cheat Sheet" -> Verify content.
