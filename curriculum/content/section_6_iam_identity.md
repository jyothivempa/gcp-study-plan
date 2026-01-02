# Day 6: IAM (Identity & Access Management)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical (Security is priority #1)

---

## 🎯 Learning Objectives

By the end of Day 6, learners will be able to:
*   **Explain** the "Who, What, Where" of IAM.
*   **Understand** Principals, Roles, and Policies.
*   **Follow** the Principle of Least Privilege.
*   **Assign** a role to a user.

---

## 🧠 1. What Is IAM? (Plain-English)

**IAM** controls **Who** can do **What** on **Which** resource.

It’s the bouncer at the club. It converts "Anyone" into "Authorized Users".

### The Big 3 Concepts:
1.  **Principal (Who):** A Google Account, a Service Account, or a Group (e.g., `bob@gmail.com`).
2.  **Role (What):** A collection of permissions (e.g., `Compute Admin` can create VMs).
3.  **Policy (Binding):** Connecting the **Who** to the **What** on a specific resource.

---

## 🏨 2. Real-World Analogy: Hotel Key Cards

*   **Principal:** The Guest (You).
*   **Role:** The Access Rights (e.g., "Guest Access").
    *   *Permissions:* Open Lobby Door, Open Gym, Open Room 202.
    *   *Note:* You cannot open Room 303 (that requires "Housekeeping" role).
*   **Resource:** The Hotel Room.

**The Golden Rule:** You only give the Guest the key to *their* room, not the Master Key. This is **Least Privilege**.

---

## 📜 3. Types of Roles (Exam Important)

| Type | Description | Recommendation |
| :--- | :--- | :--- |
| **Basic (Primitive)** | Old roles: `Viewer`, `Editor`, `Owner`. Too broad. | ⛔ **Avoid** in production. |
| **Predefined** | Granular roles managed by Google. (e.g., `Compute Admin`). | ✅ **Use these** mostly. |
| **Custom** | You pick specific permissions (e.g., `compute.instances.start`). | 🛠️ Use for specific needs. |

> **🎯 ACE Tip:** If an exam question asks "Which role should you assign to follow best practices?", eliminate `Viewer/Editor/Owner` immediately. Look for the most specific Predefined role.

---

## 🛠️ 4. Hands-On Lab: Granting Access

**🧪 Lab Objective:** Give a user (or yourself) restricted access to view buckets.

### ✅ Steps

1.  **Open Console:** Go to **IAM & Admin** > **IAM**.
2.  **View:** Look at the current list. You are likely the Owner.
3.  **Add:** Click **Grant Access** (or "Add").
4.  **Principal:** Enter a secondary email address (or a friend's).
5.  **Role:**
    *   Type "Storage".
    *   Select **Storage Object Viewer** (Read-only access to files).
6.  **Save:** Click Save.
7.  **Test (Optional):** Open an incognito window, log in as that user, and verify they can *read* files but cannot *delete* them.

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Which component represents the "Who" in IAM?**
    *   A. Role
    *   B. **Principal** ✅
    *   C. Policy

2.  **What is the "Principle of Least Privilege"?**
    *   A. Give everyone Owner access.
    *   B. **Give only the permissions needed to do the job, and no more.** ✅
    *   C. Don't use IAM.

3.  **Which role type should you generally AVOID in production?**
    *   A. Predefined
    *   B. Custom
    *   C. **Basic (Primitive)** ✅

4.  **Bob needs to restart VMs but shouldn't be able to delete them. Which role is best?**
    *   A. Compute Admin (Too powerful)
    *   B. **Compute Instance Admin** (Likely correct, check definitions) ✅ (Actually, `Compute Instance Admin (v1)` allows full control of instances. A custom role might be best, but for standard options, avoid `Project Owner`).
    *   C. Project Editor (Way too powerful)

5.  **A "Service Account" is:**
    *   A. A billing account.
    *   B. **An identity for a machine/application, not a human.** ✅

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can define Principal, Role, and Policy.', checked: false },
        { text: 'I understand why Basic roles are bad.', checked: false },
        { text: 'I know what a Service Account is.', checked: false },
        { text: 'I successfully granted a specific role to a user.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 6 Checklist
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
