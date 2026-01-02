# Day 11: Cloud Storage Advanced (Lifecycle & Security)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐ Medium

---

## 🎯 Learning Objectives

By the end of Day 11, learners will be able to:
*   **Automate** cost savings with Lifecycle Policies.
*   **Protect** data with Object Versioning.
*   **Secure** uploads with Signed URLs.

---

## 🧠 1. Lifecycle Policies (Automated Housekeeping)

You don't want to manually move old files to "Coldline" or "Archive" storage.
**Lifecycle Management** does it for you based on rules.

### Common Rules:
*   "If file is older than 30 days -> Move to Nearline."
*   "If file is older than 365 days -> Move to Archive."
*   "If file has 3 newer versions -> Delete the old one."

---

## 📜 2. Real-World Analogy: The Archivist

*   **You (User):** You dump files on the desk.
*   **Lifecycle Policy (The Archivist):**
    *   "This paper is a month old. I'll move it to the basement (**Nearline**) to save desk space."
    *   "This tax record is a year old. I'll move it to the off-site warehouse (**Archive**)."
    *   "This draft is trash. I'll shred it (**Delete**)."

---

## 🛡️ 3. Object Versioning

What happens if you overwrite `report.docx` with a blank file by mistake?
Without Versioning: It's gone.
**With Versioning:** Google keeps the old copy hidden. You can restore it.

> **Cost Warning:** You pay for **every version**. If you overwrite a 1GB file 10 times, you pay for 10GB. Always combine Versioning with Lifecycle Policies (e.g., "Keep max 3 versions").

---

## ✍️ 4. Signed URLs (Temporary Access)

How do you let a user upload a file *without* giving them a Google Account?
**Signed URL:** A magic link that gives permission for a limited time (e.g., 10 minutes).

**Use Case:** A "Upload Profile Picture" button on your website. Your backend generates a Signed URL, gives it to the user, and the user uploads directly to GCS.

---

## 🛠️ 5. Hands-On Lab: Lifecycle & Versioning

**🧪 Lab Objective:** Configure automatic deletion and test file recovery.

### ✅ Steps

1.  **Open Bucket:** Go to the bucket you created in Day 4.
2.  **Enable Versioning:**
    *   Click **Configuration** tab (or "Protection").
    *   Find "Object Versioning". Set to **On**.
3.  **Test Versioning:**
    *   Upload a text file named `test.txt` (Content: "Version 1").
    *   Upload another file named `test.txt` (Content: "Version 2").
    *   In the bucket view, click "Version History" (toggle). You see both!
4.  **Set Lifecycle Rule:**
    *   Click **Lifecycle** tab.
    *   Click **Add a rule**.
    *   **Action:** Select "Delete object".
    *   **Condition:** Select "Newer versions" and enter `2`.
    *   **Create.**
    *   *Meaning:* If I upload a 3rd version, the 1st (oldest) version will be deleted to save space.

---

## 📝 6. Quick Knowledge Check (Quiz)

1.  **What is the primary purpose of Lifecycle Management?**
    *   A. To speed up downloads.
    *   B. **To automate moving/deleting objects for cost optimization.** ✅
    *   C. To encrypt data.

2.  **You enabled Object Versioning. You overwrite a 100MB file 5 times. How much storage are you paying for?**
    *   A. 100MB
    *   B. **500MB** ✅
    *   C. 0MB

3.  **To verify that an uploaded file hasn't been corrupted, which feature should you check?**
    *   A. CRC32c / MD5 Hash
    *   B. **Content-Type**
    *   C. The file size only

4.  **You want to let a user upload a file directly to Cloud Storage securely without a GCP account. What should you generate?**
    *   A. A public bucket.
    *   B. **A Signed URL.** ✅
    *   C. An IAM Policy.

5.  **Which Lifecycle condition helps clean up old versions?**
    *   A. "Age"
    *   B. **"Number of newer versions"** ✅
    *   C. "Storage Class matches Standard"

---

## ✅ Day 11 Checklist

- [ ] I understand Lifecycle rules.
- [ ] I enabled Object Versioning.
- [ ] I setup a rule to clean up old versions.
- [ ] I know what a Signed URL is used for.
