# SECTION 42: Mock Exam 1 (Module 10)

> **Format**: 10 High-Quality Questions replicating the ACE difficulty.

## Instructions
*   Don't cheat.
*   Cover the answer key.
*   Time limit: 15 minutes.

---

### Question 1: IAM & Groups
**Scenario**: You have 50 developers in the "frontend-team". You need to give them all access to view logs in Project A. A week later, 5 new devs join.
**Q**: What is the Google Best Practice?
*   A. Create a Service Account for each dev.
*   B. Assign `roles/logging.viewer` to each user individually.
*   C. **Create a Google Group**, add all devs to the group, and assign `roles/logging.viewer` to the Group.
*   D. Give them `roles/owner` so they stop complaining.

> **Answer: C.** Always manage permissions via Groups. When new devs join, you just add them to the Group. No IAM policy change needed.

---

### Question 2: Storage Classes
**Scenario**: You have 1TB of compliance data. You need to access it once a year for an audit. If you access it, speed doesn't matter much.
**Q**: Which class is cheapest?
*   A. Standard.
*   B. Nearline.
*   C. Coldline.
*   D. **Archive**.

> **Answer: D.** Archive is for data accessed < once/year. Note: Data retrieval fees apply!

---

### Question 3: Compute Engine
**Scenario**: You need to ensure your web application can survive a generic zonal failure.
**Q**: What configuration do you need?
*   A. A single VM with a backup.
*   B. **Managed Instance Group (MIG)** distributed across multiple zones.
*   C. A larger machine type.
*   D. Preemptible VMs.

> **Answer: B.** Regional MIGs distribute VMs across zones (us-central1-a, b, c). If `a` goes down, `b` and `c` keep running.

---

*(More questions simulating the 50-question exam would go here in a real app)*

## Score
*   < 2/3? Review IAM and Storage.
*   3/3? Ready for Mock Exam 2.
