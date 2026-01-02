# Day 19: Services & Networking

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 19, learners will be able to:
*   **Explain** why Pod IPs are unreliable.
*   **Compare** ClusterIP, NodePort, and LoadBalancer.
*   **Expose** an application to the internet.

---

## 🧠 1. The Problem: Ephemeral IPs

Pods are mortal. They die and get replaced (Day 18 Lab).
Every time a Pod restarts, it gets a **new IP address**.
*How can your Frontend talk to your Backend if the Backend's IP keeps changing?*

**Solution:** A **Service**.
A Service provides a **stable** IP and DNS name that never changes. It load balances traffic to the pods behind it.

---

## 🛎️ 2. Real-World Analogy: The Reception Desk

*   **Pods** = **Doctors** in a hospital. They move rooms, change shifts.
*   **Service** = **The Reception Desk**.
    *   Patient calls: "I need a doctor." (Hits Service IP).
    *   Receptionist connects them to *any* available doctor.
    *   Patient doesn't need to know the Doctor's personal cell phone number.

---

## 🔌 3. Service Types (Cheat Sheet)

| Type | Visibility | Use Case |
| :--- | :--- | :--- |
| **ClusterIP** (Default) | **Internal Only** | Frontend talking to Backend DB. |
| **NodePort** | External (Basic) | Opens a port (30000+) on every Node. (Rarely used in prod). |
| **LoadBalancer** | **External (Prod)** | Provisions a real GCP Cloud Load Balancer. |

> **Ingress:** Not a service. It's a "Smart Router" (HTTP/S) that sits in front of a Service to handle paths (/api, /web).

---

## 🛠️ 4. Hands-On Lab: Expose Your App

**🧪 Lab Objective:** Make your Nginx Deployment accessible from the internet.

### ✅ Steps

1.  **Prerequisite:** Ensure `my-web` deployment is running.
2.  **Expose Deployment:**
    ```bash
    kubectl expose deployment my-web --type=LoadBalancer --port 80 --target-port 80
    ```
    *   *Translation:* "Create a Service connecting external Port 80 to container Port 80."
3.  **Get External IP:**
    ```bash
    kubectl get services
    ```
    *   *Wait* for `EXTERNAL-IP` to change from `<pending>` to a real IP (e.g., `34.x.x.x`). (Takes 1 min).
4.  **Test:** Click the IP. You see "Welcome to nginx!".

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Why can't you rely on Pod IP addresses?**
    *   A. They are IPv6.
    *   B. **They change every time a Pod restarts.** ✅
    *   C. They are encrypted.

2.  **Which Service type opens your app to the public Internet using a GCP Load Balancer?**
    *   A. ClusterIP
    *   B. **LoadBalancer** ✅
    *   C. Headless

3.  **Which Service type is the default and only allows internal access?**
    *   A. **ClusterIP** ✅
    *   B. NodePort
    *   C. ExternalName

4.  **What object helps you route HTTP traffic based on path (e.g. example.com/blog)?**
    *   A. Service
    *   B. **Ingress** ✅
    *   C. ReplicaSet

5.  **A Service sends traffic to a set of Pods. How does it know which Pods to pick?**
    *   A. It guesses.
    *   B. **Labels and Selectors (e.g., app=my-web).** ✅
    *   C. It picks all pods.

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I describe why we need a Stable IP.', checked: false },
        { text: 'I exposed a deployment using Type=LoadBalancer.', checked: false },
        { text: 'I accessed Nginx from my browser.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 19 Checklist
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
