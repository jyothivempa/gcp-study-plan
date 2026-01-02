# Day 10: Cloud SQL (Managed Relational Databases)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐ Medium

---

## 🎯 Learning Objectives

By the end of Day 10, learners will be able to:
*   **Explain** managed database benefits (vs installing MySQL on a VM).
*   **Choose** between Cloud SQL, Spanner, and BigQuery.
*   **Connect** to a Cloud SQL instance.

---

## 🧠 1. What Is Cloud SQL?

**Cloud SQL** is a fully managed relational database service.
It runs **MySQL**, **PostgreSQL**, or **SQL Server**.

### "Fully Managed" means Google handles:
*   ✅ Backups (Automated daily).
*   ✅ Patching (No more OS updates).
*   ✅ Failover (High Availability).
*   ✅ Replication (Read Replicas).

You just write SQL queries.

---

## 👔 2. Real-World Analogy: Hiring a DBA

*   **MySQL on Compute Engine:** You are the janitor, the mechanic, and the driver. You fix the server when it breaks.
*   **Cloud SQL:** You **hired a Database Administrator (DBA)** named Google.
    *   You tell Google: "Make sure this never goes down." (Enable HA).
    *   You tell Google: "Back it up every night." (Config).
    *   Google does the work. You pay a salary (Management fee).

---

## ⚖️ 3. Cloud SQL vs Other DBs (Exam Key)

| Service | Type | Use Case | Scale |
| :--- | :--- | :--- | :--- |
| **Cloud SQL** | Relational (SQL) | Traditional Apps, ERP, CRS, Wordpress. | Regional (Up to ~64TB). |
| **Cloud Spanner** | Relational (SQL) | Global Banking, Global Inventory. | **Global** (Unlimited Horizontal Scale). |
| **BigQuery** | Warehouse (SQL) | Analytics, Dashboarding, ML. | Petabytes. |
| **Firestore** | NoSQL | Mobile Apps, User Profiles, Game State. | Document Scale. |

> **🎯 ACE Tip:**
> *   "Global SQL Database with horizontal scale" → **Spanner**.
> *   "Lift and shift existing MySQL/Postgres" → **Cloud SQL**.
> *   "Analytics" → **BigQuery**.

---

## 🛠️ 4. Hands-On Lab: Create a MySQL Instance

**🧪 Lab Objective:** Spin up a managed MySQL database.

### ✅ Steps

1.  **Open Console:** Go to **SQL**.
2.  **Create:** Click **Create Instance**.
3.  **Engine:** Choose **MySQL**.
4.  **Config:**
    *   **Instance ID:** `my-test-db`.
    *   **Password:** Generate or set a strong one. Save it!
    *   **Database Version:** MySQL 8.0.
    *   **Region:** `us-central1`.
    *   **Zonal Availability:** Single Zone (Cheaper for lab).
5.  **Create:** Click Create. **(This takes 5-10 minutes!)**
6.  **Connect:**
    *   Once green, click **Open Cloud Shell**.
    *   Run: `gcloud sql connect my-test-db --user=root`
    *   Enter password.
    *   Run SQL: `SHOW DATABASES;`

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Which database engine is NOT supported by Cloud SQL?**
    *   A. MySQL
    *   B. PostgreSQL
    *   C. SQL Server
    *   D. **Oracle** ✅

2.  **You need a relational database that scales horizontally across the globe. Which service should you choose?**
    *   A. Cloud SQL
    *   B. **Cloud Spanner** ✅
    *   C. BigQuery
    *   D. Bigtable

3.  **What is the main benefit of "Managed" Cloud SQL over "MySQL on a VM"?**
    *   A. It is free.
    *   B. **Google handles patching, backups, and failover.** ✅
    *   C. You get root OS access (You don't).

4.  **To increase read performance for a reporting app, what should you add to Cloud SQL?**
    *   A. High Availability (HA)
    *   B. **Read Replicas** ✅
    *   C. More disk space

5.  **When should you choose BigQuery over Cloud SQL?**
    *   A. For transaction processing (OLTP).
    *   B. **For analytical queries on massive datasets (OLAP).** ✅
    *   C. For hosting a Wordpress site.

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can list the 3 engines supported by Cloud SQL.', checked: false },
        { text: 'I understand when to use Spanner vs Cloud SQL.', checked: false },
        { text: 'I created a Cloud SQL instance.', checked: false },
        { text: 'I connected via Cloud Shell.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 10 Checklist
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
