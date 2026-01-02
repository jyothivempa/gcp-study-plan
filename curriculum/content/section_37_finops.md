# SECTION 37: Cost Management (FinOps) & Optimization

> **Official Doc Reference**: [Cloud Billing](https://cloud.google.com/billing/docs) | [Cost Management](https://cloud.google.com/cost-management)

## 1️⃣ Overview: The "Runaway Bill" Nightmare 💸
In the cloud, you pay for what you provision, not just what you use (for VMs).
*   **FinOps:** The practice of bringing financial accountability to the variable spend model of cloud.
*   **Golden Rule:** efficient architecture = cost-effective architecture.

## 2️⃣ Discounts: SUDs vs CUDs (Exam Gold 🥇)
Google applies discounts automatically or contractually. Know the difference!

| Feature | **SUD (Sustained Use Discount)** | **CUD (Committed Use Discount)** | **Spot VMs** |
| :--- | :--- | :--- | :--- |
| **How to get it?** | **Automatic**. Just run a VM for >25% of a month. | **Contract**. Commit to 1 or 3 years. | **Flag**. Creating a VM with `--provisioning-model=SPOT`. |
| **Savings** | Up to 30%. | Up to 57% (1yr) or 70% (3yr). | Up to **91%**. |
| **Flexibility** | High. No lock-in. | Low. You pay even if you don't use it. | Zero. Google can kill the VM anytime. |
| **Best For** | Spiky workloads, R&D. | Steady-state production DBs/Web servers. | Batch jobs, Fault-tolerant processing. |

## 3️⃣ Architecture: Billing & Analysis 📊
How do you know *exactly* which team spent $5,000 on BigQuery?

```mermaid
graph TD
    ProjectA[Project A (Dev)] -->|Generates Logs| Billing[Cloud Billing Account]
    ProjectB[Project B (Prod)] -->|Generates Logs| Billing
    
    Billing --"Export Data"--> BQ[(BigQuery Dataset)]
    BQ --"Visualize"--> Looker[Looker Studio Dashboard]
    
    style BQ fill:#dbeafe,stroke:#1e40af
    style Looker fill:#fef3c7,stroke:#d97706
```

## 4️⃣ Resource Hierarchy & Billing 🏛️
*   **Organization Node:** The root.
*   **Billing Account:** Lives at the Organization level (usually).
*   **Project:** *Linked* to **one** Billing Account.
    *   *Trap:* A project *must* have a billing account to use paid services.
*   **Labels:** The **most important** tool for FinOps.
    *   Label resources: `env:prod`, `team:data`, `cost-center:101`.
    *   *Result:* In the bill, you can filter by `team:data`.

## 5️⃣ Exam Traps 🚨
*   **Trap:** "I want to stop the VM automatically if it costs more than $100."
    *   *Answer:* **Budgets DO NOT stop resources.** They only send alerts (Emails/PubSub). To *stop* a VM, you must link the Pub/Sub alert to a **Cloud Function** that runs a script to stop the VM.
*   **Trap:** "Who pays for the data transfer between Project A and Project B?"
    *   *Answer:* The project that **initiates** the egress pays.
*   **Trap:** "I want to analyze my bill with SQL."
    *   *Answer:* Enable **Billing Export to BigQuery**. (It is not retroactive! Enable it Day 1).

## 6️⃣ Hands-On Lab: Set a "Panic" Budget 📉
1.  **Go to:** Billing > Budgets & Alerts.
2.  **Create Budget:** "Monthly Safety Net".
3.  **Amount:** $50 (or your limit).
4.  **Thresholds:**
    *   50% ($25) -> Email me.
    *   90% ($45) -> Email me AND my manager.
    *   100% ($50) -> Email me.
5.  **Actions:** (Optional) Connect to Pub/Sub to trigger automation.

## 7️⃣ Checkpoint Questions
**Q1. You need the absolute cheapest compute for a batch job that runs for 4 hours and can restart if interrupted.**
*   A. E2 Standard VM
*   B. **Spot VM**
*   C. Committed Use Discount (1 Year)
*   D. Cloud Functions
> **Answer: B.** Spot VMs offer up to 90% off for fault-tolerant workloads.

**Q2. How do you gain access to historical billing data via SQL to create custom operational dashboards?**
*   A. Download CSVs from the Console.
*   B. Use the Billing API.
*   C. **Configure Cloud Billing Export to BigQuery.**
*   D. Use Cloud SQL.
> **Answer: C.** This is the standard pattern for granular cost analysis.

**Q3. True or False: Setting a budget of $100 will automatically turn off your VMs when you hit $100.**
*   A. True
*   B. **False**
> **Answer: B.** Budgets are for *alerting*. Programmatic action requires Pub/Sub + Cloud Functions (CapOps).

## ✅ Day 37 Checklist
<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can identify Orphaned Disks.', checked: false },
        { text: 'I know when to use Committed Use Discounts.', checked: false },
        { text: 'I understand labels for billing attribution.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 37 Checklist
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
