# Implementation Plan: ACE Exam Focus

## Goal
Explicitly demonstrate how the curriculum aligns with the **Google Cloud Associate Cloud Engineer (ACE)** exam guide to reassure the user that the content is targeted for certification success.

## Proposed Changes

### New "ACE Exam Guide" Page
#### [NEW] `templates/ace_guide.html`
*   Create a dedicated page that lists the official 4 Exam Domains.
*   Map each domain to specific Days in the curriculum.
    *   *Domain 1: Set up a cloud solution environment* -> Days 1-7
    *   *Domain 2: Plan and configure solutions* -> Days 8-14
    *   *Domain 3: Deploy and implement operations* -> Days 15-21, 35
    *   *Domain 4: Configure access and security* -> Days 22-28, 34
*   Include "Top 10 Exam Tips" section.

### Navigation Updates
#### [MODIFY] `templates/base.html`
*   Add a "Exam Guide" item to the main navigation bar, highlighted with a distinct icon (e.g., `fa-clipboard-check`).

#### [MODIFY] `gcp_study_plan/urls.py` & `curriculum/views.py`
*   Add `path('ace-guide/', views.ace_guide, name='ace_guide')`.
*   Create `ace_guide` view to render the template.

### Home Page Enhancement
#### [MODIFY] `templates/home.html`
*   Add a "Certification Guarantee" or "Exam Focused" banner/section linking to the new guide.

## Verification Plan
*   Open the new `/ace-guide/` page.
*   Verify the domain mapping is accurate.
*   Verify the link works from the navbar.
