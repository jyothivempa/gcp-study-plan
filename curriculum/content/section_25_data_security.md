# Day 25: Data Security (Encryption & KMS)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐ Medium

---

## 🎯 Learning Objectives

By the end of Day 25, learners will be able to:
*   **Explain** how GCP encrypts data by default.
*   **Differentiate** between Google-Managed Keys vs CMEK.
*   **Create** a Key in Cloud KMS.

---

## 🧠 1. Encryption Everywhere

Good News: **Google encrypts ALL data at rest and in transit by default.**
You don't need to click a button for this. It just happens.

However, some industries (Banking, Healthcare) have a rule:
*"Google cannot own the keys. WE must own the keys."*

---

## 🔑 2. Key Management Types

1.  **Google-Managed Keys (Default):** Google creates the key, rotates it, and manages it. You do nothing. (99% of use cases).
2.  **Customer-Managed Encryption Keys (CMEK):** **You** create the key in **Cloud KMS**. You manage rotation. You can **destroy** the key (making the data unreadable, even to Google).
3.  **Customer-Supplied Encryption Keys (CSEK):** You bring your own raw key bytes from on-prem. Google never stores the key. (Rare/Extreme).

---

## ✉️ 3. Real-World Analogy: The Secret Envelope

*   **Google-Managed:** You put your letter in a safe. Google holds the key to the safe. They promise to keep it locked.
*   **CMEK (KMS):** You put your letter in a safe. **You hold the key**. Google guards the safe, but they can't open it unless you give permission. If you melt the key, the safe is locked forever.

---

## 🛠️ 4. Hands-On Lab: Create a Crypto Key

**🧪 Lab Objective:** Create a KeyRing and Key in KMS.

### ✅ Steps

1.  **Open Console:** Go to **Security > Key Management**.
2.  **Create Key Ring:**
    *   Name: `my-keyring`.
    *   Location: `us-central1`.
3.  **Create Key:**
    *   Name: `my-crypto-key`.
    *   Protection Level: Software.
    *   Rotation: 90 days (Best practice).
4.  **Use it:**
    *   Go to **Cloud Storage**. Create a Bucket.
    *   Under **Encryption**, verify you can select "Customer-managed key" and pick the one you just made.
    *   *Result:* Now, if you revoke permission to that key, the bucket becomes inaccessible.

---

<!-- QUIZ_START -->
## 📝 5. Quick Knowledge Check (Quiz)

1.  **What is the default encryption state for data stored in GCP?**
    *   A. Unencrypted.
    *   B. **Encrypted at Rest and in Transit.** ✅
    *   C. Encrypted only if you pay.

2.  **You work for a bank. Regulation says you must be able to revoke Google's ability to decrypt data at any time. What do you use?**
    *   A. Default Encryption
    *   B. **CMEK (Cloud KMS)** ✅
    *   C. HTTPS

3.  **What happens if you accidentally delete/destroy a CMEK key?**
    *   A. Google can restore it.
    *   B. **The data encrypted with that key is lost forever (Crypto-shredding).** ✅
    *   C. Nothing, data is fine.

4.  **Which services allow you to use CMEK?**
    *   A. Cloud Storage
    *   B. Cloud SQL
    *   C. Compute Engine (Disks)
    *   D. **All of the above** ✅

5.  **Which service scans your data for sensitive info like Credit Card numbers?**
    *   A. Cloud Armor
    *   B. **Cloud DLP (Data Loss Prevention)** ✅
    *   C. IAM
<!-- QUIZ_END -->
---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand the default encryption.', checked: false },
        { text: 'I created a KMS KeyRing and Key.', checked: false },
        { text: 'I know the risk of destroying a key.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 25 Checklist
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
