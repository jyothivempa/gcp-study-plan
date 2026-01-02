# Day 17: GKE Modes (Standard vs Autopilot)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 17, learners will be able to:
*   **Compare** GKE Standard vs GKE Autopilot.
*   **Decide** which mode to use for a given scenario.
*   **Create** an Autopilot cluster.

---

## 🧠 1. The Two Modes of GKE

Google Kubernetes Engine (GKE) comes in two flavors.

### 1. GKE Standard (Classic)
*   **You manage the Nodes.**
*   You choose the Machine Type (e.g., `e2-medium`).
*   You pay for the Nodes (even if empty).
*   **Best for:** Custom hardware needs (GPUs), fine-grained control.

### 2. GKE Autopilot (Modern)
*   **Google manages the Nodes.**
*   You don't see "Nodes". You just ask for CPU/RAM.
*   You pay only for the Pods (usage).
*   **Best for:** Most production apps, lowering ops overhead, security by default.

---

## ✈️ 2. Real-World Analogy: Manual vs Auto Pilot

*   **GKE Standard** = **Manual Transmission Car**.
    *   You control the gears (Nodes).
    *   Fun for race car drivers (Experts).
    *   Possibility of stalling or burning the clutch if unskilled.
*   **GKE Autopilot** = **Self-Driving Taxi**.
    *   You just say "Go to Airport" (Deploy App).
    *   The car handles the steering, gas, and gears.
    *   You pay for the ride, not the engine.

---

## ⚔️ 3. Comparison Cheat Sheet

| Feature | Standard | Autopilot |
| :--- | :--- | :--- |
| **Node Management** | You | Google |
| **Pricing** | Per Node | Per Pod (CPU/RAM request) |
| **Security** | Configurable | Locking down (Best Practices enforced) |
| **SLA** | Good | **Financial SLA on Pods** |

> **🎯 ACE Tip:** 
> *   "Minimize operational overhead" or "Production Ready by default" → **Autopilot**.
> *   "Specific machine family" or "cheap spot instances" → **Standard**.

---

## 🛠️ 4. Hands-On Lab: Create Autopilot Cluster

**🧪 Lab Objective:** Spin up an Autopilot cluster.

### ✅ Steps

1.  **Open Console:** Go to **Kubernetes Engine > Clusters**.
2.  **Create:** Click **Create**.
3.  **Choose:** Select **Autopilot** (Click Configure).
4.  **Settings:**
    *   Name: `auto-cluster-1`.
    *   Region: `us-central1`.
5.  **Create:** Click Create. (Takes ~5-7 mins).
6.  **Verify:**
    *   Once green, connect via Cloud Shell.
    *   Run `kubectl get nodes`.
    *   *Notice:* You can see nodes, but you can't edit them. They are managed.

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **In GKE Standard, who is responsible for upgrading the Node OS?**
    *   A. Google (Auto-upgrade enabled by default, but you configure it).
    *   B. **You (Ultimately responsible for configuration).** ✅
    *   C. Microsoft.

2.  **In GKE Autopilot, what do you pay for?**
    *   A. The number of nodes.
    *   B. **The CPU and Memory requested by your Pods.** ✅
    *   C. A flat monthly fee.

3.  **Which mode enforces security best practices by denying root access to nodes?**
    *   A. Standard
    *   B. **Autopilot** ✅
    *   C. Neither

4.  **You want to install a custom driver on the Node OS. Which mode MUST you use?**
    *   A. Autopilot
    *   B. **Standard** (Autopilot locks down the OS) ✅

5.  **For a team with limited Kubernetes experience wanting a production cluster, which is recommended?**
    *   A. **Autopilot** ✅
    *   B. Standard

---

## ✅ Day 17 Checklist

- [ ] I know the difference between paying for *Nodes* vs *Pods*.
- [ ] I understand why Autopilot is "Secure by Default".
- [ ] I launched a GKE Autopilot cluster.
