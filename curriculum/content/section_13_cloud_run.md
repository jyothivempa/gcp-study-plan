# Day 13: Cloud Run (Serverless Containers)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical (The future of Google Cloud)

---

## 🎯 Learning Objectives

By the end of Day 13, learners will be able to:
*   **Explain** what "Serverless Container" means.
*   **Compare** Cloud Run vs App Engine.
*   **Deploy** a pre-built container image.

---

## 🧠 1. What Is Cloud Run?

**Cloud Run** is the modern sweet spot between App Engine (easy) and Kubernetes (powerful).

It runs **Stateless Containers**.
*   **Serverless:** No servers to manage. Scales to zero.
*   **Containerized:** You bring a Docker container. Google runs it.

**Why is it popular?** You can write code in ANY language, package it as a container, and Google runs it just like App Engine, but without the "Sandbox" restrictions.

---

## 🏪 2. Real-World Analogy: The Pop-Up Store

*   **App Engine:** Detailed Resort. You follow their rules (Dinner at 7 PM).
*   **Kubernetes (GKE):** Buying a Mall. You manage electricity, security, rent.
*   **Cloud Run:** A **Pop-Up Store**.
    *   You bring your own "Box" (Container) with your goods.
    *   Google gives you a spot on the street.
    *   If 100 customers come, Google instantly clones your box 100 times.
    *   If no customers come, your box disappears (Cost: $0).

---

## ⚔️ 3. Cloud Run vs App Engine (Exam Key)

| Feature | App Engine (Standard) | Cloud Run |
| :--- | :--- | :--- |
| **Unit of Deployment** | Source Code | **Container Image** |
| **Portability** | Hard (Google specific) | **Easy** (Run anywhere Docker runs) |
| **Scaling** | Fast | **Lightning Fast** (Concurrency) |
| **Recommendation** | Legacy Web Apps | **Modern Microservices** |

> **🎯 ACE Tip:** If the question mentions "Container", "Serverless", and "Portable" → **Cloud Run**.

---

## 🛠️ 4. Hands-On Lab: Deploy a Container

**🧪 Lab Objective:** Deploy a public sample container in 30 seconds.

### ✅ Steps

1.  **Open Console:** Go to **Cloud Run**.
2.  **Create:** Click **Create Service**.
3.  **Config:**
    *   **Container Image URL:** `us-docker.pkg.dev/cloudrun/container/hello` (Google's demo image).
    *   **Service Name:** `hello-run`.
    *   **Region:** `us-central1`.
4.  **Security (Important):**
    *   Select **"Allow unauthenticated invocations"**. (This makes it public).
5.  **Create:** Click Create.
6.  **Verify:** Wait 10 seconds. Click the generated URL.
    *   Boom! You have a global, auto-scaling website running SSL.

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **What is the deployment unit for Cloud Run?**
    *   A. ZIP file of code
    *   B. **Container Image** ✅
    *   C. VM Image

2.  **Can Cloud Run scale to zero?**
    *   A. **Yes** ✅
    *   B. No, min 1 instance.

3.  **What does "Stateless" mean?**
    *   A. The app has no memory.
    *   B. **The app doesn't save local data between requests (Files are lost on restart).** ✅
    *   C. The app runs in US states.

4.  **You have a Docker container that listens on Port 8080. You want to run it without managing nodes. Which service?**
    *   A. GKE (Kubernetes) - (Requires managing cluster)
    *   B. Compute Engine
    *   C. **Cloud Run** ✅

5.  **Cloud Run is built on which open-source standard?**
    *   A. Docker Swarm
    *   B. **Knative** ✅
    *   C. Terraform

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I know what Serverless means.', checked: false },
        { text: 'I understand why Containers are portable.', checked: false },
        { text: 'I deployed the hello container on Cloud Run.', checked: false },
        { text: 'I accessed the public URL.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 13 Checklist
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
