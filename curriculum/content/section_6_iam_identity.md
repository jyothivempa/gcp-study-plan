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

## ✅ Day 6 Checklist

- [ ] I can define Principal, Role, and Policy.
- [ ] I understand why Basic roles are bad.
- [ ] I know what a Service Account is.
- [ ] I successfully granted a specific role to a user.
