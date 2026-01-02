# Day 21: Week 3 Review & Exam Strategy

**Level:** Review  
**Milestone:** 🏁 Week 3 Complete! (Kubernetes Mastered)

---

## 🔁 1. Week 3 Recap (Kubernetes)

GKE is the most "heavy" topic on the exam. You mastered the basics.

| Day | Topic | Key Takeaway |
| :--- | :--- | :--- |
| **15** | **Containers** | Dockerfile builds Images. Images run as Containers. (Lunchbox). |
| **16** | **Architecture** | Control Plane (Brain) vs Nodes (Muscle). GKE manages Brain. |
| **17** | **GKE Modes** | Standard (Manage Nodes) vs Autopilot (Google Manages Nodes). |
| **18** | **Workloads** | Deployment -> ReplicaSet -> Pod. Self-healing & Scaling. |
| **19** | **Networking** | ClusterIP (Internal), LoadBalancer (External). Ingress (Smart Router). |
| **20** | **Config** | ConfigMap (Plain) vs Secret (Sensitive). 12-Factor App. |

---

## 🧪 2. Week 3 Mock Exam (10 Questions)

### Question 1
**You want to minimize operational overhead. You do not need to install custom drivers on nodes. Which GKE mode should you use?**
*   A. GKE Standard
*   B. **GKE Autopilot** ✅
*   C. Compute Engine
*   D. Cloud Run

### Question 2
**Which Kubernetes object ensures that 3 copies of your application are always running, even if a Node crashes?**
*   A. Pod
*   B. Service
*   C. **Deployment** ✅
*   D. ConfigMap

### Question 3
**You need to expose an HTTP application to the public internet using a Google Cloud Load Balancer.**
*   A. **Create a Service of type LoadBalancer.** ✅
*   B. Create a Service of type ClusterIP.
*   C. Create a Deployment only.
*   D. Use SSH.

### Question 4
**Where should you store a private API Key?**
*   A. In the Dockerfile.
*   B. In a ConfigMap.
*   C. **In a Secret.** ✅
*   D. In the Pod name.

### Question 5
**What is the role of the Kubelet?**
*   A. It schedules pods.
*   B. It stores the cluster state.
*   C. **It runs on the Node and starts containers.** ✅
*   D. It serves the API.

### Question 6
**A Pod tries to talk to another Pod using its IP address, but the connection fails after a deployment update. Why?**
*   A. The IP address changed when the Pod was recreated.
*   B. **They should communicate via a Service (Stable IP/DNS), not Pod IP.** ✅
*   C. Both A and B.

### Question 7
**Which file defines how to build a container image?**
*   A. `deployment.yaml`
*   B. **`Dockerfile`** ✅
*   C. `service.yaml`
*   D. `main.py`

### Question 8
**You need to route incoming traffic to /video to one service and /web to another. What do you use?**
*   A. LoadBalancer Service
*   B. **Ingress** ✅
*   C. NodePort
*   D. NAT Gateway

### Question 9
**In GKE Standard, who is responsible for OS security patches on the Nodes?**
*   A. Google entirely.
*   B. **You (though Google provides Auto-Upgrade, you configure it).** ✅
*   C. No one.

### Question 10
**What is a "Stateless" application ideal for Kubernetes?**
*   A. An app that saves data to the local disk.
*   B. **An app that saves data to an external DB, so pods can be deleted anytime.** ✅
*   C. An app that cannot be restarted.

---

## 🏆 3. What's Next? Week 4!

Week 4 is **Security & Operations**.
*   **Logging & Monitoring:** Cloud Operations (Stackdriver).
*   **IAM Advanced:** Least Privilege.
*   **Billing:** Budgets & Alerts.

> **🎉 You survived Kubernetes Week! This is the hardest part.**

