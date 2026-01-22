# Module 2: Projects & Billing

> **🎯 Objectives:**
> *   Master core concepts
> *   Build hands-on resources
> *   Pass the ACE exam scenarios

| 📚 Concepts | 🧪 Lab | 📝 Quiz | 💼 Interview |
|---|---|---|---|
| [Jump to Theory](#concepts) | [Jump to Lab](#hands-on-lab) | [Jump to Quiz](#knowledge-check) | [Jump to Interview](#interview-questions) |

---


> **🎯 Objectives:**
> *   Master core concepts
> *   Build hands-on resources
> *   Pass the ACE exam scenarios

| 📚 Concepts | 🧪 Lab | 📝 Quiz | 💼 Interview |
|---|---|---|---|
| [Jump to Theory](#concepts) | [Jump to Lab](#hands-on-lab) | [Jump to Quiz](#knowledge-check) | [Jump to Interview](#interview-questions) |

---


> **🎯 Objectives:**
> *   Master core concepts
> *   Build hands-on resources
> *   Pass the ACE exam scenarios

| 📚 Concepts | 🧪 Lab | 📝 Quiz | 💼 Interview |
|---|---|---|---|
| [Jump to Theory](#concepts) | [Jump to Lab](#hands-on-lab) | [Jump to Quiz](#knowledge-check) | [Jump to Interview](#interview-questions) |

---


**Duration:** ⏱️ 45 Minutes  
**Level:** Absolute Beginner  
**ACE Exam Weight:** ⭐⭐⭐⭐ Very High (Projects & Billing appear across the exam)

---

## 🎯 Learning Objectives

By the end of Day 2, learners will be able to:

*   **Explain** what a GCP Project is and why it is required.
*   **Understand** how billing accounts work in Google Cloud.
*   **Use** the GCP Free Tier safely.
*   **Apply** cost-control best practices to avoid surprise bills.
*   **Create** a project and set budgets & alerts correctly.

---

## 🧠 1. What Is a GCP Project? (Plain-English)

**A GCP Project is a logical container that holds all your cloud resources.**

Everything you create in Google Cloud *must* belong to a project:

*   🖥️ **Virtual Machines** (Compute)
*   💾 **Storage Buckets** (Data)
*   🌐 **Networks** (Connectivity)
*   🔐 **IAM Permissions** (Access Control)

👉 **Rule:** No Project = No Resources.

---

## 🌍 2. Real-World Analogy: The Office File Cabinet 🗄️

*   **Company** → Google Cloud Account (The Organization).
*   **File Cabinet** → **GCP Project** (Holds related stuff).
*   **Files/Folders** → **Resources** (VMs, Buckets, Databases).

### Why do we use projects?
1.  **Isolation:** Separate "Dev", "Test", and "Prod" environments completely.
2.  **Cost Tracking:** See exactly how much "Project A" costs vs "Project B".
3.  **Access Control:** Give a developer access to "Dev" but not "Prod".

> **🎯 ACE Tip:** If a question mentions "isolation", "billing separation", or "distinct environments" → The answer is almost always **Projects**.

---

## 🏗️ 3. GCP Resource Hierarchy (Simplified)

Think of it like a folder structure on your computer:

1.  **Google Account** (You)
2.  └── **Billing Account** (Your Credit Card)
3.  &nbsp;&nbsp;&nbsp;&nbsp;└── **Project** (The Container)
4.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── **Compute Engine**
5.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── **Cloud Storage**
6.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── **IAM & Admin**

### Key Rules to Remember:
*   A Project can have only **ONE** Billing Account.
*   A Billing Account can pay for **MULTIPLE** Projects.

---

## 💳 4. Understanding Cloud Billing

GCP uses a **Pay-As-You-Go** model.

### How You Are Charged
*   **Usage:** How much CPU/RAM you use.
*   **Time:** How long a resource runs (per second).
*   **Region:** Some regions (e.g., Zurich) are more expensive than others (e.g., Iowa).

### The Billing Account 💼
*   Holds your payment method (Credit Card / Bank Account).
*   Pays for all linked projects.
*   Can be **disabled** to stop all spending (and stop all resources).

> **🎯 Exam Shortcut:** No active Billing Account = Paid resources **cannot** run.

---

## 🆓 5. GCP Free Tier (Safe Learning Zone)

Google gives you two ways to learn for free:

### 1️⃣ Always Free (No Expiry)
Resources you can use *every month* without paying:
*   **e2-micro VM:** 1 instance (US regions).
*   **Cloud Storage:** 5 GB Standard Storage.
*   **Cloud Functions:** 2 million invocations.

### 2️⃣ Free Trial Credits ($300)
*   **Amount:** $300 USD (or local equivalent).
*   **Validity:** 90 Days.
*   **Usage:** Can be used on almost any GCP service.

> **⚠️ Warning:** The Free Tier is **limited**. If you start a massive 64-core server, you *will* burn through your credits instantly.

---

## 🚨 6. Cost Control Rules (Critically Important)

Follow these rules to avoid "Cloud Shock" bills:

1.  ✅ **Stop/Delete Unused Resources:** Don't leave VMs running overnight unless needed.
2.  ✅ **Use Small Instances:** Stick to `e2-micro` or `e2-small` for practice.
3.  ✅ **Create Budgets:** Always set a budget to get warned *before* you overspend.
4.  ✅ **Clean Up:** Delete projects when you are done with them.

> **🎯 ACE Exam Tip:** If a question asks *"How to avoid unexpected charges?"* → The answer is **Budgets & Alerts**.

---

## 🛠️ 7. Hands-On Lab: Create a Project & Enable Billing

**🧪 Lab Objective:** Create your first GCP project and set up a budget to stay safe.

### ✅ Part 1: Create a Project
1.  **Open** the [GCP Console](https://console.cloud.google.com).
2.  **Click** the **Project Selector** dropdown (top bar, next to the Google Cloud logo).
3.  **Click** **"New Project"**.
4.  **Project Name:** Enter `gcp-learning-day2`.
5.  **Billing Account:** Ensure your active account is selected.
6.  **Click** **Create**. (Wait ~30 seconds).

### ✅ Part 2: Verify Billing Link
1.  **Search** for "Billing" in the top search bar.
2.  **Select** "Billing" from the results.
3.  **Verify** that `gcp-learning-day2` appears in the list of "Projects linked to this billing account".

### ✅ Part 3: Set a Budget (Best Practice)
1.  In the Billing section, click **"Budgets & alerts"** (left menu).
2.  Click **"Create Budget"**.
3.  **Name:** `Monthly-Safety-Budget`.
4.  **Amount:** Set to `Target amount: ₹500` (or $10 USD).
5.  **Actions:** Keep default alerts (50%, 90%, 100%).
6.  **Click** **Finish**.

> **🎉 Success!** You typically receive an email alert if your spend usually hits 50% of this amount. You are now safer to experiment!

---


## ⚠️ 8. Common Exam Traps

Don't fall for these common misconceptions on the ACE exam:

*   ❌ **Trap:** "Stopping a VM stops all costs."
    *   **Truth:** You still pay for the **Disk (Storage)** attached to it!
*   ❌ **Trap:** "Data transfer is free."
    *   **Truth:** Data coming **IN** (Ingress) is usually free. Data going **OUT** (Egress) usually costs money.
*   ❌ **Trap:** "Deleting a VM deletes the Project."
    *   **Truth:** No. The Project remains. To delete everything, delete the **Project**.
---

<!-- QUIZ_START -->
## 📝 9. Quick Knowledge Check (Quiz)

1.  **Every GCP resource must belong to a:**
    *   A. Folder
    *   B. **Project** ✅
    *   C. Billing Account

2.  **Can one Billing Account pay for multiple Projects?**
    *   A. **Yes** ✅
    *   B. No

3.  **What happens if you disable the Billing Account?**
    *   A. Resources run for free
    *   B. **All paid resources stop working** ✅
    *   C. Nothing happens

4.  **What is the best way to prevent surprise bills?**
    *   A. Check the console every hour
    *   B. **Set up Budgets & Alerts** ✅
    *   C. Only use the Free Tier

5.  **True or False: The Free Tier allows unlimited usage of all services.**
    *   A. True
    *   B. **False** ✅
<!-- QUIZ_END -->
---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can explain what a GCP Project is.', checked: false },
        { text: 'I understand how Billing Accounts link to Projects.', checked: false },
        { text: 'I have created my first Project (gcp-learning-day2).', checked: false },
        { text: 'I have set up a Budget to track spending.', checked: false },
        { text: 'I completed the Quiz.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 2 Checklist
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
---

### 🗑️ Lab Cleanup (Mandatory)

> **⚠️ Critical:** Delete resources to avoid unecessary billing!

1.  **Delete Project:** (Fastest way)
    ```bash
    gcloud projects delete $PROJECT_ID
    ```
2.  **Or Delete Resources Individually:**
    ```bash
    # Example commands (verify before running)
    gcloud compute instances delete [INSTANCE_NAME] --quiet
    gcloud storage rm -r gs://[BUCKET_NAME]
    ```