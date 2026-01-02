# Day 9: Cloud Load Balancing

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 9, learners will be able to:
*   **Understand** why Load Balancing is necessary.
*   **Distinguish** between Global (HTTP) and Regional (Network) Load Balancers.
*   **Configure** a simple HTTP Load Balancer.

---

## 🧠 1. What Is Load Balancing?

If you have 1,000 users and only 1 Web Server, that server will crash.
If you have 2 Web Servers (MIG), how do you tell user A to go to Server 1, and user B to Server 2?

**Solution:** A **Load Balancer (LB)**.

It sits in front of your VMs and sits behind a single **Anycast IP**.

---

## 👮 2. Real-World Analogy: The Traffic Cop

*   **Users** = Cars.
*   **VMs** = Lanes on a highway.
*   **Load Balancer** = **The Traffic Cop**.
    *   He sees Lane 1 is stuck (High CPU).
    *   He waves cars into Lane 2 (Healthy).
    *   If Lane 3 is closed (Unhealthy VM), he puts cones up so no one goes there.

---

## 🏗️ 3. Types of Load Balancers (Cheat Sheet)

| Type | Layer | Global/Regional | Use Case |
| :--- | :--- | :--- | :--- |
| **External HTTP(S)** | Layer 7 (App) | **Global** | Websites, APIs, content serving. |
| **External TCP/UDP** | Layer 4 (Transport) | **Regional** | Gaming, Non-HTTP apps. |
| **Internal HTTP(S)** | Layer 7 (App) | Regional | Internal microservices. |

> **🎯 ACE Tip:**
> *   "Global application" or "Content Delivery" → **Global HTTP(S) LB**.
> *   "Non-HTTP traffic" or "Custom Protocol" → **TCP/UDP LB**.

---

## 🛠️ 4. Hands-On Lab: Set Up an HTTP LB

**🧪 Lab Objective:** Put a Load Balancer in front of yesterday's MIG.

### ✅ Steps

1.  **Prerequisite:** Ensure your MIG (Day 8 Lab) is running.
2.  **Open Console:** Go to **Network Services** > **Load Balancing**.
3.  **Start:** Click **Create Load Balancer**.
4.  **Type:** Choose **Application Load Balancer (HTTP/S)**.
5.  **Config:**
    *   **Frontend:** Leave default (Port 80). Global.
    *   **Backend:**
        *   Create a "Backend Service".
        *   Select your MIG (`my-web-cluster`).
        *   Port: 80.
        *   Health Check: Create one (Protocol TCP, Port 80).
    *   **Routing Rules:** Host and Path = Simple (Default).
6.  **Create:** Click Create. **Wait 5-10 minutes!** (Global propagation is slow).
7.  **Test:** Copy the Frontend IP. Open it in browser.
    *   You are now hitting the LB, which routes you to one of your Clones!

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Which Load Balancer is Global and operates at Layer 7?**
    *   A. Network TCP LB
    *   B. **External HTTP(S) LB** ✅
    *   C. Internal UDP LB

2.  **What does a "Health Check" do?**
    *   A. Scans for viruses.
    *   B. **Checks if a backend VM is responsive. If not, the LB stops sending traffic to it.** ✅
    *   C. Checks the user's browser health.

3.  **You want to serve traffic from a single IP address to users in Asia, Europe, and US. Which solution works best?**
    *   A. DNS Load Balancing
    *   B. **Global HTTP Load Balancer (Anycast IP)** ✅
    *   C. VPN

4.  **Can a Load Balancer distribute traffic to instances in different regions?**
    *   A. **Yes (Global LBs only)** ✅
    *   B. No, strictly regional.

5.  **Layer 4 Load Balancing handles:**
    *   A. URL paths (/images, /video)
    *   B. **TCP/UDP Traffic (IP and Ports)** ✅
    *   C. Cookies

---

## ✅ Day 9 Checklist

- [ ] I understand the difference between Layer 4 and Layer 7 LBs.
- [ ] I know which LB is Global.
- [ ] I created a Backend Service linked to a MIG.
- [ ] I accessed my app via the LB IP.
