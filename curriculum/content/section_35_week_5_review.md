# WEEK 5 REVIEW: Architecture & Data

## 1️⃣ The "Big Picture" Recap
We moved from "Building Components" to "Designing Solutions".
*   **Dataflow vs Dataproc:** New Streaming vs Legacy Hadoop.
*   **BigQuery:** Where data goes to be analyzed (Petabyte scale).
*   **Pub/Sub:** The "Shock Absorber" that decouples systems.
*   **Hybrid:** Connecting the old world (On-Prem) to the new world (Cloud).

## 2️⃣ Decision Tree Cheat Sheet
1.  **Strict Latency requirements?** -> Hybrid Interconnect (Fiber).
2.  **Need Cheap/Fast Connectivity?** -> Cloud VPN.
3.  **Need to ingest 1M events/sec?** -> Pub/Sub.
4.  **Processing streaming data?** -> Dataflow.
5.  **Running Spark jobs?** -> Dataproc.
6.  **Analyze 10TB of CSVs?** -> BigQuery.

## 3️⃣ Mock Questions (Week 5)

**Q1. You need to connect your on-premise Oracle database to a Cloud Application with private IP RFC1918 addresses. You cannot use the public internet. Speed is not critical, but budget is low.**
*   A. Dedicated Interconnect.
*   B. Carrier Peering.
*   C. **Cloud VPN.**
*   D. Transfer Appliance.
> **Answer: C.** VPN is the cheapest private connection method. *Wait!* The question says "Cannot use public internet". VPN uses public internet as transport (encrypted). If strict "No Internet" is required, you MUST use Interconnect. *However*, usually "Private IP access" implies VPN is acceptable. If "No Public Internet" is the hard constraint, **Partner Interconnect** is the entry-level private fiber option.

**Q2. Which BigQuery feature reduces cost by pruning the amount of data scanned?**
*   A. Clustering.
*   B. **Partitioning.**
*   C. Indexing.
*   D. Sharding.
> **Answer: B.** Partitioning splits files by date.

**Q3. Startups often use Pub/Sub between their frontend and backend. Why?**
*   A. It makes the database faster.
*   B. **Decoupling (If the backend crashes, the frontend can still accept messages).**
*   C. It encrypts data.
> **Answer: B.** Reliability pattern: "Fail independently."

## ✅ Week 5 Checklist
<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can draw a Hybrid Network diagram (VPN/Interconnect).', checked: false },
        { text: 'I know when to use Dataflow (Beam) vs Dataproc (Spark).', checked: false },
        { text: 'I understand BigQuery pricing (Slots vs On-Demand).', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Week 5 Confidence Checklist
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
