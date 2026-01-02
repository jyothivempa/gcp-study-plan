# Day 7: Week 1 Review & Exam Strategy

**Level:** Review  
**Milestone:** 🏁 Week 1 Complete!

---

## 🔁 1. Week 1 Recap

Congratulations! You have set the foundation for your Cloud Career.

| Day | Topic | Key Takeaway |
| :--- | :--- | :--- |
| **1** | **Foundations** | Cloud = Renting resources. OpEx > CapEx. IaaS/PaaS/SaaS. |
| **2** | **Projects & Billing** | Projects isolate resources. Budgets prevent bankruptcy. |
| **3** | **Compute Engine** | IaaS. Zones for HA. Choosing the right Machine Family. |
| **4** | **Cloud Storage** | Object storage. Buckets are global names. Storage Classes save money. |
| **5** | **Networking** | VPC is Global. Subnets are Regional. Firewall rules block ingress by default. |
| **6** | **IAM** | Identity (Who) + Role (What). Least Privilege is King. |

---

## 🧪 2. Week 1 Mock Exam (10 Questions)

Test your knowledge. No cheating!

### Question 1
**You want to deploy a specialized database that requires massive memory (4TB+). Which Compute Engine machine family should you choose?**
*   A. E2 (General Purpose)
*   B. C2 (Compute Optimized)
*   C. **M2 (Memory Optimized)** ✅
*   D. N1 (General Purpose)

### Question 2
**You need to store audit logs for 7 years to meet legal regulations. You will likely never access them. Which storage class is cheapest?**
*   A. Standard
*   B. Nearline
*   C. **Archive** ✅
*   D. Coldline

### Question 3
**You created a web server VM but cannot reach it via the External IP. You confirmed the web server software is running. what is the most likely cause?**
*   A. The VM is in the wrong Zone.
*   B. **You forgot to create a Firewall Rule allowing Port 80.** ✅
*   C. You need to enable Billing.
*   D. IAM permissions are missing.

### Question 4
**Which GCP resource is Global?**
*   A. Subnet
*   B. VM Instance
*   C. **VPC Network** ✅
*   D. Persistent Disk

### Question 5
**You need to give a contractor access to upload files to a bucket, but nothing else. What should you do?**
*   A. Make them a Project Editor.
*   B. **Assign the 'Storage Object Creator' role to their email on that specific bucket.** ✅
*   C. Share your password.
*   D. Make the bucket public.

### Question 6
**Which pricing model offers the best discount for running a VM 24/7 for 3 years?**
*   A. Preemptible Instances
*   B. **Committed Use Discounts** ✅
*   C. Sustained Use Discounts
*   D. Free Tier

### Question 7
**True or False: A single Project can be linked to multiple Billing Accounts.**
*   A. True
*   B. **False** (One Project -> One Billing Account) ✅

### Question 8
**What is the difference between IaaS and PaaS?**
*   A. IaaS is cheaper.
*   B. **IaaS manages Infrastructure (OS/Hardware); PaaS manages the Runtime/Platform (just Code).** ✅
*   C. PaaS is for storage only.

### Question 9
**Which firewall rule allows traffic from ANYWHERE?**
*   A. Source: 127.0.0.1
*   B. **Source: 0.0.0.0/0** ✅
*   C. Source: 192.168.0.0/16

### Question 10
**What is a Service Account?**
*   A. A support ticket.
*   B. **A special account used by an application or VM/Robot to interact with GCP.** ✅
*   C. An administrator account.

---

## 🏆 3. What's Next? Week 2!

Week 2 gets serious. We move from "Basics" to "Management".

*   **Managed Instance Groups (MIGs):** Auto-scaling your VMs.
*   **Load Balancing:** Distributing traffic globally.
*   **Cloud SQL:** Managed Databases.
*   **App Engine & Cloud Run:** Serverless computing.

> **🎉 Take a break! You earned it.**

