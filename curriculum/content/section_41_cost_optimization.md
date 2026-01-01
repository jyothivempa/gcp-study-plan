# SECTION 41: Cost Optimization & Best Practices (Module 9)

> **Goal**: Save money. Don't get fired for a $10,000 surprise bill.

## 1️⃣ The 4 Pillars of Cost Optimization
1.  **Visibility:** You can't fix what you can't see. (Billing Reports, Labels).
2.  **Accountability:** Who spent this? (Budgets, Alerts).
3.  **Control:** Stop the bleeding. (Quotas, Capping).
4.  **Recommendations:** Active advice. (Recommender API).

## 2️⃣ Exam Critical: Pricing Calculators
*   **Google Cloud Pricing Calculator:** Web-based tool. Use for **planning** (Estimating future costs).
*   **Cost Table Report:** In-console tool. Use for **analyzing** (Breakdown of invoice).

## 3️⃣ Resource Cleanup Strategies
*   **Orphaned Disks:** You deleted the VM, but forgot the Disk. You are still paying for 500GB.
    *   *Fix:* Check "Disks" tab filtered by "In Use by: None".
*   **Static IPs:** Unattached Static IPs cost money. Attached ones are free.
    *   *Fix:* Release unused IPs.
*   **Snapshots:** Old snapshots accumulate. Use **Snapshot Schedules** with Retention Policies (e.g., "Keep for 14 days").

## 4️⃣ Hands-On Lab: Cost Analysis 🛠️
1.  Go to **Billing** > **Reports**.
2.  Group by **Service**.
3.  See which service is costing $0.01 (likely Storage or Compute).
4.  Go to **Budgets & Alerts**.
5.  Create a "Panic Button" budget: Alert me at $10.00 spend.

## 5️⃣ Checkpoint Quiz
<form>
  <div class="quiz-question" id="q1">
    <p class="font-bold">1. You deleted a VM, but your bill is still increasing. What is the most likely cause?</p>
    <div class="space-y-2">
      <label class="block"><input type="radio" name="q1" value="correct"> You forgot to delete the attached Persisted Disk.</label>
      <label class="block"><input type="radio" name="q1" value="wrong"> The VM is in a zombie state.</label>
      <label class="block"><input type="radio" name="q1" value="wrong"> Google charges a deletion fee.</label>
    </div>
  </div>
</form>
