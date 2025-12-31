import os
import django
import sys
import textwrap

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def update_day22_gke():
    # Target Day 22
    try:
        day = Day.objects.get(number=22)
    except Day.DoesNotExist:
        print("Error: Day 22 does not exist. Please run populate_content.py first to scaffold.")
        return

    # 1. Define Visual Content (Concept)
    concept_content = """
### 1️⃣ Plain-English Explanation
**Kubernetes (K8s)** is like a massive robotic crane system for your shipping containers (Docker apps).
*   **Docker**: Puts your app in a standardized box.
*   **Kubernetes**: Moves duplications of that box around ships (Servers), ensuring they don't fall off.
*   **GKE**: Google manages the crane for you. You just tell it "I want 3 boxes of specific color", and it makes sure they exist.

### 2️⃣ Architecture: Control Plane vs Nodes
*   **Control Plane (The Captain)**:
    *   Managed by Google (hidden).
    *   Decides where to put pods, detects failures.
    *   *Cost*: Free for Zonal (single zone), Paid for Regional (HA).
*   **Nodes (The Workers)**:
    *   The actual VMs (Compute Engine) doing the heavy lifting.
    *   You pay for these (in Standard mode).

### 3️⃣ Modes of Operation (Crucial Exam Topic)
| Feature | **Autopilot** (Preferred) ✈️ | **Standard** 🛠️ |
| :--- | :--- | :--- |
| **Management** | Google manages Nodes | You manage Nodes |
| **Billing** | Pay per **Pod** (CPU/RAM) | Pay per **Node** (VM) |
| **Security** | Locked down (No SSH) | Full Access (SSH allowed) |
| **Best For** | Production, Efficiency | Legacy apps, GPUs, specific OS tweaks |

### 4️⃣ Kubernetes Objects Essentials
1.  **Pod**: The atom. Smallest unit. Usually 1 container. Ephemeral (dies easily).
2.  **Deployment**: The Manager. "Make sure 3 copies of Frontend are running." Handles updates.
3.  **Service**: The Networker. Gives a stable IP to a set of dynamic Pods.
    *   *ClusterIP*: Internal only.
    *   *LoadBalancer*: External access.

### 5️⃣ GKE Networking
*   **VPC Native**: Pods get real VPC IP addresses (high performance).
*   **Global LB**: You can put a Global HTTP(S) Load Balancer in front of GKE (Multi-cluster ingress).

### 9️⃣ One-Line Memory Hook 🧠
**GKE is the Conductor, your Containers are the Orchestra.**
"""

    # 2. Define Hands-on Content (Lab)
    hands_on_content = """
### 5️⃣ Console Walkthrough: Deploy Ngnix
**Goal**: Launch a web server on GKE Autopilot.

1.  **Create Cluster**:
    *   Go to **Kubernetes Engine** > **Clusters**.
    *   Click **Create**.
    *   Choose **Autopilot**. Name it `hello-cluster`.
    *   Region: `us-central1`.
    *   Click **Create** (Takes ~5 mins).

2.  **Connect via Shell**:
    *   Click the "Connect" button (3 dots) > **Run in Cloud Shell**.
    *   This sets up your `kubectl` context.

3.  **Deploy App**:
    ```bash
    # 1. Create Deployment (The Logic)
    kubectl create deployment nginx-web --image=nginx
    
    # 2. Expose to Internet (The Network)
    kubectl expose deployment nginx-web --type=LoadBalancer --port=80
    ```

4.  **Verify**:
    *   Run `kubectl get services`.
    *   Wait for `EXTERNAL-IP`.
    *   Click the IP. You see "Welcome to nginx!".

5.  **Cleanup**:
    *   Delete the cluster to avoid costs!
"""

    # 3. Update Day Model
    day.title = "Google Kubernetes Engine (GKE)"
    day.description = "Orchestrate containerized applications with K8s."
    day.concept_content = textwrap.dedent(concept_content).strip()
    day.hands_on_content = textwrap.dedent(hands_on_content).strip()
    day.outcome = "deployed a scalable containerized application on GKE."
    
    # Interview Questions
    day.interview_questions = """
### 8️⃣ Interview-Ready Q&A
**Q1: Why use Autopilot instead of Standard?**
*Answer:* Autopilot removes the overhead of managing worker nodes. It handles bin-packing, security patching, and scaling, reducing operational toil (OpEx).

**Q2: What happens if a Pod crashes?**
*Answer:* The Deployment controller notices the state mismatch (Desired: 3, Actual: 2) and spins up a new Pod immediately to replace it. This is "Self-Healing".

**Q3: Can GKE Pods talk to Cloud SQL?**
*Answer:* Yes, typically using the "Cloud SQL Proxy" sidecar container for secure authentication without managing IP whitelists.
"""
    day.save()
    print(f"Updated Day {day.number}: {day.title}")

    # 4. Update Quiz Questions
    # Clear existing
    QuizQuestion.objects.filter(day=day).delete()
    
    questions = [
        {
            'question_text': "In GKE Autopilot mode, what are you billed for?",
            'option_1': "The number of Master Nodes",
            'option_2': "The underlying VM instances (Nodes)",
            'option_3': "The CPU and Memory requested by your Pods",
            'option_4': "The number of namespaces",
            'correct_option': 3
        },
        {
            'question_text': "Which Kubernetes object creates a Stable IP address for a set of Pods?",
            'option_1': "Deployment",
            'option_2': "Service",
            'option_3': "Ingress",
            'option_4': "ReplicaSet",
            'correct_option': 2
        },
        {
            'question_text': "To survive a Zone failure (data center outage), which cluster type should you choose?",
            'option_1': "Zonal Cluster",
            'option_2': "Regional Cluster",
            'option_3': "Private Cluster",
            'option_4': "Autopilot Cluster",
            'correct_option': 2
        }
    ]

    for q in questions:
        QuizQuestion.objects.create(day=day, **q)
    
    print(f"Created {len(questions)} quiz questions for Day {day.number}")

if __name__ == "__main__":
    update_day22_gke()
