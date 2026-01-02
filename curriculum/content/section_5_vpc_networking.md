# Day 5: VPC Networking Basics

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical (Networking is the backbone)

---

## 🎯 Learning Objectives

By the end of Day 5, learners will be able to:
*   **Define** Virtual Private Cloud (VPC).
*   **Understand** Subnets and IP addressing.
*   **Create** Firewall Rules to control traffic.
*   **Differentiate** between Internal vs External IP.

---

## 🧠 1. What Is a VPC? (Plain-English)

**VPC (Virtual Private Cloud)** is your own private network inside Google Cloud.
It isolates your resources from other customers.

Think of it as your virtual data center.

### Core Components:
1.  **VPC Network:** The global shell.
2.  **Subnets:** Regional slices of the network (e.g., `10.0.1.0/24` in `us-east1`).
3.  **Firewall Rules:** The security guards allowing/blocking traffic.
4.  **Routes:** The maps telling traffic where to go.

---

## 🏠 2. Real-World Analogy: Home Wi-Fi

*   **VPC** = Your entire **Home Network**.
*   **Subnet** = A specific **Room** (Kitchen, Garage). 
    *   *Note: In GCP, subnets are Regions, not rooms.*
*   **Firewall** = The **Front Door Security**. 
    *   Who can come in? (Ingress).
    *   Who can go out? (Egress).

---

## 🛡️ 3. Firewall Rules (The Security Guard)

By default, **ALL Incoming (Ingress) traffic is BLOCKED.**
You must explicitly allow traffic.

### Common Ports to Know:
*   **Port 80 (HTTP):** Standard Web Traffic (Unsecured).
*   **Port 443 (HTTPS):** Secure Web Traffic.
*   **Port 22 (SSH):** Remote access to Linux servers.
*   **Port 3389 (RDP):** Remote access to Windows servers.

> **🎯 ACE Tip:** To secure SSH, never allow `0.0.0.0/0` (everyone). Restrict it to your specific IP or use **IAP (Identity-Aware Proxy)**.

---

## 🛠️ 4. Hands-On Lab: Create a VPC & Firewall

**🧪 Lab Objective:** Build a custom network and open it for web traffic.

### ✅ Steps

1.  **Open Console:** Go to **VPC Network**.
2.  **Create:** Click **Create VPC Network**.
3.  **Name:** `my-custom-vpc`.
4.  **Subnets:** Choose **Custom**.
    *   Name: `us-subnet`
    *   Region: `us-central1`
    *   Range: `10.0.1.0/24`
5.  **Click Create.** (Wait a minute).
6.  **Add Firewall Rule:**
    *   Go to **Firewall** (left menu).
    *   Click **Create Firewall Rule**.
    *   Name: `allow-web`.
    *   Network: `my-custom-vpc`.
    *   Targets: `All instances in the network`.
    *   Source Filter: `IPv4 ranges` -> `0.0.0.0/0` (Anywhere).
    *   Protocols/Ports: Check `tcp` and type `80`.
7.  **Create:** Click Create.

Now any VM in this VPC can receive web traffic!

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **A VPC in Google Cloud is:**
    *   A. Regional
    *   B. **Global** ✅
    *   C. Zonal

2.  **A Subnet in Google Cloud is:**
    *   A. Global
    *   B. **Regional** ✅
    *   C. Zonal

3.  **By default, what is the behavior of Ingress (Incoming) traffic?**
    *   A. Allowed
    *   B. **Blocked** ✅
    *   C. Allowed only from Google

4.  **Which tag represents "The entire internet" in IP ranges?**
    *   A. 127.0.0.1
    *   B. **0.0.0.0/0** ✅
    *   C. 192.168.1.1

5.  **Which port do you need to open for a secure HTTPS web server?**
    *   A. 80
    *   B. 22
    *   C. **443** ✅

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand VPC is Global, Subnets are Regional.', checked: false },
        { text: 'I created a custom VPC.', checked: false },
        { text: 'I created a custom Subnet.', checked: false },
        { text: 'I created a Firewall Rule to allow Port 80.', checked: false }
    ]
}">
    <h3>
        <i class="fa-solid fa-list-check"></i>
        Day 5 Checklist
    </h3>
    <template x-for="(item, index) in items" :key="index">
        <div class="checklist-item" @click="item.checked = !item.checked">
            <div class="checklist-box" :class="{ 'checked': item.checked }">
                <i class="fa-solid fa-check text-white text-xs"></i>
            </div>
            <span x-text="item.text" :class="{ 'line-through text-slate-400': item.checked }"></span>
        </div>
    </template>
</div>
