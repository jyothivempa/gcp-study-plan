# Day 16: GKE Architecture (Control Plane & Nodes)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 16, you will be able to:
*   **Visualize** the Kubernetes Control Plane and Worker Node interaction.
*   **Explain** the "Shared Responsibility" model in Google Kubernetes Engine.
*   **Identify** key components like the API Server, Scheduler, and Kubelet.
*   **Navigate** the logical boundary between Google-managed and customer-managed resources.

---

## 🏢 Industry Context: GKE in Production

> [!NOTE]
> **Role Lens:** GKE knowledge is essential for DevOps, Platform Engineering, and SRE roles. This is where companies run production workloads.

### Job Roles & GKE Usage

| Role | How They Use GKE | Day-to-Day Tasks |
|------|-----------------|------------------|
| **Platform Engineer** | Design cluster architecture | Node pools, Workload Identity, policies |
| **DevOps Engineer** | Deploy and scale applications | Deployments, Services, CI/CD integration |
| **SRE** | Maintain cluster reliability | Monitoring, autoscaling, troubleshooting |
| **Security Engineer** | Harden cluster security | RBAC, network policies, Pod Security |

### Autopilot vs Standard Decision

| Factor | Autopilot | Standard |
|--------|-----------|----------|
| **Node Management** | Google | You |
| **Per-Pod Billing** | Yes | No (per-node) |
| **Customization** | Limited | Full control |
| **Best For** | Teams without K8s expertise | Advanced teams needing control |

> [!TIP]
> **Interview Tip:** "When asked GKE mode, I say: Autopilot for teams that want to focus on apps, Standard for teams needing custom node configs or special hardware like GPUs."

### ❌ Interview Mistakes to Avoid

| Mistake | Why It's Bad | What to Say Instead |
|---------|--------------|---------------------|
| "I always use Standard mode" | Shows no cost awareness | "I evaluate Autopilot vs Standard based on team needs" |
| "I manually scale node pools" | Doesn't leverage auto-scaling | "I configure cluster autoscaler with min/max nodes" |
| "I don't know what Kubelet does" | Basic K8s knowledge gap | "Kubelet is the node agent that ensures containers run in pods" |

---

## 🧠 1. The Kubernetes "Command & Control" Center

A GKE cluster consists of two distinct pools of responsibility: the **Control Plane** (The Brain) and the **Nodes** (The Muscle).

### Architectural Blueprint

```mermaid
graph LR
    subgraph "Google-Managed Project"
        CP[Control Plane]
        API[API Server] --> ETCD[(etcd)]
        API --> SCH[Scheduler]
        API --> CM[Controller Manager]
    end

    subgraph "Your Project (VPC)"
        NP_STD[Node Pool: Standard]
        NP_SPOT[Node Pool: Spot/Preemptible]
        
        Node1[Worker Node 1]
        Node2[Worker Node 2]
        
        subgraph "Node Detail"
            KLT[Kubelet]
            KPRX[Kube-Proxy]
            CRI[Container Runtime]
            POD1[Pod A]
            POD2[Pod B]
        end
    end

    API <-.-> KLT
    API <-.-> KPRX
    NP_STD --> Node1
    NP_SPOT --> Node2
```

| Component | Responsibility | ACE Exam Note |
| :--- | :--- | :--- |
| **API Server** | Cluster "Front Door" | All `kubectl` commands talk to this. |
| **etcd** | Cluster State DB | Stores configuration. **Never** accessible to you in GKE. |
| **Scheduler** | Workload Placement | Decides which Node has enough RAM/CPU for a Pod. |
| **Kubelet** | Node Resident Agent | Reports Node health back to the API Server. |
| **Kube-Proxy** | Networking | Manages IP tables/rules for Service connectivity. |

---

---

## 🌊 3. Node Pools: Organizing the Muscle
In GKE, you don't just add single nodes; you manage **Node Pools**. A pool is a group of nodes with identical configuration.

| Pool Type | Ideal For | ACE Exam Key |
|-----------|-----------|--------------|
| **Standard** | Regular workloads | "High availability", "Reliable" |
| **Spot / Preemptible** | Batch processing, Testing | "Extreme cost savings (up to 80%)", "Fault tolerant workloads" |
| **Custom / GPU** | ML / Video Rendering | "Compute Intensive" |

> [!CAUTION]
> **Spot Nodes** can be reclaimed by Google at any time with 30 seconds' notice. Never use them for non-distributed databases or stateful apps without a clear strategy.

---

## ⌨️ 4. Kubectl Mastery: The CLI Cheatsheet
The ACE exam expects you to know basic troubleshooting commands.

| Command | Purpose | When to use? |
|---------|---------|--------------|
| `kubectl get pods` | List all pods | Checking status (Running, Pending, Error). |
| `kubectl describe pod [NAME]` | Detailed view of a pod | Finding WHY a pod failed (Logs/Events). |
| `kubectl logs [NAME]` | View app stdout | Debugging code errors inside the container. |
| `kubectl exec -it [NAME] -- bash` | Open shell inside pod | Manual debugging or DB connectivity tests. |
| `kubectl get nodes` | List worker nodes | Checking for "Ready" status. |

---

## 🛠️ 3. Hands-On Lab: Peeking Under the Hood

Even though the Control Plane is managed, we can see its effects through `kubectl`.

### 🧪 Lab Objective
Inspect the default system components and understand where they live.

### ✅ Steps

1.  **Get Credentials**:
    ```bash
    gcloud container clusters get-credentials [CLUSTER_NAME] --zone [ZONE]
    ```

2.  **List System Workloads**:
    ```bash
    # We use -n kube-system to see the internal components
    kubectl get pods -n kube-system
    ```
    > [!NOTE]
    > Notice you see `kube-proxy` and `fluentbit` (logging), but you **cannot** see the API Server or etcd. That's because they run in a hidden Google-managed project!

3.  **Inspect a Node**:
    ```bash
    kubectl describe node [NODE_NAME]
    ```
    *Look for the "Conditions" section. This is what the **Kubelet** reports back to the brain.*

---

## ⚠️ 4. Exam Traps & Best Practices

> [!WARNING]
> **etcd Access**: A common exam trap asks how to backup the etcd database in GKE. **The answer is: You don't.** Google manages all etcd backups and high availability automatically.

> [!TIP]
> **Version Management**: GKE allows you to choose "Release Channels" (Rapid, Regular, Stable). For production, **Stable** is the recommended choice for maximum reliability.

---

<!-- QUIZ_START -->
## 📝 5. Knowledge Check

1.  **Which component is responsible for deciding which node a new Pod should run on?**
    *   A. Kubelet
    *   B. API Server
    *   C. **Scheduler** ✅
    *   D. etcd

2.  **In GKE, where is the Control Plane located?**
    *   A. On the first worker node in your VPC.
    *   B. **In a separate Google-managed project.** ✅
    *   C. In a Cloud Storage bucket.
    *   D. It runs as a container on every node.

3.  **What is the role of the Kubelet?**
    *   A. It acts as the load balancer for incoming traffic.
    *   B. It stores the state of the cluster.
    *   C. **It is the agent that runs on each node and ensures containers are running in a Pod.** ✅
    *   D. It schedules new workloads based on resource availability.

4.  **Why can't you see the etcd pods when running `kubectl get pods -n kube-system`?**
    *   A. They are hidden for security reasons.
    *   B. You don't have the "Owner" role.
    *   C. **They run on the master nodes, which are managed by Google and not visible in your node list.** ✅
    *   D. etcd is not used in GKE.

5.  **Which GKE release channel is recommended for production workloads?**
    *   A. Rapid
    *   B. Regular
    *   C. **Stable** ✅
    *   D. Extended
<!-- QUIZ_END -->
---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand the difference between Control Plane and Worker Nodes.', checked: false },
        { text: 'I know that I do not manage etcd in GKE.', checked: false },
        { text: 'I can identify the API Server as the entry point for kubectl.', checked: false },
        { text: 'I understand the shared responsibility model.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 16 Mastery Checklist
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
