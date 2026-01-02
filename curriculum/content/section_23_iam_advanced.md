# Day 23: IAM Advanced (Service Accounts)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical

---

## 🎯 Learning Objectives

By the end of Day 23, learners will be able to:
*   **Define** a Service Account (SA).
*   **Differentiate** between User Accounts and Service Accounts.
*   **Troubleshoot** "Permission Denied" errors using the Policy Troubleshooter.

---

## 🧠 1. What Is a Service Account?

We talked about **You** (User) accessing GCP in Day 6.
But how does **Your App** (running on a VM) access a Bucket?
Apps don't have Gmail addresses. They don't have passwords.

**Solution:** **Service Account (SA)**.
*   An Identity for a machine.
*   Email looks like: `my-app@project-id.iam.gserviceaccount.com`.
*   You grant Roles to the SA, just like a User.

---

## 🎫 2. Real-World Analogy: The VIP Staff Pass

*   **User Account** = **Driver's License**. Identifies a specific human (Bob).
*   **Service Account** = **"STAFF" Badge**. 
    *   Whoever wears the badge (VM, Cloud Function) gets access to the Staff Room (Bucket).
    *   The badge doesn't care *which human* started the VM. It only cares that the VM has the badge.

---

## 🔑 3. Keys vs Managed Identity

Two ways to "wear" the badge:
1.  **Attached (Managed):** You attach the SA to the VM when creating it.
    *   **Secure.** Google rotates the keys automatically.
    *   *Recommended.*
2.  **Keys (JSON file):** You download a `.json` key file.
    *   **Dangerous!** If you leak this on GitHub, hackers are instantly YOU.
    *   *Avoid unless absolutely necessary (e.g., On-prem server).*

---

## 🛠️ 4. Hands-On Lab: Service Account Access

**🧪 Lab Objective:** Create a VM that *cannot* access Storage, then fix it.

### ✅ Steps

1.  **Create Bucket:** `gsutil mb gs://my-secret-bucket-[RANDOM]`
2.  **Create VM (Default SA):**
    *   Create a standard VM. (It uses the *Compute Engine Default SA*).
    *   SSH into it.
    *   Run `gsutil ls gs://my-secret-bucket...` -> **Success**.
    *   *Why?* The Default SA is too powerful (Editor role).
3.  **Create Custom SA:**
    *   IAM > Service Accounts > Create.
    *   Name: `restricted-sa`. Do **NOT** grant any roles yet.
4.  **Create VM (Restricted):**
    *   Create VM. In **Identity and API Access**, select `restricted-sa`.
    *   SSH into it.
    *   Run `gsutil ls ...` -> **AccessDeniedException**.
5.  **Fix it:**
    *   Go to Console > Storage > Bucket.
    *   Grant `Storage Object Viewer` to `restricted-sa@...`.
    *   Try SSH command again. -> **Success!**

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **What is a Service Account?**
    *   A. A Gmail account for admins.
    *   B. **A special account representing a non-human application/machine.** ✅
    *   C. A billing account.

2.  **Which practice is recommended for granting access to a VM running on GCP?**
    *   A. Download a JSON key and upload it to the VM.
    *   B. **Attach the Service Account to the VM (Managed Identity).** ✅
    *   C. Hardcode your username/password.

3.  **You accidentally uploaded a Service Account JSON key to a public GitHub repo. What should you do?**
    *   A. Delete the repo.
    *   B. **Revoke/Delete the key immediately in console.** ✅
    *   C. Hope no one sees it.

4.  **Your colleague gets a "403 Permission Denied" error. Which tool helps identify the missing role?**
    *   A. Cloud Debugger
    *   B. **Policy Troubleshooter** ✅
    *   C. Cloud Trace

5.  **The "Compute Engine Default Service Account" has which role by default?**
    *   A. Viewer
    *   B. **Editor (Very broad!)** ✅
    *   C. Owner

---

## ✅ Day 23 Checklist

- [ ] I know what a Service Account is.
- [ ] I created a custom SA with limited permissions.
- [ ] I successfully swapped a VM's identity.
