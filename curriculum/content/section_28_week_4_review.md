# Day 28: Week 4 Review & Exam Strategy

**Level:** Review  
**Milestone:** 🏁 Week 4 Complete! (Ops & Security)

---

## 🔁 1. Week 4 Recap (Day 2 Ops)

You now know how to run, secure, and pay for the cloud.

| Day | Topic | Key Takeaway |
| :--- | :--- | :--- |
| **22** | **Ops** | Metrics (Speedometer) vs Logs (Black Box) vs Alerts. Ops Agent needed for Memory. |
| **23** | **Functions** | Event-driven (Pub/Sub triggers). Great for glue code. |
| **24** | **NetSec** | Firewall Rules (Priority). IAP = SSH without Public IP. |
| **25** | **Armor/DLP** | Cloud Armor = WAF (DDoS). DLP = Redact PII (Credit Cards). |
| **26** | **Billing** | Budgets (Alerts only). Quotas (Hard limits). BigQuery Export (Analysis). |
| **27** | **IaC** | Terraform = Declarative Blueprint. Reproducible infrastructure. |

---

## 🎯 2. Exam Focus Areas

### Critical Concepts for ACE Exam

#### Cloud Operations (Stackdriver)
- **Monitoring:** Metrics, Dashboards, Uptime Checks.
  - **Ops Agent:** Required for **RAM (Memory)** and **Disk Space** logs within the OS. Standard GCP metrics only see "outside" (CPU usage).
- **Logging:** Centralized logs.
  - **Sinks:** Export logs to **Cloud Storage** (Compliance/Long-term), **BigQuery** (Analytics), or **Pub/Sub** (Splunk/External).
- **Trace:** Latency bottleneck analysis (Microservices).
- **Profiler:** CPU/RAM efficiency (Code optimization).

#### IAM Troubleshooting
- **Policy Troubleshooter:** "Why can't User X do Action Y?"
- **Service Accounts:**
  - **Keyless:** Workload Identity (Best Practice for GKE).
  - **Keys:** Downloaded JSON keys (Security risk if leaked).

#### Billing & Resource Management
- **Budgets:**
  - Sending email = Free.
  - Stopping billing = Requires **Pub/Sub** -> **Cloud Function** (Programmatic).
- **Quotas:**
  - **Rate Quota:** API calls per minute (prevent spam).
  - **Allocation Quota:** Number of VMs per region (prevent hoarding).
- **Labels:** User-defined tags for cost tracking (`env: prod`, `team: sales`).

#### Network Security
- **Identity-Aware Proxy (IAP):**
  - Allows SSH/RDP into private VMs **WITHOUT** functionality external IP.
  - Exam Keyword: "Secure administrative access without VPN or Bastion host".
- **Cloud Armor:**
  - WAF (Web Application Firewall) attached to **Global Load Balancer**.
  - Blocks SQL Injection, XSS, Geo-blocking.

---

## ⚠️ 3. Common Mistakes

### Mistake #1: Thinking Support Roles Grant Access
**Wrong:** "I gave him 'Billing Account Viewer' so he can create VMs."  
**Right:** Billing roles ONLY allow viewing/managing billing. You need `Compute Instance Admin` to create VMs.

### Mistake #2: Terraform State Management
- **Local State (`terraform.tfstate`):** Dangerous for teams (conflicts).
- **Remote State (GCS Bucket):** Best practice regarding locking and team collaboration.

### Mistake #3: Forgetting the Ops Agent
- **Exam Scenario:** "You set up an Alert for 90% Memory usage but it's not firing."
- **Reason:** You didn't install the Ops Agent. GCP implies CPU visibility, not RAM visibility.

---

## 🧪 4. Hands-On Review Lab

Secure a text-handling function.

### Project: Secure Event-Driven Function

**Scenario:** A specialized Cloud Function that processes files uploaded to a bucket, but uses a specific Service Account for security.

**Steps:**

1.  **Create Service Account**
    ```bash
    gcloud iam service-accounts create function-sa \
      --display-name="Function Runner"
    ```

2.  **Grant Permissions (Least Privilege)**
    - Needs to read from buckets.
    - Needs to write logs.
    ```bash
    gcloud projects add-iam-policy-binding $PROJECT_ID \
      --member="serviceAccount:function-sa@$PROJECT_ID.iam.gserviceaccount.com" \
      --role="roles/storage.objectViewer"
    
    gcloud projects add-iam-policy-binding $PROJECT_ID \
      --member="serviceAccount:function-sa@$PROJECT_ID.iam.gserviceaccount.com" \
      --role="roles/logging.logWriter"
    ```

3.  **Deploy Function (Review)**
    ```bash
    gcloud functions deploy secure-func \
      --runtime python310 \
      --trigger-http \
      --allow-unauthenticated \
      --service-account=function-sa@$PROJECT_ID.iam.gserviceaccount.com \
      --entry-point=hello_world \
      --source=.
    ```

**What You Practiced:**
- ✅ Custom Service Account creation
- ✅ Granular role assignment
- ✅ Deploying with a specific identity

---

## 📚 5. Study Tips for Week 5

- **You are NOT done!** We have expanded the course to **Week 7**.
- **Week 5 is "Advanced Architecting".**
  - We will cover Hybrid Connectivity (VPN/Interconnect).
  - Data Analytics (BigQuery Deep Dive).
  - Pub/Sub pipelines.

---

## 🏆 6. What's Next? Week 5!

The journey continues. We move from "admin" to "architect".

*   **Day 29:** Architecture Case Studies (Netflix/Spotify style).
*   **Day 30:** Advanced Data (BigQuery).
*   **Day 31:** Pub/Sub & Data Pipelines.
*   **Day 32:** Dataflow & Dataproc.
*   **Day 33:** Hybrid Cloud (VPNs).
*   **Day 34:** Database Migration.

> **🎉 Milestone Reached: Core ACE curriculum complete. Now leveling up to Professional Architect skills.**
