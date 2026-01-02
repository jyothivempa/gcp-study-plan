# Day 16: Kubernetes Architecture

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 16, learners will be able to:
*   **Draw** the Kubernetes High-Level Architecture.
*   **Explain** the role of the Control Plane vs Nodes.
*   **Define** Kubelet and Kube-Proxy.

---

## 🧠 1. What Is Kubernetes (K8s)?

**Kubernetes** is an open-source platform for managing containerized workloads and services. Use it to deploy 10,000 containers across 500 machines as if they were one computer.

### The Two Main Parts:
1.  **Control Plane (The Master):** The brain. Makes decisions (Scheduling, Scaling).
2.  **Nodes (The Workers):** The muscle. Where your Apps actually run.

---

## 🚢 2. Real-World Analogy: The Ship Captain

*   **Kubernetes Cluster** = **A Cargo Ship**.
*   **Control Plane** = **The Captain (Bridge)**.
    *   The Captain decides: "Put Container X on the front deck." (Scheduling).
    *   He checks: "Is Container Y broken? Replace it." (Self-healing).
*   **Worker Nodes** = **The Deck Hands (Sailors)**.
    *   They don't think. They just carry the containers.
    *   If a Sailor gets sick (Node fails), the Captain moves the work to another Sailor.

---

## 🏗️ 3. Component Deep Dive

| Component | Location | Role |
| :--- | :--- | :--- |
| **API Server** | Control Plane | The "Front Door". Accepts commands (`kubectl`). |
| **Scheduler** | Control Plane | Decides *where* to put a new Pod. |
| **ETCD** | Control Plane | The Database. Stores the *state* of the cluster. |
| **Kubelet** | **Worker Node** | The Agent. Talks to the Captain. Starts containers. |
| **Pod** | Worker Node | Wrapper around a container. |

---

## 🛠️ 4. Hands-On Lab: View Cluster Info

**🧪 Lab Objective:** Inspect a cluster to see these components.

### ✅ Steps

1.  **Open Cloud Shell.**
2.  **Set Project:** `gcloud config set project [YOUR_PROJECT_ID]`
3.  **Create a tiny cluster (Takes 5 mins):**
    ```bash
    gcloud container clusters create test-cluster --num-nodes=1 --zone=us-central1-a
    ```
4.  **View Nodes:**
    ```bash
    kubectl get nodes
    ```
    *   *Result:* You see your "Sailor" (Worker Node).
5.  **View System Pods:**
    ```bash
    kubectl get pods -n kube-system
    ```
    *   *Result:* You see `kube-dns`, `kube-proxy` running. (Note: In GKE, you don't see the Control Plane pods because Google manages them for you!).

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Which component is the "Brain" of the cluster?**
    *   A. Worker Node
    *   B. **Control Plane** ✅
    *   C. Kubelet

2.  **Where do your application containers run?**
    *   A. Control Plane
    *   B. **Worker Nodes** ✅
    *   C. Within ETCD

3.  **In GKE, who manages the Control Plane?**
    *   A. You do.
    *   B. **Google (Fully Managed)** ✅
    *   C. Your ISP.

4.  **What acts as the "Database" for Kubernetes, storing the configuration?**
    *   A. Cloud SQL
    *   B. **etcd** ✅
    *   C. Redis

5.  **Which agent runs on every Worker Node to talk to the Control Plane?**
    *   A. Docker
    *   B. **Kubelet** ✅
    *   C. Scheduler

---

## ✅ Day 16 Checklist

- [ ] I can draw a line between Master and Worker.
- [ ] I know GKE manages the Master for me.
- [ ] I ran `kubectl get nodes`.
