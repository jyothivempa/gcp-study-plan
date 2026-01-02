# Day 14: Week 2 Review & Exam Strategy

**Level:** Review  
**Milestone:** 🏁 Week 2 Complete!

---

## 🔁 1. Week 2 Recap (Management & Scale)

You have graduated from single VMs to massive, auto-scaling architecture.

| Day | Topic | Key Takeaway |
| :--- | :--- | :--- |
| **8** | **Instance Groups** | MIGs = Cattle (Stateless). Auto-healing & Auto-scaling. |
| **9** | **Load Balancing** | Global HTTP(S) LB is Layer 7. Health Checks determine routing. |
| **10** | **Cloud SQL** | Managed MySQL/Postgres. HA is for reliability, Read Replicas are for speed. |
| **11** | **Storage Adv** | Lifecycle rules automate deletions. Signed URLs give temporary access. |
| **12** | **App Engine** | PaaS. Standard (Scale to 0) vs Flexible (Docker). Traffic Splitting. |
| **13** | **Cloud Run** | Serverless Containers. Portable. Best for modern microservices. |

---

## 🧪 2. Week 2 Mock Exam (10 Questions)

### Question 1
**You have a web application in a MIG. Users report 500 errors. You notice the CPU usage is low. The Load Balancer Health Check is failing for 2 instances. What will the MIG do?**
*   A. Restart the Load Balancer.
*   B. **Delete the unhealthy instances and recreate them (Auto-healing).** ✅
*   C. Add more instances (Auto-scaling).
*   D. Send an email only.

### Question 2
**You need a global database that scales horizontally to handle millions of transactions per second.**
*   A. Cloud SQL
*   B. **Cloud Spanner** ✅
*   C. Bigtable
*   D. Firestore

### Question 3
**You want to deploy a legacy Java application that requires specific OS modifications. You want a managed platform.**
*   A. App Engine Standard
*   B. **App Engine Flexible** ✅
*   C. Cloud Functions
*   D. Cloud SQL

### Question 4
**Which Load Balancer type preserves the client IP address and handles TCP traffic without inspecting headers?**
*   A. External HTTP(S) LB
*   B. **External Network TCP/UDP LB (Passthrough)** ✅
*   C. Internal HTTP LB

### Question 5
**You need to store objects for legal reasons for 10 years. You trigger a delete command. Which feature prevents this deletion?**
*   A. Lifecycle Policy
*   B. **Retention Policy (Bucket Lock)** ✅
*   C. Versioning
*   D. Signed URL

### Question 6
**Cloud Run scales based on:**
*   A. CPU usage only.
*   B. **Concurrency (Requests per container).** ✅
*   C. Memory usage.
*   D. Number of nodes.

### Question 7
**What is the fastest way to roll back a buggy App Engine version?**
*   A. Redeploy the old code.
*   B. **Traffic Splitting (Switch 100% traffic back to previous version instantly).** ✅
*   C. Delete the project.

### Question 8
**You have a read-heavy Analytics app using Cloud SQL. The main database is slow. What is the best fix?**
*   A. Increase CPU.
*   B. **Create Read Replicas and point analytics queries there.** ✅
*   C. Use SSDs.

### Question 9
**Which storage class allows you to access data instantly but charges a retrieval fee?**
*   A. Standard
*   B. **Nearline / Coldline / Archive (All have instant access, but retrieval fees apply).** ✅
*   C. Tape

### Question 10
**You have a Docker container. You want to run it Serverlessly. Which two services can you use?**
*   A. Compute Engine & Cloud Run
*   B. **App Engine Flexible & Cloud Run** ✅
*   C. GKE & Compute Engine

---

## 🏆 3. What's Next? Week 3!

Week 3 is **Kubernetes Week**.
*   **GKE (Google Kubernetes Engine):** The industry standard for container orchestration.
*   **Pods, Services, Deployments:** The k8s vocabulary.

> **🎉 Great job! You are halfway to becoming a Cloud Engineer.**

