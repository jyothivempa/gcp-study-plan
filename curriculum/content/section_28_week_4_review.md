# Day 28: Week 4 Review & Exam Strategy

**Level:** Review  
**Milestone:** 🏁 Week 4 Complete! (Ops & Security)

---

## 🔁 1. Week 4 Recap (Day 2 Ops)

You now know how to run, secure, and pay for the cloud.

| Day | Topic | Key Takeaway |
| :--- | :--- | :--- |
| **22** | **Ops** | Metrics (Speedometer) vs Logs (Black Box) vs Alerts. Ops Agent needed for Memory. |
| **23** | **IAM** | Service Accounts = Identity for Robots. Least Privilege. Troubleshooter. |
| **24** | **NetSec** | Firewall Rules (Priority). IAP = SSH without Public IP. |
| **25** | **DataSec** | Default Encryption. CMEK = You hold the key. |
| **26** | **Billing** | Budgets (Alerts only). Quotas (Hard limits). BigQuery Export (Analysis). |
| **27** | **IaC** | Terraform = Declarative Blueprint. Reprodicuble. |

---

## 🧪 2. Week 4 Mock Exam (10 Questions)

### Question 1
**You need to prevent your team from accidentally spinning up expensive GPU instances. What mechanism should you use?**
*   A. Budget Alert
*   B. **Quota (Limit to 0 GPUs)** ✅
*   C. Firewall Rule
*   D. IAM Policy

### Question 2
**You SSH into a VM and check `free -m`. You see 90% RAM usage. You go to Cloud Monitoring but only see CPU. Why?**
*   A. RAM metrics are delayed.
*   B. **You did not install the Ops Agent.** ✅
*   C. You need a larger VM.
*   D. Logging is disabled.

### Question 3
**You have a private VM with no external IP. You need to SSH into it securely. Best option?**
*   A. Give it a public IP temporarily.
*   B. **Configure Identity-Aware Proxy (IAP).** ✅
*   C. VPN.
*   D. Bastion Host.

### Question 4
**Who manages the keys when using "Default Encryption"?**
*   A. You.
*   B. **Google.** ✅
*   C. Cloud KMS.
*   D. The Auditor.

### Question 5
**Does a Billing Budget stop your services when the threshold is met?**
*   A. Yes.
*   B. **No.** ✅

### Question 6
**An application running on a VM needs to access a Bucket. What is the secure way to handle auth?**
*   A. Hardcode credentials in code.
*   B. **Assign a Service Account to the VM.** ✅
*   C. Use your personal Gmail.
*   D. Make the bucket public.

### Question 7
**Which firewall rule takes precedence?**
*   A. Priority 1000 Deny
*   B. Priority 65535 Allow
*   C. **Priority 100 Allow** (Lowest number wins) ✅
*   D. Priority 1000 Allow

### Question 8
**What is the benefit of Terraform over gcloud scripts?**
*   A. Imperative execution.
*   B. **Declarative state management (Idempotency).** ✅
*   C. It runs on Windows.

### Question 9
**You need to analyze billing data to find out how much a specific label cost last month.**
*   A. Look at the PDF invoice.
*   B. **Export Billing to BigQuery and write SQL.** ✅
*   C. Use Cloud Logging.

### Question 10
**What is the purpose of Cloud Armor?**
*   A. Encrypt data.
*   B. **Protect Global Load Balancers from DDoS and Web Attacks.** ✅
*   C. Firewall for VMs.

---

## 🏆 3. End of Course!

**Congratulations!** You have completed the 4-week "GCP Zero to Hero" Study Plan.
*   Week 1: Core Infra (Compute, Storage, Network).
*   Week 2: Scale (MIGs, SQL, Serverless).
*   Week 3: Kubernetes (GKE).
*   Week 4: Security & Ops.

> **Next Steps:** Review all Mock Exams. Book your ACE exam. Good luck! 🎓

