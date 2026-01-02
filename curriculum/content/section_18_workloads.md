# Day 18: Workloads (Pods & Deployments)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical

---

## 🎯 Learning Objectives

By the end of Day 18, learners will be able to:
*   **Define** a Pod.
*   **Explain** why we use Deployments instead of naked Pods.
*   **Deploy** an Nginx server to GKE.

---

## 🧠 1. The Pod (The Atom)

In Docker, the unit is a "Container".
In Kubernetes, the unit is a **Pod**.

*   A Pod is a wrapper around 1 (or more) containers.
*   "Shared Fate": Containers in a Pod share the same IP and Storage.

---

## 👬 2. Real-World Analogy: Peas in a Pod

*   **Docker Container** = **A Pea**.
*   **Kubernetes Pod** = **The Pod (Green shell)**.
    *   Ideally, you put 1 pea in 1 pod.
    *   Sometimes, if two peas are best friends (App + Log Agent), you put 2 peas in 1 pod.
    *   **Kubernetes only moves the Pod.** It doesn't touch the peas directly.

---

## 🚀 3. Deployments (The Manager)

You rarely run a Pod directly. Why? If it dies, it stays dead.
Instead, you create a **Deployment**.

*   **Deployment:** "I want 3 replicas of Nginx."
*   It creates a **ReplicaSet**, which ensures 3 Pods are *always* running.
*   If a Node crashes, the Deployment makes new Pods on another node.

> **Hierarchy:** Deployment -> ReplicaSet -> Pod -> Container.

---

## 🛠️ 4. Hands-On Lab: Deploy Nginx

**🧪 Lab Objective:** Run a web server on your cluster.

### ✅ Steps

1.  **Connect** to your cluster (Standard or Autopilot).
2.  **Create Deployment:**
    ```bash
    kubectl create deployment my-web --image=nginx:latest --replicas=3
    ```
3.  **Verify:**
    ```bash
    kubectl get pods
    ```
    *   *Result:* You should see 3 pods named `my-web-xxxx` Running.
4.  **Test Self-Healing:**
    *   Delete one pod: `kubectl delete pod [POD_NAME]`
    *   Quickly run `kubectl get pods`.
    *   *Result:* A new pod is instantly starting (Age: 2s). The Deployment replaced it!

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **What is the smallest deployable unit in Kubernetes?**
    *   A. Container
    *   B. **Pod** ✅
    *   C. Deployment

2.  **Why use a Deployment instead of a Pod?**
    *   A. Deployments are faster.
    *   B. **Deployments provide self-healing and scaling (via ReplicaSets).** ✅
    *   C. Pods are deprecated.

3.  **If you have a multi-container Pod, what do they share?**
    *   A. Nothing.
    *   B. **Network IP and localhost.** ✅
    *   C. CPU quota only.

4.  **You want to run exactly 5 copies of your app. What do you configure?**
    *   A. **replicas: 5** in the Deployment. ✅
    *   B. Run `docker run` 5 times.
    *   C. Use 5 Clusters.

5.  **Which object ensures a specified number of healthy pods are running?**
    *   A. Scheduler
    *   B. **ReplicaSet** (Managed by Deployment) ✅
    *   C. Kubelet

---

## ✅ Day 18 Checklist

- [ ] I describe the relationship: Deployment > ReplicaSet > Pod.
- [ ] I ran `kubectl create deployment`.
- [ ] I saw the self-healing in action.
