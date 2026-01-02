# Day 12: App Engine (PaaS)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐ Medium

---

## 🎯 Learning Objectives

By the end of Day 12, learners will be able to:
*   **Define** Platform as a Service (PaaS).
*   **Choose** between Standard Environment vs Flexible Environment.
*   **Deploy** a "Hello World" app without configuring a server.
*   **Understand** Traffic Splitting.

---

## 🧠 1. What Is App Engine?

**App Engine** is a fully managed platform (PaaS) for building web applications.
You just upload your code (Python, Java, Node.js, Go), and Google runs it.

**Zero Config:** You don't create VMs. You don't install OS updates. You don't set up Load Balancers. It's built-in.

---

## 🌴 2. Real-World Analogy: The All-Inclusive Resort

*   **Compute Engine (IaaS):** You rent an Airbnb. You have to cook, clean, and buy groceries.
*   **App Engine (PaaS):** You go to an **All-Inclusive Resort**.
    *   Food is ready. Room is cleaned. Pool is open.
    *   You just enjoy the holiday (**Write Code**).
    *   **Pro:** Easy!
    *   **Con:** You can't repaint the walls (Lees control over OS).

---

## ⚔️ 3. Standard vs Flexible (The Big Decision)

| Feature | Standard Environment | Flexible Environment |
| :--- | :--- | :--- |
| **Startup Time** | milliseconds (Instant) | Minutes (Uses VMs) |
| **Price** | Scales to Zero (Free if unused) | Always running (Min 1 instance) |
| **Languages** | Specific versions (Python 3.10, Node 18) | Any Language (Docker) |
| **OS Access** | Sandbox (No SSH) | SSH Allowed |

> **🎯 ACE Tip:** 
> *   "Scale to zero" or "Sudden traffic spikes" → **Standard**.
> *   "Custom Docker container" or "Background processes" → **Flexible**.

---

## 🚦 4. Traffic Splitting (Canary Deployments)

App Engine is famous for easy **Blue/Green** testing.
You can say: *"Send 90% of users to V1, and 10% to V2."*
This lets you test new features safely.

---

## 🛠️ 5. Hands-On Lab: Deploy a Python App

**🧪 Lab Objective:** Deploy a simple app using Cloud Shell.

### ✅ Steps

1.  **Open Cloud Shell:** Click the Terminal icon in top-right.
2.  **Create Folder:**
    ```bash
    mkdir my-app
    cd my-app
    ```
3.  **Create App File (`main.py`):**
    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello App Engine!'

    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8080, debug=True)
    ```
    *(You can use `nano main.py` to paste this).*
4.  **Create Config (`app.yaml`):**
    ```yaml
    runtime: python39
    ```
5.  **Deploy:**
    ```bash
    gcloud app deploy
    ```
6.  **Verify:** Select Region (e.g., `us-central1`). Wait ~2 mins.
7.  **View:** run `gcloud app browse`.

---

## 📝 6. Quick Knowledge Check (Quiz)

1.  **App Engine is an example of which service model?**
    *   A. IaaS
    *   B. **PaaS (Platform as a Service)** ✅
    *   C. SaaS

2.  **Which environment can scale to zero (costing nothing)?**
    *   A. **Standard** ✅
    *   B. Flexible
    *   C. Both

3.  **You need to install a custom 3rd-party library that requires C-level OS access. Which environment should you use?**
    *   A. Standard
    *   B. **Flexible** (It runs in a Docker container on a VM) ✅

4.  **What built-in feature allows you to test a new version on 1% of users?**
    *   A. A/B Tester
    *   B. **Traffic Splitting** ✅
    *   C. Load Balancer

5.  **With App Engine, do you need to configure a Firewall manually to allow HTTP?**
    *   A. Yes
    *   B. **No, the platform handles routing/firewalling for web traffic automatically.** ✅

---

## ✅ Day 12 Checklist

- [ ] I understand the PaaS model.
- [ ] I can differentiate Standard vs Flexible.
- [ ] I created `app.yaml`.
- [ ] I deployed an app via `gcloud app deploy`.
