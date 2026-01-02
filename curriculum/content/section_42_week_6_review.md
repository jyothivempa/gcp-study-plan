# Week 6 Review: The Capstone Experience & SRE Mindset

**Duration:** ⏱️ 60 Minutes  
**Level:** Comprehensive  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical (Scenario Synthesis)

---

## 🏗️ 1. The Capstone Skills Tree

This week, you transitioned from a "student" to a "builder." You solved four real-world scenarios that mirrored the complexity of the ACE exam's highest-weighted questions.

```mermaid
mindmap
  root((Week 6 Mastery))
    Networking
      "Custom VPC Flow"
      "Cloud NAT/Router"
      "Firewall Tagging"
    Security
      "Least Privilege IAM"
      "Custom Roles"
      "IAP Tunnels"
    DevOps
      "Cloud Build YAML"
      "Artifact Registry"
      "Deployment Strategies"
    Data
      "BigQuery Partitioning"
      "Dry Run Auditing"
      "Columnar Optimization"
```

---

## 📈 2. SRE: Balancing Reliability vs. Agility

Site Reliability Engineering (SRE) is the "secret sauce" of Google's operations. The ACE exam expects you to understand how to balance innovation with stability.

| Concept | The "Human" Definition | The "Exam" Definition |
| :--- | :--- | :--- |
| **SLI** | "How are we doing right now?" | A specific metric (Latency, Error Rate). |
| **SLO** | "The goal we usually hit." | A target value for an SLI (99.9% success). |
| **SLA** | "The contract with legal teeth." | A business agreement with financial penalties. |
| **Error Budget** | "Permission to break things." | The amount of downtime allowed before stopping new features. |

**Pro Tip:** If you have 100% of your Error Budget left, you are moving too slowly! Use that budget to push new features or perform risky migrations.

---

## 💼 3. Career Pivot: Building Your Portfolio

The projects you built this week aren't just for learning; they are for your resume.

*   **Network Fix:** Showcases your ability to troubleshoot complex hybrid-cloud connectivity.
*   **Hardened IAM:** Demonstrates that you are a "Security-First" engineer.
*   **Automated Pipeline:** Proves you can scale infrastructure without "ClickOps."
*   **Optimized BigQuery:** Shows you understand cloud costs (FinOps).

---

## 📝 4. Advanced Mock Exam (Week 6)

<!-- QUIZ_START -->
1.  **Your application has an SLO of 99.9% availability per month. You have experienced 40 minutes of downtime this month. Your monthly 'Error Budget' is 43 minutes. What should you do?**
    *   A. Stop all new feature releases immediately.
    *   B. **Proceed with caution. You have 3 minutes of budget left.** ✅
    *   C. Ignore it; 40 minutes is close enough.
    *   D. Delete the project and restart.

2.  **A team is using a basic 'roles/editor' permission for their Service Accounts. You recommend 'Custom Roles.' What is the primary benefit?**
    *   A. It reduces the monthly bill.
    *   B. **It reduces the 'Attack Surface' by following the Principle of Least Privilege.** ✅
    *   C. It makes the build process faster.
    *   D. It allows access to the Free Tier.

3.  **Which combination of services allows a private VM to download internet updates while blocking all direct inbound traffic?**
    *   A. VPC Peering + Cloud SQL.
    *   B. **Cloud NAT + Cloud Router + VPC Firewall (Default Egress).** ✅
    *   C. Global Load Balancer + Cloud Armor.
    *   D. App Engine + Secret Manager.

4.  **How does 'Partitioning' in BigQuery directly contribute to FinOps goals?**
    *   A. It encrypts data for free.
    *   B. **It allows the query engine to prune unrelated data, reducing the bytes scanned and thus lowering cost.** ✅
    *   C. It makes the dashboard look better.
    *   D. It increases the throughput of the API.

5.  **A developer committed a Service Account JSON key to a public GitHub repo. What is the immediate 'SRE' response?**
    *   A. Ask the developer to delete the file from Git.
    *   B. **Disable/Delete the key in GCP Console and rotate the credentials immediately.** ✅
    *   C. Change the developer's password.
    *   D. Do nothing; the repo is private now.
<!-- QUIZ_END -->

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can explain the relationship between SLIs and SLOs.', checked: false },
        { text: 'I know when to use an Error Budget to push features.', checked: false },
        { text: 'I understand why long-lived JSON keys are a security risk.', checked: false },
        { text: 'I can articulate the value of my capstone projects to an employer.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Week 6 Mastery Checklist
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
