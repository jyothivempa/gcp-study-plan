# GCP Interview Question Bank

> **Master Collection:** 60+ interview questions organized by topic and difficulty level.

---

## 📊 Question Distribution

| Topic | Beginner | Intermediate | Advanced | Total |
|-------|----------|--------------|----------|-------|
| IAM & Security | 3 | 3 | 3 | 9 |
| VPC Networking | 3 | 3 | 3 | 9 |
| Compute Engine | 2 | 3 | 2 | 7 |
| Containers & GKE | 2 | 3 | 2 | 7 |
| Storage | 2 | 3 | 2 | 7 |
| Serverless | 2 | 3 | 2 | 7 |
| Data Services | 2 | 3 | 2 | 7 |
| DevOps & IaC | 2 | 2 | 2 | 6 |
| **Total** | **18** | **23** | **18** | **59** |

---

## 🔐 IAM & Security

### Beginner

**Q1: What is the difference between a Role and a Permission?**
> "A permission is a single action like `storage.objects.get`. A role is a collection of permissions. I use predefined roles for maintainability."

**Q2: Why avoid Basic Roles (Owner/Editor/Viewer)?**
> "They're too broad. Editor grants write to almost everything. I use predefined roles like `roles/compute.instanceAdmin` for specific access."

**Q3: What is a Service Account?**
> "An identity for applications to make API calls. I use them instead of user accounts for VMs and workloads."

### Intermediate

**Q4: When create Custom Role vs Predefined Role?**
> "Predefined 95% of time—Google maintains them. Custom only when predefined is too permissive and no narrower option exists."

**Q5: How decide between users vs Google Groups for permissions?**
> "Always Groups. Scales better—update group membership, not IAM. Cleaner audit trail."

**Q6: What is Workload Identity Federation?**
> "Exchange external tokens (GitHub, AWS) for GCP access. Eliminates JSON keys for CI/CD."

### Advanced

**Q7: Your CI/CD needs to deploy to GKE. Set this up securely.**
> "Workload Identity Federation → Pool for GitHub → SA with `container.developer` role → No JSON keys."

**Q8: Developer gets 'Permission Denied' creating VM. Troubleshoot.**
> "1. Check `gcloud auth list` 2. Check project 3. Check IAM binding 4. Test permissions 5. Check Org Policies"

**Q9: JSON key leaked to GitHub. Immediate response?**
> "Disable key → Delete key → Check audit logs → Create new SA with least privilege → Implement Workload Identity"

---

## 🌐 VPC Networking

### Beginner

**Q1: Difference between VPC and Subnet in GCP?**
> "VPC is global network spanning all regions. Subnet is regional—VMs are placed in subnets. Unlike AWS, GCP VPCs are global."

**Q2: What happens with no firewall rules in new VPC?**
> "Ingress blocked by default, egress allowed. Must explicitly allow HTTP/HTTPS."

**Q3: What is Private Google Access?**
> "Allows VMs without external IPs to reach Google APIs privately."

### Intermediate

**Q4: VPC Peering vs Shared VPC?**
> "Peering connects separate VPCs across orgs. Shared VPC is one org with central network control. Shared for control, Peering for isolation."

**Q5: VM needs internet access but no public IP. How?**
> "Cloud NAT with Cloud Router. Outbound-only access without exposing VM."

**Q6: Load balancer health checks failing but can curl backend. Why?**
> "Health checks come from 35.191.0.0/16 and 130.211.0.0/22. Need firewall rule allowing these ranges."

### Advanced

**Q7: VMs in VPC-A can't reach VPC-B with peering. Troubleshoot.**
> "1. Check peering ACTIVE both sides 2. Check route export/import 3. Verify no CIDR overlap 4. Check firewalls BOTH VPCs 5. Verify routes"

**Q8: Design network for 50 projects, 3 teams, central control.**
> "Shared VPC with Host Project. Platform team owns VPC. Service Projects for each team. Subnets per team/env."

**Q9: What is IAP tunneling and when to use it?**
> "Identity-Aware Proxy for SSH without opening port 22 to internet. Source range 35.235.240.0/20. Secure alternative to public SSH."

---

## 💻 Compute Engine

### Beginner

**Q1: E2 vs N2 machine types?**
> "E2 cheapest, variable performance—dev/test. N2 consistent performance—production, SLAs."

**Q2: What is Spot VM?**
> "60-91% discount, can be preempted with 30s notice. Use for fault-tolerant batch jobs."

### Intermediate

**Q3: VM needs to survive host maintenance. Configure it.**
> "Live Migration (default). Google moves VM to healthy hardware <1s downtime. GPU VMs must restart."

**Q4: Custom images vs startup scripts?**
> "Images: faster boot, production. Scripts: flexible, dev/test. My pattern: base image + scripts for env config."

**Q5: MIG auto-healing vs auto-scaling?**
> "Healing replaces unhealthy VMs. Scaling adds/removes based on load. Different features."

### Advanced

**Q6: Design solution for 1000 videos/day encoding, cost-optimized.**
> "Spot VMs C2, autoscaling MIG → 0, Pub/Sub queue, checkpoint every 5min to GCS."

**Q7: VM performance degrades every afternoon. Troubleshoot.**
> "Check Monitoring graphs, E2 vs N2, noisy neighbor, scheduled jobs, network quotas."

---

## 🐳 Containers & GKE

### Beginner

**Q1: Why containers start faster than VMs?**
> "Containers share host kernel, virtualize at OS level. VMs boot full OS."

**Q2: GKE Autopilot vs Standard?**
> "Autopilot: Google manages nodes, per-pod billing. Standard: you manage, more control."

### Intermediate

**Q3: What is Workload Identity in GKE?**
> "Link Kubernetes Service Account to GCP Service Account. Pods authenticate without JSON keys."

**Q4: Pod is CrashLoopBackOff. Troubleshoot.**
> "`kubectl describe pod`, `kubectl logs`, check liveness probe, image pull issues, resource limits."

**Q5: When GKE vs Compute Engine?**
> "GKE for microservices, container-native. Compute for monoliths, legacy, licensing."

### Advanced

**Q6: Design microservices deployment on GKE.**
> "Autopilot for simplicity, Workload Identity, horizontal pod autoscaler, Cloud SQL with Auth Proxy."

**Q7: Node pool considerations for ML workloads.**
> "GPU node pool, preemptible for cost, taints/tolerations, cluster autoscaler."

---

## 💾 Storage

### Beginner

**Q1: Which storage class for rarely accessed backups?**
> "Coldline (90 days) or Archive (365 days). Cheaper storage, higher retrieval cost."

**Q2: What is Signed URL?**
> "Time-limited URL granting temporary access. No Google account needed. Max 7 days."

### Intermediate

**Q3: How reduce storage costs for old data?**
> "Lifecycle rules: Standard → Nearline (30d) → Coldline (90d) → Archive."

**Q4: Versioning enabled, costs jumped. Why?**
> "Paying for all versions. Add lifecycle rule to delete versions older than N days."

**Q5: Persistent Disk vs Local SSD?**
> "PD network-attached, survives restart. Local SSD physically attached, data wiped on stop."

### Advanced

**Q6: Design data lake with cost optimization.**
> "Standard for hot data, lifecycle to Archive, partitioned folders, BigQuery external tables."

**Q7: Need 7-year retention, no deletion possible. Solution?**
> "Bucket Lock with Retention Policy. WORM storage. Irreversible."

---

## ⚡ Serverless (Cloud Run / Functions)

### Beginner

**Q1: Cloud Run vs Cloud Functions?**
> "Functions for simple events. Run for complex apps, containers. Both serverless."

**Q2: What causes cold starts?**
> "New container instance initialization. Set min-instances=1 to keep warm."

### Intermediate

**Q3: 1st Gen vs 2nd Gen Cloud Functions?**
> "2nd Gen: 60min timeout (vs 9min), 1000 concurrency, Eventarc, built on Cloud Run."

**Q4: Cloud Run concurrency setting impact?**
> "Higher = fewer instances, lower cost. Lower = more isolation. Balance based on workload."

**Q5: How secure secrets in serverless?**
> "Secret Manager integration. Reference secrets in deployment, mounted at runtime."

### Advanced

**Q6: Design event-driven image processing pipeline.**
> "GCS upload → Pub/Sub → Cloud Function → Process → Store result. DLQ for failures."

**Q7: Canary deployment on Cloud Run.**
> "Deploy new revision, split traffic 90/10, monitor errors, gradually shift."

---

## 📊 Data Services (BigQuery / Pub/Sub)

### Beginner

**Q1: BigQuery pricing model?**
> "On-demand: $5/TB scanned. Flat-rate: slots for predictable cost."

**Q2: Push vs Pull subscription in Pub/Sub?**
> "Push for webhooks, real-time. Pull for batch, rate control, no public endpoint."

### Intermediate

**Q3: How reduce BigQuery query costs?**
> "Partition by date, cluster by frequent filters, SELECT only needed columns."

**Q4: Dead Letter Queue in Pub/Sub?**
> "Catches messages that fail after N retries. Prevents poison messages from blocking."

**Q5: BigQuery vs Cloud SQL?**
> "BigQuery for analytics (OLAP). Cloud SQL for transactions (OLTP)."

### Advanced

**Q6: Design real-time analytics pipeline.**
> "Dataflow streaming → BigQuery. Pub/Sub input → Transform → BigQuery sink."

**Q7: Exactly-once processing requirement. Solution?**
> "Pub/Sub exactly-once delivery + idempotent processing. Dataflow handles this."

---

## 🔧 DevOps & IaC

### Beginner

**Q1: terraform plan vs terraform apply?**
> "Plan shows preview. Apply makes changes. Always review plan first."

**Q2: Where store Terraform state?**
> "Remote backend (GCS bucket). Never commit to git—contains secrets."

### Intermediate

**Q3: Cloud Build trigger types?**
> "GitHub push, PR, schedule, manual. Branch patterns for filtering."

**Q4: Terraform modules benefit?**
> "Reusable, DRY, version controlled. Share across teams via module registry."

### Advanced

**Q5: Design CI/CD for GKE deployment.**
> "GitHub → Cloud Build → Build image → Push to Artifact Registry → Cloud Deploy to GKE."

**Q6: GitOps workflow for infrastructure.**
> "PR to change Terraform → Review → Merge → Cloud Build auto-applies. State in GCS."

---

## 💡 Interview Tips

### Before the Interview
- Review this question bank
- Practice explaining WHY, not just WHAT
- Prepare 2-3 real project examples

### During the Interview
- Start with simple answer, then elaborate
- Admit gaps: "I haven't used X, but my approach would be..."
- Ask clarifying questions for scenarios
