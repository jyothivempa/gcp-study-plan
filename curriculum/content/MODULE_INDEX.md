# GCP Associate Cloud Engineer - Course Module Index

> **Industry-Focused Learning Tracks** organized by job role and skill progression

---

## 📚 How to Use This Guide

This course is organized into **7 learning tracks** instead of a strict day-by-day sequence. You can:
- Follow the **recommended order** for structured learning
- **Jump to specific tracks** based on your career focus
- Use **time estimates** to plan your study schedule

**Total Course Duration:** 60-80 hours (6-8 weeks at 10-12 hrs/week)

---

## 🎯 Track 1: GCP Core Foundations
**Duration:** 12-15 hours | **ACE Exam Weight:** 20%

Master the fundamentals of Google Cloud Platform before diving into specific services.

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **Cloud Fundamentals** | [section_1_cloud_foundations.md](section_1_cloud_foundations.md) | 90 min | Cloud models, GCP vs AWS/Azure, regions |
| **GCP Project Structure** | [section_2_gcp_structure.md](section_2_gcp_structure.md) | 60 min | Organization hierarchy, folders, IAM basics |
| **Billing & Cost Management** | [section_2_gcp_projects_billing.md](section_2_gcp_projects_billing.md) | 60 min | Budgets, billing accounts, cost optimization |
| **Cloud Shell & CLI** | [section_21_cloud_shell.md](section_21_cloud_shell.md) | 90 min | gcloud commands, Cloud Shell editor |

### 🎓 Learning Outcomes
- [ ] Explain GCP's global infrastructure
- [ ] Create and manage projects
- [ ] Set up billing alerts
- [ ] Use gcloud CLI confidently

### 🔍 Job Roles Focus
- **Cloud Engineer:** All modules critical
- **DevOps:** Focus on CLI and scripting
- **FinOps:** Deep dive on billing module

---

## 🎯 Track 2: Compute & App Hosting
**Duration:** 15-18 hours | **ACE Exam Weight:** 25%

Learn how to deploy and manage applications on GCP compute platforms.

| Module | File | Time | Key Topics |
|--------|-----|------|------------|
| **Compute Engine Basics** | [section_4_compute_engine.md](section_4_compute_engine.md) | 120 min | VMs, machine types, Spot VMs, Live Migration |
| **Instance Groups & Auto-scaling** | [section_8_instance_groups.md](section_8_instance_groups.md) | 90 min | MIGs, auto-healing, scaling policies |
| **Load Balancing** | [section_9_load_balancing.md](section_9_load_balancing.md) | 120 min | Global/Regional LB, health checks |
| **Containers Introduction** | [section_15_containers.md](section_15_containers.md) | 90 min | Docker basics, Artifact Registry |
| **GKE Architecture** | [section_16_kubernetes_arch.md](section_16_kubernetes_arch.md) | 120 min | Control plane, nodes, Autopilot vs Standard |
| **Cloud Run** | [section_13_cloud_run.md](section_13_cloud_run.md) | 90 min | Serverless containers, auto-scaling |
| **App Engine** | [section_12_app_engine.md](section_12_app_engine.md) | 90 min | Standard vs Flexible, traffic splitting |
| **Cloud Functions** | [section_23_cloud_functions.md](section_23_cloud_functions.md) | 90 min | Event-driven, Eventarc, triggers |

### 📊 Service Comparison Decision Table

| Need | Use | Why |
|------|-----|-----|
| Full VM control | **Compute Engine** | Custom OS, SSH access, GPU workloads |
| High availability web tier | **MIG + Load Balancer** | Auto-healing, multi-zone |
| Stateless containers | **Cloud Run** | Serverless, pay-per-use, fastest deploy |
| Kubernetes workloads | **GKE Autopilot** | Managed K8s, no node management |
| Simple web app | **App Engine Standard** | PaaS, zero config scaling |
| Event-driven functions | **Cloud Functions** | Sub-second invocations |

### 🎓 Learning Outcomes
- [ ] Choose the right compute service for different workloads
- [ ] Deploy auto-scaling, self-healing applications
- [ ] Configure load balancers for high availability
- [ ] Containerize and deploy apps

### 🔍 Job Roles Focus
- **Cloud Engineer:** All modules
- **DevOps Engineer:** Focus on containers, GKE, Cloud Build
- **SRE:** Deep dive on MIG, load balancing, monitoring

---

## 🎯 Track 3: Storage & Databases
**Duration:** 10-12 hours | **ACE Exam Weight:** 15%

Understand GCP's storage options and when to use each.

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **Cloud Storage Basics** | [section_6_cloud_storage.md](section_6_cloud_storage.md) | 90 min | Buckets, storage classes, versioning |
| **Storage Advanced** | [section_11_storage_advanced.md](section_11_storage_advanced.md) | 120 min | Lifecycle policies, Signed URLs, retention |
| **Persistent Disks** | [section_5_storage_basics.md](section_5_storage_basics.md) | 60 min | Zonal vs regional, snapshots |
| **Cloud SQL** | [section_10_cloud_sql.md](section_10_cloud_sql.md) | 120 min | HA setup, backups, read replicas |
| **Cloud Spanner & Bigtable** | [section_23_cloud_spanner_bigtable.md](section_23_cloud_spanner_bigtable.md) | 90 min | When to use each, scaling patterns |

### 📊 Storage Decision Table

| Data Type | Best Service | Why |
|-----------|-------------|-----|
| Object storage (images, backups) | **Cloud Storage** | Durable, cheap, global access |
| VM boot disk | **Persistent Disk** | High IOPS, snapshots |
| Relational database | **Cloud SQL** | Managed MySQL/Postgres |
| Global transactions | **Cloud Spanner** | 99.999% availability, global scale |
| Time-series / IoT | **Bigtable** | Millions of ops/sec, HBase compatible |
| NoSQL documents | **Firestore** | Real-time sync, mobile SDKs |

### 🎓 Learning Outcomes
- [ ] Select appropriate storage for different use cases
- [ ] Implement lifecycle policies for cost optimization
- [ ] Configure database high availability
- [ ] Manage backups and disaster recovery

---

## 🎯 Track 4: Networking & Security
**Duration:** 15-18 hours | **ACE Exam Weight:** 25%

Master VPC networking and implement enterprise security.

### Networking Modules

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **VPC Fundamentals** | [section_5_vpc_networking.md](section_5_vpc_networking.md) | 120 min | Subnets, routes, firewall rules |
| **Hybrid Connectivity** | [section_14_hybrid_connectivity.md](section_14_hybrid_connectivity.md) | 120 min | Cloud VPN, Cloud Interconnect |
| **DNS & CDN** | [section_13_dns_cdn.md](section_13_dns_cdn.md) | 90 min | Cloud DNS, Cloud CDN |
| **Network Security** | [section_24_network_security.md](section_24_network_security.md) | 90 min | Private Google Access, Cloud NAT |

### Security Modules

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **IAM Fundamentals** | [section_6_iam_identity.md](section_6_iam_identity.md) | 120 min | Roles, service accounts, policies |
| **Advanced IAM** | [section_17_advanced_iam.md](section_17_advanced_iam.md) | 90 min | Workload Identity, Conditions, Deny Policies |
| **KMS & Encryption** | [section_18_kms_encryption.md](section_18_kms_encryption.md) | 90 min | CMEK, envelope encryption, Cloud HSM |
| **Cloud Armor** | [section_25_cloud_armor.md](section_25_cloud_armor.md) | 60 min | WAF, DDoS protection |
| **Security Operations** | [section_20_security_operations.md](section_20_security_operations.md) | 90 min | Security Command Center, VPC Flow Logs |

### 🎓 Learning Outcomes
- [ ] Design secure VPC architectures
- [ ] Implement least-privilege IAM policies
- [ ] Configure hybrid cloud connectivity
- [ ] Encrypt data at rest and in transit

### 🔍 Job Roles Focus
- **Security Engineer:** All security modules + IAM deep dive
- **Network Engineer:** Focus on VPC, hybrid connectivity
- **Cloud Engineer:** Balanced focus across all modules

---

## 🎯 Track 5: Operations & Monitoring
**Duration:** 8-10 hours | **ACE Exam Weight:** 15%

Implement SRE practices and production monitoring.

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **Cloud Operations** | [section_22_cloud_ops.md](section_22_cloud_ops.md) | 120 min | Logging, Monitoring, Trace, Profiler |
| **Backup & DR** | [section_20_backup_dr.md](section_20_backup_dr.md) | 90 min | Snapshots, disaster recovery patterns |
| **SRE Operations** | [section_36_sre_ops.md](section_36_sre_ops.md) | 90 min | SLOs, error budgets, incident response |
| **FinOps** | [section_37_finops.md](section_37_finops.md) | 60 min | Cost optimization, billing analysis |

### 🎓 Learning Outcomes
- [ ] Create monitoring dashboards and alerts
- [ ] Implement log-based metrics
- [ ] Design disaster recovery strategies
- [ ] Optimize cloud costs

---

## 🎯 Track 6: Data & DevOps
**Duration:** 10-12 hours | **ACE Exam Weight:** 10%

Build data pipelines and CI/CD workflows.

### Data Modules

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **Pub/Sub** | [section_31_pubsub.md](section_31_pubsub.md) | 90 min | Messaging patterns, DLQ, exactly-once |
| **BigQuery** | [section_24_bigquery_data_warehousing.md](section_24_bigquery_data_warehousing.md) | 120 min | Partitioning, clustering, cost optimization |
| **Dataflow & Dataproc** | [section_32_dataflow_dataproc.md](section_32_dataflow_dataproc.md) | 90 min | Batch vs streaming, when to use each |

### DevOps Modules

| Module | File | Time | Key Topics |
|--------|------|------|------------|
| **Terraform/IaC** | [section_26_infrastructure_as_code_terraform.md](section_26_infrastructure_as_code_terraform.md) | 120 min | State management, modules, best practices |
| **Cloud Build CI/CD** | [section_27_cloud_build_ci_cd.md](section_27_cloud_build_ci_cd.md) | 90 min | Build triggers, deployment pipelines |

---

## 🎯 Track 7: Capstone Projects & Exam Prep
**Duration:** 12-15 hours | **Pass/Fail**

Apply everything you've learned in real-world projects.

### Capstone Projects

| Project | File | Time | Skills Practiced |
|---------|------|------|------------------|
| **Static Website + CDN** | [capstone_1_static_website.md](capstone_1_static_website.md) | 240 min | GCS, CDN, Load Balancer, DNS, SSL |
| **Serverless API** | [capstone_2_serverless_api.md](capstone_2_serverless_api.md) | 240 min | Cloud Run, Cloud SQL, Secret Manager, CI/CD |
| **Enterprise Network** | [capstone_3_enterprise_network.md](capstone_3_enterprise_network.md) | 180 min | VPC, subnets, firewall, IAM, logging |

### Mini-Projects & Practice

| Resource | File | Purpose |
|----------|------|---------|
| **Mini-Projects** | [mini_projects.md](mini_projects.md) | 5 quick portfolio projects |
| **Interview Prep** | [interview_question_bank.md](interview_question_bank.md) | 60+ questions with answers |
| **Interview Strategy** | [interview_guide.md](interview_guide.md) | How to ace GCP interviews |

### Exam Preparation

| Module | File | Time | Focus |
|--------|------|------|-------|
| **Mock Exam 1** | [section_43_mock_exam_1.md](section_43_mock_exam_1.md) | 120 min | 50 questions, timed |
| **Mock Exam 2** | [section_44_mock_exam_2.md](section_44_mock_exam_2.md) | 120 min | 50 questions, timed |
| **Exam Strategy** | [section_45_exam_strategy.md](section_45_exam_strategy.md) | 60 min | Tips, traps, time management |

---

## 🗺️ Recommended Learning Paths

### Path 1: Complete Beginner (8 weeks)
```
Week 1-2: Track 1 (Foundations)
Week 3-4: Track 2 (Compute) + Track 3 (Storage)
Week 5-6: Track 4 (Networking & Security)
Week 7: Track 5 (Operations) + Track 6 (Data/DevOps)
Week 8: Track 7 (Projects + Exam Prep)
```

### Path 2: Already Know AWS/Azure (4 weeks)
```
Week 1: Tracks 1-2 (focus on GCP differences)
Week 2: Tracks 3-4 (networking model is VERY different)
Week 3: Track 6 (IaC with Terraform) + Capstone
Week 4: Exam prep + Mock exams
```

### Path 3: Job-Focused (Pick Your Role)

**Cloud Engineer Track:**
> Tracks 1, 2, 4, 5 → Capstone 1 & 3 → Interview prep

**DevOps Engineer Track:**
> Tracks 1, 2, 6 → All mini-projects → Capstone 2 → Interview prep

**Data Engineer Track:**
> Tracks 1, 3, 6 (Data modules only) → BigQuery deep dive → Custom data project

---

## 📝 Study Tips

### Daily Routine
1. **Theory (30 min):** Read module content
2. **Hands-On Lab (60 min):** Follow CLI steps in YOUR project
3. **Quiz (15 min):** Test knowledge
4. **Review (15 min):** Note tricky concepts

### Weekly Milestones
- [ ] Complete one full track
- [ ] Build a mini-project
- [ ] Answer 10 interview questions out loud

### Pre-Exam Checklist
- [  ] Completed all 7 tracks
- [ ] Built 3 capstone projects
- [ ] Scored 80%+ on both mock exams
- [ ] Can explain 20+ interview questions
- [ ] Reviewed common exam traps

---

## 🎯 Success Metrics

You're ready for the ACE exam when:
- ✅ You can design a 3-tier architecture from scratch
- ✅ You've deployed at least 3 real projects
- ✅ You score 80%+ consistently on practice exams
- ✅ You can explain WHY you chose a service, not just WHAT it does
- ✅ You've troubleshot 10+ production-like scenarios

---

## 📚 Additional Resources

| Resource | File | When to Use |
|----------|------|-------------|
| **Production Checklists** | Each module | Before deploying to production |
| **Decision Tables** | Throughout modules | When choosing between services |
| **Troubleshooting Guides** | IAM, VPC, Compute | When things break |
| **Cost Calculators** | Billing module | Before provisioning resources |

---

**Last Updated:** 2026-01-21  
**Course Version:** 4.0 (Industry-Ready Edition)
