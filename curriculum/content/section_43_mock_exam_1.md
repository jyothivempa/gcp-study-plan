# Day 45: Final Mock Exam & Certification Readiness

**Duration:** ⏱️ 120 Minutes  
**Level:** Simulation  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ 100% (The Grand Finale)

---

## 🏁 The Final Simulation

This is it. 20 high-fidelity questions that replicate the difficulty, phrasing, and technical depth of the Official Google Cloud Associate Cloud Engineer exam.

**Rules:**
1.  **Time Limit:** 45 minutes.
2.  **Passing Score:** 16/20 (80%).
3.  **Mindset:** Think like an SRE—reliability and cost are everything.

---

## 🏗️ Domain 1: Setting up a Cloud Solution Environment


1.  **Scenario: You have 3 projects (Dev, Test, Prod). You want to ensure that only the 'Prod' project has 'Billing Export' enabled to BigQuery to save on storage costs. Where do you configure this?**
    *   A. In each project's settings.
    *   B. **In the Billing Account settings.** ✅ (Billing exports are configured at the Billing Account level).
    *   C. In the Organization IAM.
    *   D. In BigQuery Dataset properties.

2.  **You need to prevent any developer from creating a VM with an External IP in a specific folder. Which tool do you use?**
    *   A. VPC Firewall Rules.
    *   B. **Organization Policy (Constraints).** ✅ (Org policies can restrict resource configurations).
    *   C. IAM Custom Roles.
    *   D. Cloud Armor.

## 💻 Domain 2: Planning and Configuring

3.  **Requirement: You need a database that handles global relational data with high availability (99.999%) and horizontal scaling. Cost is not the primary concern.**
    *   A. Cloud SQL.
    *   B. **Cloud Spanner.** ✅ (The only global relational DB with that SLA).
    *   C. Cloud Bigtable.
    *   D. Firestore.

4.  **Requirement: A batch processing job runs for 10 hours but can be interrupted. You want to minimize cost.**
    *   A. E2-Standard-8.
    *   B. **Spot (Preemptible) VMs.** ✅ (Up to 90% cheaper).
    *   C. Committed Use Discounts.
    *   D. App Engine Standard.

## 🚀 Domain 3: Deploying and Implementing

5.  **How do you deploy a new version of an App Engine app without immediate traffic promotion?**
    *   A. `gcloud app deploy --promote`.
    *   B. **`gcloud app deploy --no-promote`.** ✅ (`--no-promote` keeps the new version at 0% traffic).
    *   C. `kubectl apply -f app.yaml`.
    *   D. Use Cloud Build.

6.  **Which command allows you to increase the number of nodes in a GKE cluster named 'my-cluster'?**
    *   A. `kubectl scale deployment ...`
    *   B. **`gcloud container clusters resize my-cluster --num-nodes=5`.** ✅ (Cluster size is a GCP resource level action).
    *   C. `gcloud compute instances scale`.
    *   D. Edit the YAML in the console.

## 🔒 Domain 4: Ensuring Successful Operation

7.  **A VM is running out of disk space. You have increased the Persistent Disk size in the Console. What is the next step?**
    *   A. Restart the VM.
    *   B. **Resize the file system within the OS (e.g., `resize2fs`).** ✅ (Increasing disk size doesn't auto-resize the partition).
    *   C. Take a snapshot and create a new VM.
    *   D. Use `gsutil`.

8.  **You need to find out why a specific user was granted the 'Owner' role 2 hours ago. Where do you look?**
    *   A. Cloud Monitoring.
    *   B. **Cloud Logging (Activity Logs).** ✅ (Audit logs track "Who did What").
    *   C. IAM Dashboard.
    *   D. Security Command Center.

## 🛡️ Domain 5: Security and Access

9.  **Your application on a VM needs to access a private Cloud Storage bucket. What is the Google-recommended way to provide credentials?**
    *   A. Download a JSON key to the VM.
    *   B. **Assign a Service Account to the VM and use the Metadata Server.** ✅ (No keys to manage).
    *   C. Put the credentials in the metadata (labels).
    *   D. Use your own user account.

10. **A contractor needs access to a specific private object in GCS for 15 minutes. What should you generate?**
    *   A. A Service Account Key.
    *   B. **A Signed URL.** ✅ (Temporary access without IAM changes).
    *   C. A Public Link.
    *   D. A VPN Tunnel.

## 🧠 Mixed Bag (The "Pro" Level)

11. **You are using Cloud Build to build a container. You want the build to trigger ONLY when a tag starting with 'v*' is pushed to Git. Where is this filter set?**
    *   A. In the `cloudbuild.yaml`.
    *   B. **In the Cloud Build Trigger configuration.** ✅
    *   C. In GitHub settings.
    *   D. In the VPC Firewall.

12. **You want to connect an on-premises network to GCP with 10 Gbps of dedicated bandwidth. Which service?**
    *   A. Carrier Peering.
    *   B. **Dedicated Interconnect.** ✅ (Physical direct fiber).
    *   C. HA VPN.
    *   D. VPC Peering.

13. **Which BigQuery feature helps reduce the number of bytes scanned for queries that filter by a `timestamp` column?**
    *   A. Clustering.
    *   B. **Partitioning.** ✅ (Pruning happens at the partition level).
    *   C. Materialized Views.
    *   D. SQL LIMIT.

14. **You have multiple VPCs across different organizations that need to communicate. What is the best hub-and-spoke solution?**
    *   A. VPC Peering.
    *   B. **Network Connectivity Center.** ✅ (Managed hub for multi-org/multi-vpc).
    *   C. Shared VPC.
    *   D. Cloud NAT.

15. **A Cloud Run service is experiencing high latency. You suspect the cold start is the issue. How do you mitigate this?**
    *   A. Increase CPU.
    *   B. **Set 'Minimum Instances' to 1.** ✅ (Keeps a container 'warm').
    *   C. Use GKE.
    *   D. Enable Cloud CDN.

16. **You have 1 PB of data in GCS Standard. You won't touch it for 365 days. How do you save the MOST money?**
    *   A. Just leave it.
    *   B. **Move it to Archive Class.** ✅ (Lowest storage cost for long-term data).
    *   C. Delete it.
    *   D. Compress it.

17. **Which gcloud component is used to manage local docker authentication for Artifact Registry?**
    *   A. `gcloud auth login`.
    *   B. **`gcloud auth configure-docker`.** ✅
    *   C. `gcloud container clusters`.
    *   D. `gsutil`.

18. **A GKE pod is failing to pull an image from Artifact Registry. The Service Account has 'Viewer' role on the project. What is the likely missing permission?**
    *   A. `roles/artifactregistry.writer`.
    *   B. **`roles/artifactregistry.reader` on the specific repository.** ✅ (Project viewer doesn't always include granular resource access).
    *   C. `roles/owner`.
    *   D. The pod has no internet.

19. **You need to store secrets for your application. You want them to be versioned and encrypted. Which service?**
    *   A. Cloud KMS.
    *   B. **Secret Manager.** ✅ (Versions, audits, and simple API).
    *   C. Metadata Server.
    *   D. Environment Variables.

20. **You are auditing a VPC. You see a route with destination `0.0.0.0/0` and next hop `default-internet-gateway`. What does this do?**
    *   A. Blocks all traffic.
    *   B. **Provides a path for outbound traffic to the public internet.** ✅
    *   C. Connects to on-premises.
    *   D. Enables VPC Peering.

21. **Scenario: Your gcloud command is failing with "Insufficient permissions". You want to see which exact identity is being used. Which command do you run?**
    *   A. `gcloud auth login`.
    *   B. **`gcloud config list` or `gcloud auth list`.** ✅ (Shows the active account).
    *   C. `kubectl auth can-i`.
    *   D. `gcloud iam roles list`.

22. **Requirement: You need to migrate a 10 TB SQL Server database from on-premises to GCP with minimal downtime. Which service should you choose?**
    *   A. Cloud Storage Transfer Service.
    *   B. **Database Migration Service (DMS).** ✅ (Designed for minimal downtime migrations).
    *   C. Manual export/import.
    *   D. BigQuery Data Transfer Service.

23. **You are using GKE Autopilot. You want to ensure your pod runs on a node with an SSD. How do you specify this?**
    *   A. Create a new Node Pool with SSDs.
    *   B. **Use a `nodeSelector` or `ephemeral-storage` request in your Pod spec.** ✅ (Autopilot manages the underlying nodes based on Pod needs).
    *   C. SSH into the node and mount the SSD.
    *   D. You cannot use SSDs in Autopilot.

24. **A team says they can't see the Cloud Console. You find out the Organization Policy "Disable Service Usage" is on. Where is this likely applied?**
    *   A. At the Project level.
    *   B. **At the Organization or Folder level.** ✅ (Org policies are usually applied high up to set guardrails).
    *   C. In the IAM Role.
    *   D. Inside the VPC.

25. **Which command is used to sync a local directory to a Cloud Storage bucket?**
    *   A. `gcloud storage cp`.
    *   B. **`gcloud storage rsync`.** ✅ (Syncs changes only, mirroring the local state).
    *   C. `gsutil cat`.
    *   D. `terraform apply`.

---

## 📖 Question Explanations (The Deep Dive)

1.  **Billing Export:** Billing is a **Billing Account** level resource. While projects *contain* resources, the billing account *pays* for them and holds the export settings.
2.  **Org Policy:** Firewalls control traffic (IPs), but **Org Policies** control resource creation rules (No External IPs allowed).
3.  **Cloud Spanner:** Relational + Global + 99.999% SLA = Spanner. Cloud SQL is regional. Bigtable is Non-relational.
4.  **Spot VMs:** Previously called Preemptible. They are 60-91% cheaper for interruptible jobs.
5.  **App Engine Promote:** The `--no-promote` flag is the standard for "Canary" or "Blue/Green" testing before moving 100% traffic.
6.  **GKE Resize:** Changing node count is a **GCP** infrastructure change, so use `gcloud`. `kubectl scale` changes pod counts inside K8s.
7.  **Disk Resize:** Increasing bits on a disk (GCP level) doesn't change the partition (OS level). You must tell the OS to use the new space.
8.  **Logging:** Audit logs are the "Forensics" of GCP. They answer "Who did what, where, and when?".
9.  **Service Accounts:** JSON keys are a security risk if leaked. **Service Accounts** attached to VMs use the metadata server to get temporary tokens automatically.
10. **Signed URL:** For one-off, time-limited access to private objects for people without Google accounts.
11-20. [Summarized logic: Always choose the most managed, cost-effective, and secure option according to the Shared Responsibility Model.]
21. **gcloud identity:** `gcloud config list` shows your active project, account, and zone—the FIRST place to check for permission errors.
22. **Migration:** **DMS** handles the underlying replication (CDC) to keep the target in sync until you are ready to cut over.
23. **Autopilot SSD:** In Autopilot, your Pod Spec IS your infrastructure request. Google provisions the right hardware to match your Pod demands.
24. **Org Policy Scope:** These are almost always applied at the **Org/Folder** level to ensure "Inherited" compliance across all sub-projects.
25. **rsync:** `cp` copies everything; `rsync` only copies what's different. Pro-choice for massive data moves.


---

## 🏁 Final Evaluation

| Score | Status | Recommendation |
| :--- | :--- | :--- |
| **18-20** | 🏆 **ACE MASTER** | You are ready. Book the exam today! |
| **15-17** | 👍 **READY** | Review your incorrect answers and scheduling. |
| **< 15** | 📚 **MORE STUDY** | Re-read the Week reviews and Capstone retrospectives. |

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I completed the final mock exam under timed conditions.', checked: false },
        { text: 'I understand why I got my incorrect answers wrong.', checked: false },
        { text: 'I have scheduled my official exam.', checked: false },
        { text: 'I am a Certified Cloud Engineer (In Progress)!', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Ready for Certification?
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
