# Day 26: Billing & Resource Management

**Duration:** ⏱️ 45 Minutes  
**Level:** Beginner  
**ACE Exam Weight:** ⭐⭐⭐ Medium

---

## 🎯 Learning Objectives

By the end of Day 26, learners will be able to:
*   **Set up** Billing Budgets and Alerts.
*   **Understand** Quotas and how to request increases.
*   **Export** billing data to BigQuery for analysis.

---

## 🧠 1. The Cloud Bill

The cloud is "Pay as you go". This is great, until you leave a massive GPU cluster running over the weekend.
**Cost Management safeguards are mandatory.**

### Key Concepts:
1.  **Budget:** A target amount (e.g., $100).
2.  **Alert:** A notification sent when you hit 50%, 90%, or 100% of the budget.
    *   *Note:* Alerts do **NOT** stop services. They just scream at you via Email.
3.  **Quota:** Hard limits on resources (e.g., "Max 5 CPUs per region") to prevent accidental massive spending.

---

## 💳 2. Real-World Analogy: The Credit Limit

*   **Quota** = **Your Credit Card Limit ($5000)**.
    *   Standard safeguard. You can ask bank to raise it.
    *   Prevents you from accidentally buying an island.
*   **Budget Alert** = **SMS Notification**.
    *   "You have spent $50." -> "You have spent $90."
    *   It doesn't freeze the card. It just warns you.

---

## 🛠️ 3. Hands-On Lab: Set a Budget

**🧪 Lab Objective:** Create a safeguard for your project.

### ✅ Steps

1.  **Open Console:** Go to **Billing**.
2.  **Menu:** Select **Budgets & alerts**.
3.  **Create:** Click **Create Budget**.
    *   Name: `My Learning Budget`.
    *   Time range: Monthly.
    *   Amount: **Specified amount** -> **$20.00**.
4.  **Actions:**
    *   Thresholds: 50%, 90%, 100%.
    *   Notifications: Email alerts to billing admins.
5.  **Finish:** Click Save.
    *   *Result:* If your labs cost $10, you will get an email.

---

## 📊 4. BigQuery Export

The Billing console is nice, but what if you need to know: *"How much did Project A spend on Storage in Tokyo on Tuesday?"*
For detailed SQL analysis, you **Export Billing Data to BigQuery**.
This is a common exam question!

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Does setting a Billing Budget automatically stop your VMs when the limit is reached?**
    *   A. Yes
    *   B. **No, it only sends alerts.** ✅
    *   C. Yes, but only for Compute Engine.

2.  **You can't create a database because you reached the "Limit of 5 instances". What is this called?**
    *   A. Budget
    *   B. **Quota** ✅
    *   C. Firewall

3.  **How do you analyze complex spending patterns using SQL?**
    *   A. Download a CSV.
    *   B. **Enable Billing Export to BigQuery.** ✅
    *   C. Use Cloud Monitoring.

4.  **Who can link a Project to a Billing Account?**
    *   A. Any editor.
    *   B. **Billing Account User (or Admin).** ✅
    *   C. Viewer.

5.  **What is the best way to categorize costs (e.g. separate "Dev" vs "Prod" spend)?**
    *   A. Use separate credit cards.
    *   B. **Use Labels (e.g. env=prod) and filter billing reports.** ✅
    *   C. Quotas.

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I created a Budget of $20.', checked: false },
        { text: 'I verified my Email is set for alerts.', checked: false },
        { text: 'I understand that Budgets do NOT stop spending.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 26 Checklist
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
