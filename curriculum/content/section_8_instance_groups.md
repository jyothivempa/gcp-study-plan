# Day 8: Instance Groups & Auto-healing

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High (Scaling concepts are frequent)

---

## 🎯 Learning Objectives

By the end of Day 8, learners will be able to:
*   **Differentiate** between Unmanaged vs Managed Instance Groups (MIGs).
*   **Configure** Auto-healing to replace broken VMs.
*   **Understand** Auto-scaling logic.

---

## 🧠 1. What Are Instance Groups?

An **Instance Group** is a collection of VM instances that you manage as a single entity.

### Two Types:
1.  **Unmanaged Instance Group:** A bag of random VMs. Used for legacy apps that need to be grouped for a load balancer. (Rarely used).
2.  **Managed Instance Group (MIG):** Identical VMs created from a template. 
    *   **Auto-Healing:** If a VM crashes, MIG replaces it.
    *   **Auto-Scaling:** Adds/removes VMs based on CPU load.
    *   **Updates:** Rollover updates with 0 downtime.

---

## 💂 2. Real-World Analogy: Cloning an Army

*   **Single VM** = **Captain America**. He is unique. If he gets sick, you have 0 heroes.
*   **MIG** = **Stormtroopers**. They are all identical (Clones).
    *   If one falls, the Empire just sends another one (**Auto-healing**).
    *   If the rebels attack, the Empire sends 100 more (**Auto-scaling**).

> **Key Concept:** In a MIG, VMS are **Stateless**. You don't name them "Web-Server-1". You treat them like cattle, not pets.

---

## 🛠️ 3. Hands-On Lab: Create a MIG

**🧪 Lab Objective:** Create a group of Apache web servers that auto-heals.

### ✅ Steps

**Phase 1: Create the Template (The Blueprint)**
1.  Go to **Compute Engine** > **Instance Templates**.
2.  Click **Create Instance Template**.
3.  Name: `web-server-v1`.
4.  Machine type: `e2-micro`.
5.  **Startup Script (Advanced > Management):**
    ```bash
    #! /bin/bash
    apt update && apt install -y apache2
    echo "This is a Replica!" > /var/www/html/index.html
    ```
6.  Firewall: Allow HTTP traffic.
7.  Click **Create**.

**Phase 2: Create the Group (The Army)**
1.  Go to **Instance Groups** (left menu).
2.  Click **Create Instance Group**.
3.  Select **New Managed Instance Group (Stateless)**.
4.  Name: `my-web-cluster`.
5.  Template: Select `web-server-v1`.
6.  Location: Single Zone (`us-central1-a`).
7.  **Autoscaling:** Set "Minimum number of instances" to **2**.
8.  Click **Create**.

**Phase 3: Verify Auto-healing**
1.  Wait for the 2 VMs to start (green check).
2.  **Delete** one of the VMs manually.
3.  Wait 30 seconds... The MIG will automatically notice it's missing and **create a new one**. Spooky!

---

## 📝 4. Quick Knowledge Check (Quiz)

1.  **Which type of Instance Group contains identical VMs created from a template?**
    *   A. Unmanaged
    *   B. **Managed (MIG)** ✅
    *   C. Zonal

2.  **What happens if you manually delete a VM that belongs to a MIG?**
    *   A. The Group size shrinks permanently.
    *   B. **The MIG detects the loss and re-creates the VM automatically.** ✅
    *   C. You get a billing credit.

3.  **For Auto-scaling to work, your application should ideally be:**
    *   A. Stateful (Stores data locally)
    *   B. **Stateless (Stores data in a DB/Bucket)** ✅
    *   C. Massive

4.  **Where do you define the Startup Script for a MIG?**
    *   A. In the Group settings.
    *   B. **In the Instance Template.** ✅
    *   C. You cannot use startup scripts.

5.  **You need to update the OS version for all 100 VMs in your MIG. What is the feature called?**
    *   A. Manual Restart
    *   B. **Rolling Update** ✅
    *   C. Blue/Green Deployment

---

## ✅ Day 8 Checklist

- [ ] I can describe the difference between Pets (Single VM) and Cattle (MIG).
- [ ] I created an Instance Template.
- [ ] I launched a MIG with 2 instances.
- [ ] I tested Auto-healing by deleting a VM.
