# Day 3: Compute Engine (VMs) & Machine Types

**Duration:** ⏱️ 45 Minutes  
**Level:** Beginner  
**ACE Exam Weight:** ⭐⭐⭐ High (VM questions are everywhere)

---

## 🎯 Learning Objectives

By the end of Day 3, learners will be able to:
*   **Explain** what Compute Engine is.
*   **Select** the right Machine Type for a workload.
*   **Understand** Regions vs. Zones.
*   **Deploy** a web server on a Virtual Machine (VM).

---

## 🧠 1. What Is Compute Engine? (Plain-English)

**Compute Engine** is Google's **IaaS** (Infrastructure as a Service) product.

It lets you create **Virtual Machines (VMs)** running on Google's global infrastructure. 
It’s basically renting a raw computer in the cloud.

### Use Cases:
*   Hosting legacy apps.
*   Running databases (MySQL, Postgres).
*   Web servers (Nginx, Apache).
*   Batch processing.

---

## 🍕 2. Real-World Analogy: The Pizza Shop

*   **Compute Engine (IaaS)** is like **Making a Pizza from Scratch**.
    *   You buy the dough, cheese, tomato sauce (**Hardware**).
    *   You choose the oven temp, baking time, and toppings (**OS & Config**).
    *   **Pro:** Total control. You can make any pizza you want.
    *   **Con:** You have to do all the work (patching, updates).

---

## 🏗️ 3. Core Concepts (Exam Critical)

### 🌍 Regions & Zones
*   **Region:** A specific geographical location (e.g., `us-central1`, `europe-west1`).
    *   Contains 3+ Zones.
*   **Zone:** An isolated location within a region (e.g., `us-central1-a`).
    *   Think of it as a separate building in the same campus.
    *   **Rule:** If a Zone goes down, the others survive.

> **🎯 ACE Tip:** For **High Availability**, deploy VMs across **Multiple Zones**. For **Disaster Recovery**, deploy across **Multiple Regions**.

### 💻 Machine Types
Google offers "Families" of VMs for different jobs:

| Family | Purpose | Analogy |
| :--- | :--- | :--- |
| **E2 / N1 / N2** (General Purpose) | Web servers, databases, Dev/Test. | The Toyota Camry. Reliable, balanced. |
| **C2** (Compute Optimized) | Gaming, Video Encoding, High Performance Computing. | The Sports Car (Ferrari). Fast CPU. |
| **M2** (Memory Optimized) | Massive in-memory databases (SAP HANA). | The Moving Van. Huge memory capacity. |

---

## 🛠️ 4. Hands-On Lab: Launch a Web Server

**🧪 Lab Objective:** Create a Linux VM and install the Nginx web server.

### ✅ Steps

1.  **Open Console:** Go to **Compute Engine** > **VM Instances**.
2.  **Create:** Click **Create Instance**.
3.  **Config:**
    *   **Name:** `my-first-web-server`
    *   **Region:** `us-central1` (or close to you)
    *   **Machine type:** `e2-micro` (Free Tier friendly!)
    *   **Boot Disk:** Debian (Default)
4.  **Firewall:** Check the box **"Allow HTTP traffic"**.
5.  **Startup Script (Automation):**
    *   Expand **Advanced Options** > **Management**.
    *   Paste this into "Automation" / "Startup Script":
        ```bash
        #! /bin/bash
        apt update
        apt install -y nginx
        echo "<h1>Hello from Google Cloud! 🍕</h1>" > /var/www/html/index.html
        ```
6.  **Launch:** Click **Create**.
7.  **Verify:** Wait for the green checkmark. Click the **External IP** link. 
    *   You should see your "Hello" message!

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Compute Engine is an example of which service model?**
    *   A. PaaS
    *   B. SaaS
    *   C. **IaaS** ✅
    *   D. FaaS

2.  **You need to ensure your application keeps running even if a single data center loses power. What should you do?**
    *   A. Use a bigger VM.
    *   B. **Deploy VMs in multiple Zones.** ✅
    *   C. Use a specific Region.
    *   D. Backup to a USB drive.

3.  **Which machine family is best for a general-purpose web server?**
    *   A. M2 (Memory Optimized)
    *   B. **E2 (General Purpose)** ✅
    *   C. A2 (Accelerator/GPU)

4.  **What does "Allow HTTP Traffic" actually do?**
    *   A. Installs Chrome.
    *   B. **Creates a Firewall Rule to allow port 80.** ✅
    *   C. Gives you a domain name.

5.  **True or False: You pay for a VM even if it is stopped.**
    *   A. True (Full price)
    *   B. **False (You only pay for the attached Disk)** ✅

---

## ✅ Day 3 Checklist

- [ ] I understand Regions vs Zones.
- [ ] I can choose the right VM family.
- [ ] I created a VM with a Startup Script.
- [ ] I viewed my web page via External IP.
