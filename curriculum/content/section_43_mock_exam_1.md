# SECTION 43: Mock Exam 1 (Simulation)

> **Format**: 20 High-Quality Questions replicating the ACE difficulty.
> **Time Limit**: 45 minutes.

## Instructions
1.  Read the question.
2.  Select your answer mentally.
3.  Reveal the answer by expanding the toggle (or reading the text below).

---

## 🏗️ Domain 1: Setting up a Cloud Solution Environment

### Q1. IAM & Groups
**Scenario:** You have 50 developers in the "frontend-team". You need to give them all access to view logs in Project A. A week later, 5 new devs join.
**Q**: What is the Google Best Practice?
*   A. Create a Service Account for each dev.
*   B. Assign `roles/logging.viewer` to each user individually.
*   C. **Create a Google Group**, add all devs to the group, and assign `roles/logging.viewer` to the Group.
*   D. Give them `roles/owner` so they stop complaining.

> **Answer: C.** Always manage permissions via Groups. When new devs join, you just add them to the Group. No IAM policy change needed.

### Q2. Hierarchy Permissions
**Scenario:** You have an Organization Policy at the **Root** level that enforces `allowed-locations: us-central1`. You have a project inside a folder. You try to create a bucket in `europe-west1`.
**Q**: What happens?
*   A. It works because Projects override folders.
*   B. **It fails.** Organization Policies are inherited top-down and are restrictive.
*   C. It works if you are an Owner.
*   D. It fails unless you use `gcloud --force`.

> **Answer: B.** Org Policies flow down. If the Root says "US only", the Project cannot violate that.

---

## 💻 Domain 2: Planning and Configuring a Solution

### Q3. Compute Engine Availability
**Scenario:** You need to ensure your web application can survive a generic zonal failure.
**Q**: What configuration do you need?
*   A. A single VM with a backup.
*   B. **Managed Instance Group (MIG)** distributed across multiple zones (Regional).
*   C. A larger machine type.
*   D. Preemptible VMs.

> **Answer: B.** Regional MIGs distribute VMs across zones (us-central1-a, b, c). If `a` goes down, `b` and `c` keep running.

### Q4. Storage Costs
**Scenario:** You have 1TB of compliance data. You must keep it for 5 years. You will access it roughly once every 2 years.
**Q**: Which class is cheapest?
*   A. Standard.
*   B. Nearline.
*   C. Coldline.
*   D. **Archive**.

> **Answer: D.** Archive is for data accessed < once/year. It has the lowest storage cost.

### Q5. Kubernetes (GKE) Pods
**Scenario:** You deployed an app to GKE. You want to ensure that there are always 3 copies of your pod running.
**Q**: Which resource do you define?
*   A. Pod.
*   B. Container.
*   C. **Deployment** (containing a ReplicaSet).
*   D. Service.

> **Answer: C.** Deployments manage ReplicaSets, which ensure the desired number of pods are running.

---

## 🚀 Domain 3: Deploying and Implementing

### Q6. App Engine Versions
**Scenario:** You are deploying a new version of your App Engine app. You want to send 1% of traffic to the new version to test it (Canary Deployment).
**Q**: How do you do this?
*   A. Delete the old version.
*   B. Use `gcloud app deploy --promote`.
*   C. **Deploy with `--no-promote`**, then use Traffic Splitting in the Console to send 1%.
*   D. Use a Load Balancer.

> **Answer: C.** `--no-promote` deploys it but keeps it at 0% traffic. Then you manually split traffic.

### Q7. Cloud Functions Limits
**Scenario:** You have a Python script that takes 25 minutes to process a large video file. You want to run it on Cloud Functions 1st Gen.
**Q**: Will it work?
*   A. Yes.
*   B. **No.**
*   C. Only if you use 8GB RAM.

> **Answer: B.** Cloud Functions 1st Gen times out at 9 minutes. 2nd Gen goes to 60 mins (HTTP). Cloud Run is better for long jobs.

---

## 🔒 Domain 4: Ensuring Successful Operation

### Q8. Monitoring vs Logging
**Scenario:** Your boss asks: "Who deleted the database yesterday?"
**Q**: Where do you look?
*   A. Cloud Monitoring.
*   B. **Cloud Logging (Audit Logs).**
*   C. Error Reporting.
*   D. Billing Report.

> **Answer: B.** Logging answers "Who, What, When". Monitoring answers "How much CPU?".

### Q9. SSH Connection Issues
**Scenario:** You cannot SSH into your VM. You checked the firewall, and port 22 is open.
**Q**: What is the most likely issue?
*   A. The VM is preemptible.
*   B. **The VM has no external IP** and you are not using IAP.
*   C. You forgot your password.
*   D. GCP is down.

> **Answer: B.** To SSH directly, you need a Public IP OR use Identity-Aware Proxy (IAP) for private VMs.

---

## 🛡️ Domain 5: Security and Access

### Q10. Service Accounts in VMs
**Scenario:** Your application on a VM needs to write to a Cloud Storage bucket.
**Q**: How should you authenticate?
*   A. Hardcode your owner/password in the code.
*   B. Upload a JSON Service Account key to the VM.
*   C. **Attach a Service Account to the VM** with `roles/storage.objectAdmin`.
*   D. Make the bucket public.

> **Answer: C.** Never handle keys if you can avoid it. Attaching the SA allows the VM to authenticate automatically via Metadata Server.

### Q11. Secret Management
**Scenario:** Additional DB passwords are needed in your Cloud Function.
**Q**: Where should you store them?
*   A. In the source code.
*   B. In an environment variable (plaintext).
*   C. **Secret Manager**.
*   D. A text file in the bucket.

> **Answer: C.** Secret Manager encrypts, versions, and audits access to secrets.

---

## 🧠 Mixed Bag

### Q12. Preemptible VMs
**Scenario:** You have a batch processing job that runs for 4 hours. It can be stopped and resumed without issues. You want to save money.
**Q**: What do you use?
*   A. E2-standard-4.
*   B. **Preemptible (or Spot) VMs.**
*   C. Committed Use Discounts.

> **Answer: B.** Spot VMs are up to 90% cheaper but can be stopped by Google at any time.

### Q13. VPC Peering vs Shared VPC
**Scenario:** Team A and Team B have separate projects. They are completely independent but need to talk via private IP.
**Q**: What is the simplest way to connect them?
*   A. Shared VPC.
*   B. **VPC Peering.**
*   C. Cloud VPN.

> **Answer: B.** Peering connects two defaults (decentralized). Shared VPC is for centralized control (one host project).

### Q14. BigQuery Cost Control
**Scenario:** Your intern ran a `SELECT *` query and cost you $500.
**Q**: How do you prevent this?
*   A. Fire the intern.
*   B. **Set a Custom Quota (Maximum bytes billed)** per day for the project or user.
*   C. Use `LIMIT 10`. (This does NOT reduce cost!).

> **Answer: B.** `LIMIT` affects output, not scanning cost. Custom Quotas enforce a hard limit on bytes processed.

### Q15. Cloud Run vs Cloud Run Jobs
**Scenario:** You have a script that generates a report every nigh. It is not an HTTP request service.
**Q**: What do you use?
*   A. Cloud Run Service.
*   B. **Cloud Run Jobs.**
*   C. App Engine Flex.

> **Answer: B.** Jobs are for "run to completion" tasks. Services are for "serve requests".

### Q16. Global Load Balancing
**Scenario:** You have users in Tokyo, London, and New York. You want them to reach your app via a single IP, and land on the closest server.
**Q**: Which LB?
*   A. **External HTTP(S) Load Balancer (Global).**
*   B. Network Load Balancer.
*   C. Regional External HTTP LB.

> **Answer: A.** Global LB uses Anycast IP to route users to the nearest Google Point of Presence.

### Q17. CMEK
**Scenario:** A banking client requires that THEY manage the encryption keys, not Google.
**Q**: What feature is this?
*   A. Default Encryption.
*   B. **Customer-Managed Encryption Keys (CMEK) via Cloud KMS.**
*   C. CSEK (Customer-Supplied).

> **Answer: B.** CMEK lets you manage keys in KMS. (CSEK is where you hold the raw key on-prem, rarely used).

### Q18. Filestore
**Scenario:** You need a shared file system (NFS) for 100 Linux VMs to read/write data simultaneously.
**Q**: Which service?
*   A. Cloud Storage (GCS).
*   B. Persistent Disk.
*   C. **Filestore.**
*   D. Bigtable.

> **Answer: C.** Filestore is fully managed NFS. GCS is object storage (not posix). PD can only be ReadWrite by ONE VM (mostly).

### Q19. Cloud Build
**Scenario:** You want to build a Docker image every time code is pushed to the `main` branch.
**Q**: What resource do you create?
*   A. A Cron job.
*   B. **Cloud Build Trigger.**
*   C. A Jenkins server.

> **Answer: B.** Triggers listen to VCS events.

### Q20. Billing Exports
**Scenario:** You need to analyze your spending trends using SQL queries and visualize them in Looker Studio.
**Q**: What is step 1?
*   A. Download CSV.
*   B. **Enable Billing Export to BigQuery.**
*   C. Use the Cost Management console.

> **Answer: B.** To use SQL, you must export the data to BigQuery.

---

## 🏁 Calculate Your Score

*   **18-20**: Ready for the real exam!
*   **14-17**: Review your weak domains.
*   **< 14**: Re-read Weeks 1-4.
