# Day 4: Cloud Storage (GCS) & Storage Classes

**Duration:** ⏱️ 45 Minutes  
**Level:** Beginner  
**ACE Exam Weight:** ⭐⭐⭐⭐ Very High

---

## 🎯 Learning Objectives

By the end of Day 4, learners will be able to:
*   **Explain** how Cloud Storage differs from a Disk.
*   **Choose** the correct Storage Class (Standard vs Nearline vs Coldline vs Archive).
*   **Create** a Bucket and upload objects.
*   **Understand** Object Versioning.

---

## 🧠 1. What Is Cloud Storage? (Plain-English)

**Cloud Storage** is "Object Storage". 
It is NOT a hard drive attached to a VM (that's Persistent Disk).

### Key Features:
*   **Infinite Scale:** Store exabytes of data.
*   **Global Access:** Accessible via URL (HTTP) from anywhere.
*   **Serverless:** No VM to manage. Just upload files.

---

## 🤖 2. Real-World Analogy: Google Drive for Robots

*   **Google Drive** is for **Humans** (drag and drop, UI, docs).
*   **Cloud Storage** is for **Applications** (APIs, code, massive scale).

Think of a **Bucket** like a **Folder** in the cloud that has a unique name.
Think of an **Object** like a **File** inside that bucket.

---

## 🧊 3. Storage Classes (The "Temperature" of Data)

Google charges you less if you promise to access data less often.

| Class | Use Case | "Temperature" | Min Duration |
| :--- | :--- | :--- | :--- |
| **Standard** | Streaming videos, websites, "Hot" data used daily. | 🔥 Hot | None |
| **Nearline** | Backups aimed at once-a-month access. | 🌤️ Warm | 30 Days |
| **Coldline** | Disaster recovery, accessed once-a-quarter. | ❄️ Cold | 90 Days |
| **Archive** | Regulation logs, "Tape" replacement, accessed once-a-year. | 🧊 Frozen | 365 Days |

> **🎯 ACE Tip:** 
> *   "Access frequently" → **Standard**.
> *   "Access once a month" → **Nearline**.
> *   "Long-term retention / Regulations" → **Archive**.

---

## 🛠️ 4. Hands-On Lab: Host a Static Website

**🧪 Lab Objective:** Create a bucket and host a simple public file.

### ✅ Steps

1.  **Open Console:** Go to **Cloud Storage** > **Buckets**.
2.  **Create:** Click **Create**.
3.  **Name:** `my-unique-bucket-name-xyz` (Must be globally unique!).
4.  **Settings:**
    *   **Region:** `us-central1`
    *   **Class:** `Standard`
    *   **Access Control:** Uncheck "Enforce public access prevention" (So we can share it).
    *   **Access Control:** Choose **Uniform**.
5.  **Upload:** Upload an image or `index.html` file.
6.  **Make Public:**
    *   Go to **Permissions** tab.
    *   Click **Grant Access**.
    *   Add Principal: `allUsers`.
    *   Role: `Storage Object Viewer`.
    *   Save.
7.  **Test:** Click the "Public URL" link next to your file. It works!

> **⚠️ Security Warning:** Only do this for public websites. Never grant `allUsers` access to private data!

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Which storage class is cheapest for storing data you plan to access only once a year?**
    *   A. Standard
    *   B. Nearline
    *   C. **Archive** ✅
    *   D. Coldline

2.  **What must be unique about a Bucket Name?**
    *   A. Unique within your project.
    *   B. **Globally unique across ALL of Google Cloud.** ✅
    *   C. Just contains your name.

3.  **Cloud Storage is what type of storage?**
    *   A. Block Storage
    *   B. File Storage
    *   C. **Object Storage** ✅

4.  **How do you make a file downloadable by anyone on the internet?**
    *   A. Send them the password.
    *   B. **Grant the 'Storage Object Viewer' role to 'allUsers'.** ✅
    *   C. You cannot do this.

5.  **Is Cloud Storage used for running an Operating System?**
    *   A. Yes
    *   B. **No (That's Persistent Disk)** ✅

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I can pick the right Storage Class.', checked: false },
        { text: 'I created a globally unique bucket.', checked: false },
        { text: 'I uploaded a file.', checked: false },
        { text: 'I configured IAM to make an object public.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 4 Checklist
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
