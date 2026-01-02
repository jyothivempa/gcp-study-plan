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

## 🎯 2. Exam Focus Areas

### Critical Concepts for ACE Exam

#### GKE Modes: Standard vs Autopilot

| Feature | Standard | Autopilot |
| :--- | :--- | :--- |
| **Nodes** | You manage, upgrade, and pay for nodes. | Google manages nodes completely. |
| **Pricing** | Pay per **NODE** (even if empty). | Pay per **POD** (CPU/RAM requested). |
| **SSH Access** | Yes (You own the underlying VM). | No (Access is locked down). |
| **Best For** | Custom tweaks, special hardware (GPUs). | "Just run my pods", Ops-free. |

**Exam Tip:** "Maximize operational efficiency" or "Reduce management overhead" → **Autopilot**. "Need to install custom driver on node" → **Standard**.

#### Kubernetes Networking (The "Service" Types)

1.  **ClusterIP (Default):** Internal IP only. Pod-to-Pod communication.
2.  **NodePort:** Opens a specific port on every Worker Node IP. Good for testing, rare in Prod.
3.  **LoadBalancer:** Provisions a real GCP External Load Balancer. One IP per service. Expensive if you have 50 services.
4.  **Ingress:** Smart HTTP/S router. One IP for MANY services (`/api` -> Service A, `/web` -> Service B).

**Exam Tip:** "expose http application to internet" → **LoadBalancer** or **Ingress**. "Internal communication only" → **ClusterIP**.

#### Pod Lifecycle & Self-Healing
- **Deployment:** Manages ReplicaSets (updates, rollbacks).
- **ReplicaSet:** Ensures X number of pods are running.
- **Pod:** The actual running container(s).
- **If a Pod dies:** ReplicaSet recreates it.
- **If a Node dies (Standard):** MIG recreates the Node -> ReplicaSet reschedules the Pods.

#### ConfigMaps vs Secrets
- **ConfigMap:** Environment variables, config files (`.conf`). Stored in plain text.
- **Secret:** Passwords, API keys, certs. Stored base64 encoded (encrypted at rest in etcd).

---

## ⚠️ 3. Common Mistakes

### Mistake #1: Manually Creating Pods
**Wrong:** `kubectl run my-pod ...`  
**Right:** Always use a **Deployment**. Single pods don't self-heal if the node dies. Deployments do.

### Mistake #2: Forgetting to Enable APIs
- To use GKE, you MUST enable `container.googleapis.com`.
- Lab failure reason #1: API not enabled.

### Mistake #3: Confusing Ingress with LoadBalancer
- **LoadBalancer Service:** layer 4 (TCP). One IP per service.
- **Ingress:** Layer 7 (HTTP). One IP for the whole cluster (routing rules).

### Mistake #4: Stateful Apps in GKE
- By default, if a pod dies, its disk data is **LOST**.
- You MUST use persistent volumes (PV/PVC) or StatefulSets for databases.

---

## 🧪 4. Hands-On Review Lab

Deploy a stateless web app and expose it via a Load Balancer.

### Project: "Hello-GKE" Quick Deploy

**Steps:**

1.  **Create GKE Cluster (Autopilot)**
    ```bash
    gcloud container clusters create-auto my-cluster \
      --region us-central1
    ```
    *(Takes ~5 mins. Go grab coffee.)*

2.  **Get Credentials (Connect kubectl to cluster)**
    ```bash
    gcloud container clusters get-credentials my-cluster \
      --region us-central1
    ```

3.  **Deploy Application**
    ```bash
    kubectl create deployment hello-server \
      --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    ```

4.  **Expose to Internet**
    ```bash
    kubectl expose deployment hello-server \
      --type=LoadBalancer \
      --port 80
    ```

5.  **Get External IP**
    ```bash
    kubectl get service hello-server --watch
    ```
    *Wait until `EXTERNAL-IP` changes from `<pending>` to a real IP.*

6.  **Test & Clean Up**
    - Visit IP in browser.
    - Delete:
      ```bash
      gcloud container clusters delete my-cluster --region us-central1
      ```

**What You Practiced:**
- ✅ Creating an Autopilot cluster
- ✅ Using `kubectl` to deploy apps
- ✅ Exposing apps via GCP Load Balancer

---

## 📚 5. Study Tips for Week 4

- **Week 4 is Ops & Security.** Less coding, more configuring.
- **Logging:** Understand the difference between Logging (text) and Monitoring (metrics/graphs).
- **IAM:** We go deeper than Week 1. Conditional IAM and Service Accounts.

---

## 🏆 6. What's Next? Week 4!

Week 4 is **Security & Operations**.

*   **Cloud Operations:** Monitoring, Logging, Trace, Profiler (the "Stackdriver" suite).
*   **Advanced IAM:** Conditions, Workload Identity.
*   **Data Warehousing:** BigQuery basics.
*   **Event Driven:** Cloud Functions & Eventarc.

> **🎉 You survived Kubernetes Week! This is the hardest part.**
