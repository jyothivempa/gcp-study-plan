# SECTION 19: GKE Basics (Kubernetes)

> **Official Doc Reference**: [GKE Documentation](https://cloud.google.com/kubernetes-engine/docs)

## 1️⃣ Overview: The Orchestra
If Cloud Run is a "Food Truck", **GKE (Google Kubernetes Engine)** is a massive "Orchestra".
*   **Concept:** You have 1000 containers. You need them to talk to each other, restart if they crash, and scale across 50 VMs.
*   **Kubernetes (K8s):** The open-source system (invented by Google) to manage this.
*   **GKE:** Google's managed version. "The best place to run K8s".

## 2️⃣ Architecture Diagram (Exam Critical 🚨)
You must understand the difference between **Control Plane** and **Node**.

```mermaid
graph TD
    subgraph "Google Managed (Hidden)"
        CP[Control Plane / Master]
        API[API Server]
        Sch[Scheduler]
        CP --> API
        CP --> Sch
    end
    
    subgraph "Your Project (Visible)"
        Node1[Worker Node (VM)]
        Node2[Worker Node (VM)]
        
        subgraph "Inside Node 1"
            Pod1[Pod A]
            Pod2[Pod B]
        end
    end
    
    API --"Commands"--> Node1
    API --"Commands"--> Node2
    
    style CP fill:#e0f2fe,stroke:#0284c7
    style Node1 fill:#dcfce7,stroke:#15803d
    style Pod1 fill:#fee2e2,stroke:#991b1b
```
*   **Control Plane:** The Brain. Google manages it. (Zero ops for you).
*   **Node:** The Muscle. Standard Compute Engine VMs that run your pods.
*   **Pod:** The Atom. The smallest unit. Usually contains 1 container (e.g., your App).

## 3️⃣ Modes: Standard vs Autopilot 🚗
*   **Standard:** You manage the Nodes (VMs). You choose "e2-medium". You patch the OS.
*   **Autopilot:** Google manages the Nodes. You just say "Here is a Pod". You pay per Pod resource (CPU/RAM). **Best for most users.**

## 4️⃣ Zero-to-Hero: Service Types ⚡
How do people talk to your Pods?
1.  **ClusterIP:** Internal Only. (Database).
2.  **NodePort:** Open a port on the VM IP. (Messy. Avoid).
3.  **LoadBalancer:** Creates a **Google Cloud Load Balancer** with a Public IP. (Production Standard).

## 5️⃣ Hands-On Lab: Create a Cluster 🛠️
1.  **Create Cluster:**
    ```bash
    gcloud container clusters create-auto my-cluster --region=us-central1
    ```
2.  **Get Credentials (Login):**
    ```bash
    gcloud container clusters get-credentials my-cluster --region=us-central1
    ```
3.  **Run Nginx:**
    ```bash
    kubectl create deployment nginx --image=nginx
    ```
4.  **Expose to Internet:**
    ```bash
    kubectl expose deployment nginx --port=80 --type=LoadBalancer
    ```

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I need to install a custom GPU driver on the Node."
    *   *Answer:* You must use **GKE Standard**. Autopilot locks down the Node OS for security.
*   **Trap:** "What is the smallest deployable unit in K8s?"
    *   *Answer:* A **Pod**. NOT a container. (A pod *wraps* a container).
*   **Trap:** "How do I ensure High Availability?"
    *   *Answer:* Use a **Regional Cluster** (Control Plane replicated across 3 zones) instead of a Zonal Cluster.

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. In GKE Autopilot, who manages the Worker Nodes (Operating System upgrades)?**
*   A. You.
*   B. Google.
*   C. The Linux Foundation.
*   D. No one (they are immutable).
> **Answer: B.** Autopilot offloads node management to Google.

**Q2. Which command is used to interact with a running cluster?**
*   A. `gcloud run`
*   B. `terraform`
*   C. `kubectl`
*   D. `docker`
> **Answer: C.** `kubectl` (Kube-Control) is the universal tool for K8s.

**Q3. If a Pod crashes, who restarts it?**
*   A. You must SSH in and restart it.
*   B. The Load Balancer.
*   C. The Kubelet (Agent on the Node).
*   D. Cloud Functions.
> **Answer: C.** The Kubelet on the node watches the pod status and restarts it automatically.
