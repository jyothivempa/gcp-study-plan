# SECTION 17: App Engine (PaaS)

> **Official Doc Reference**: [App Engine Documentation](https://cloud.google.com/appengine/docs)

## 1️⃣ Overview: The "Serviced Apartment"
*   **Concept:** You bring the Code (Suitcase). Google manages the OS, Hardware, Networking, and Scaling (The Building).
*   **History:** Google's first product (2008).
*   **Key Feature:** Deploy by typing `gcloud app deploy`.

## 2️⃣ Standard vs Flexible (The Exam Gold 🥇)

| Feature | **App Engine Standard** | **App Engine Flexible** |
| :--- | :--- | :--- |
| **Startup Speed** | Milliseconds (Instant Scale). | Minutes (VM Boot time). |
| **Price** | Free Tier available. Pays for idle if min-instances > 0. | No Free Tier. Expensive (Always running VMs). |
| **Runtimes** | Restricted (Python, Java, Go, Node, PHP). | Any Docker Container (Custom Runtimes). |
| **OS Access** | Sandbox (No SSH, No Background writing). | Full SSH access. Background threads allowed. |
| **Use Case** | Sudden traffic spikes (Websites). | Consistent logic, VPN requirements, Custom Libraries. |

## 3️⃣ Scaling Logic (Visualized)

```mermaid
graph LR
    Traffic[User Request] --> LoadBalancer[App Engine LB]
    LoadBalancer --> S1[Instance 1 (Busy)]
    LoadBalancer --> S2[Instance 2 (Busy)]
    LoadBalancer --"Slope > Target"--> S3[Instance 3 (Spinning Up)]
    
    style S3 fill:#fef3c7,stroke:#d97706
```
*   **The Magic:** You set `target_cpu_utilization: 0.6`. If CPU hits 60%, Google creates Instance 3 automatically.

## 4️⃣ Hands-On Lab: Deploy a Hello World 🌍
1.  **Write Code (`main.py`):**
    ```python
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return 'Hello World!'
    ```
2.  **Write Config (`app.yaml`):**
    ```yaml
    runtime: python39
    ```
3.  **Deploy:**
    ```bash
    gcloud app deploy
    ```
4.  **View:**
    ```bash
    gcloud app browse
    ```

## 5️⃣ Traffic Splitting (Canary Deployments) 🐤
Safely release V2 without breaking V1.
*   **Command:** `gcloud app services set-traffic default --splits=v1=.9,v2=.1`
*   **Result:** 90% of users see Old Site. 10% see New Site.
*   *Exam Tip:* Traffic splitting can be by **IP Address** (Sticky) or **Cookie** (Session).

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I need to run a legacy binary that requires C++ libraries on App Engine."
    *   *Answer:* Use **App Engine Flexible**. Standard environment is sandboxed and does not allow custom system binaries.
*   **Trap:** "I want to install a VPN software on the server."
    *   *Answer:* **App Engine Flexible** (or Compute Engine). Standard cannot access OS network stack.
*   **Trap:** "I want to scale to zero to save money."
    *   *Answer:* **App Engine Standard**. (Flexible requires at least 1 VM running).

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. Which App Engine environment scales to zero?**
*   A. Standard
*   B. Flexible
*   C. Both
*   D. Neither
> **Answer: A.** Standard scales to 0. Flexible runs on VMs, so minimum is 1.

**Q2. You want to test a new version of your app on 1% of users. What feature do you use?**
*   A. Cloud CDN
*   B. Traffic Splitting
*   C. Cloud Armor
*   D. VPC Flow Logs
> **Answer: B.** App Engine's built-in Traffic Splitting.

**Q3. How do you define the runtime version (e.g., Python 3.9) for your app?**
*   A. In the `main.py` file.
*   B. In the `app.yaml` file.
*   C. In the Google Cloud Console settings.
*   D. It is automatic.
> **Answer: B.** The `app.yaml` file is the configuration source of truth.
