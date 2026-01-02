# WEEK 6 REVIEW: The Capstone Experience

## 1️⃣ You Are Now a Builder
This week was different. No theory. Pure building.
*   **Network Capstone:** Debugging connectivity (Firewalls, Routes).
*   **Security Capstone:** Checking permissions (IAM, Buckets).
*   **DevOps Capstone:** Automation (CI/CD).
*   **Data Capstone:** Pipelines (ETL).

## 2️⃣ Mental Shift: The "SRE" Mindset
We touched on **Site Reliability Engineering (SRE)** this week.
*   **SLO (Objective):** "We settle for 99.9%."
*   **SLA (Agreement):** "If we perform below 99.0%, we pay you money."
*   **Error Budget:** The difference. "We can fail for 43 minutes this month. Let's use it to ship features fast."

## 3️⃣ FinOps Recap
*   **CUDs (Committed Use Discounts):** 1 year or 3 year contract. massive savings.
*   **Spot Instances:** 60-91% off, but Google can kill them. Best for Batch jobs (Dataflow/Dataproc).

## 4️⃣ Mock Questions (Week 6)

<!--
**Q1. Your team wants to safely experiment with a new feature, but they are afraid of breaking Production. You have plenty of "Error Budget" left. What does an SRE say?**
*   A. "No."
*   B. **"Go ahead. We have budget to burn."**
*   C. "Ask the CEO."
> **Answer: B.** Error Budgets are meant to be used to increase velocity.

**Q2. You are auditing a project. You see a Service Account Key exported 400 days ago. What is the risk?**
*   A. Key rotation is missing. If an employee left with that key, they still have access.
*   B. The key is expired.
*   C. Google will delete it.
> **Answer: A.** Long-lived keys are the #1 security hole.
-->

## ✅ Week 6 Checklist
<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I completed all 4 Capstone projects.', checked: false },
        { text: 'I know what SLO, SLA, and SLI stand for.', checked: false },
        { text: 'I understand Spot Instances.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Week 6 Confidence Checklist
    </h3>
    <template x-for="(item, index) in items" :key="index">
        <div class="checklist-item" @click="item.checked = !item.checked">
            <div class="checklist-box" :class="{ 'checked': item.checked }">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <span x-text="item.text" :class="{ 'line-through text-slate-400': item.checked }"></span>
        </div>
    </template>
</div>
