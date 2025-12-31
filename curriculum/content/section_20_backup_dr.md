# SECTION 20: Backup & Disaster Recovery

## 1️⃣ Plain-English Explanation
*   **Backup:** Making a photocopy of your passport. If you lose the passport, you buy a new one and use the photocopy to prove who you are.
*   **Disaster Recovery (DR):** Having a second passport, a second suitcase, and a second plane ticket in a safe deposit box in another country. If your house burns down, you fly there and carry on.

*   **RPO (Recovery Point Objective):** How much data can you lose? (e.g., "I can lose the last 15 minutes of work").
*   **RTO (Recovery Time Objective):** How long can you be offline? (e.g., "I must be back online in 4 hours").

## 2️⃣ Snapshots (The Magic Button)
In GCP, the most important backup tool is the **Snapshot**.
*   **Disk Snapshot:** Captures the exact state of your VM's hard drive.
*   **Incremental:** The first snapshot takes 10 minutes (Full Copy). The second snapshot takes 10 seconds (Only copies what changed). *Saves huge money.*
*   **Global:** Snapshots are stored in Cloud Storage. You can take a snapshot in `us-central1` and restore it to a new VM in `asia-south1`. This is how you move VMs across the world!

## 3️⃣ DR Strategies (Exam Focus)
1.  **Cold (Cheapest):** Backup data to Archive storage. No servers running. RTO = Days.
2.  **Warm (Middle):** Database is running, but App Servers are off. You turn them on when disaster strikes. RTO = Minutes/Hours.
3.  **Hot (Expensive):** Everything is running in two regions at once (Active-Active). Load Balancer sends traffic to both. RTO = Near Zero.

## 4️⃣ Exam Scenarios & Traps 🚨
*   **Trap:** "I need to move a VM from Project A to Project B."
    *   *Answer:* Create an **Image** from the Disk, then create a new VM in Project B from that Image.
*   **Trap:** "Can I schedule snapshots automatically?"
    *   *Answer:* Yes. Use a **Snapshot Schedule**. (e.g., "Every night at 2 AM, keep for 14 days").

## 5️⃣ One-Line Memory Hook 🧠
> "Snapshots are **Global** teleportation devices for your VMs."

## 6️⃣ Checkpoint Questions
1.  **True or False: Snapshots are Zonal resources.**
    *   *Answer: False. They are stored globally (or multi-regionally) in Cloud Storage.*
2.  **If I delete the VM, is the Snapshot deleted?**
    *   *Answer: No. Snapshots live independently.*
3.  **Which DR strategy has the lowest cost: Hot, Warm, or Cold?**
    *   *Answer: Cold.*

## ➡️ What’s Next 
We have the tools. Now we need to think like an Architect. How do we combine them?
**Next Section:** Architecture Thinking.



## ⚡ Zero-to-Hero: Pro Tips
*   **CLI Command**: Practice `gcloud backup list` to see resources via command line.
*   **Real World**: In production, prefer **Terraform** over clicking in the console for backup.


<!-- FLASHCARDS
[
  {
    "term": "RTO",
    "def": "Recovery Time Objective. How long can you be down?"
  },
  {
    "term": "RPO",
    "def": "Recovery Point Objective. How much data can you lose?"
  },
  {
    "term": "Snapshot",
    "def": "Incremental backup of a Persistent Disk."
  },
  {
    "term": "Image",
    "def": "Complete bootable backup of a VM."
  },
  {
    "term": "Cross-Region",
    "def": "Storing backups in a different region for disaster recovery."
  }
]
-->
