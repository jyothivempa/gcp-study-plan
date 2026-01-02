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

## 🎯 2. Exam Focus Areas

### Critical Concepts for ACE Exam

#### Cloud Models (IaaS, PaaS, SaaS)
- **IaaS** (Compute Engine): You manage OS, Apps, Runtime
- **PaaS** (App Engine, Cloud Run): Google manages OS, you deploy code
- **SaaS** (Gmail, Workspace): Google manages everything

**Exam Tip:** Questions will test if you know WHEN to use each model.

#### Resource Hierarchy
```
Organization
  └── Folders (optional)
      └── Projects (required)
          └── Resources (VMs, Buckets, etc.)
```

**Exam Tip:** IAM policies are inherited top-down. Organization policy = most restricted.

#### Compute Engine Essentials
- **Zones:** Independent failure domains (choose 3+ for HA)
- **Regions:** Geographic locations (choose closest to users)
- **Machine Types:**
  - General Purpose: E2, N2, N2D (most workloads)
  - Compute Optimized: C2, C2D (HPC, gaming)
  - Memory Optimized: M2, M1 (large in-memory databases)
  
**Exam Tip:** Know when to use Preemptible VMs (batch jobs) vs Spot VMs (FAULT-TOLERANT workloads).

#### Cloud Storage Classes

| Class | Use Case | Min Duration | Cost |
|-------|----------|--------------|------|
| **Standard** | Hot data, frequent access | None | $$$ |
| **Nearline** | Once/month access | 30 days | $$ |
| **Coldline** | Once/quarter access | 90 days | $ |
| **Archive** | Once/year access | 365 days | ¢ |

**Exam Tip:** Storage class is PER-OBJECT, not per-bucket. Use Object Lifecycle Policies to auto-downgrade.

#### VPC Networking
- **VPC = Global** across all regions
- **Subnets = Regional** within a VPC
- **Firewall Rules:**
  - Default: Deny ALL ingress, Allow ALL egress
  - Priority: Lower number = higher priority (0-65535)
  - Can target by Tags or Service Accounts

**Exam Tip:** Remember `0.0.0.0/0` = entire internet. Use CIDR carefully!

#### IAM Best Practices
1. **Primitive Roles** (Owner, Editor, Viewer) = TOO BROAD. Avoid!
2. **Predefined Roles** = Google-managed, granular
3. **Custom Roles** = Your own permissions (if predefined isn't enough)
4. **Service Accounts** = For applications, not humans

**Exam Formats:**
- "User needs to create VMs but NOT delete them" → Compute Instance Admin (v1)
- "Developer needs read-only bucket access" → Storage Object Viewer

---

## ⚠️ 3. Common Mistakes

### Mistake #1: Confusing Global vs Regional Resources
**Wrong:** "My VPC is in us-central1"  
**Right:** "My VPC is global. My subnet is in us-central1."

### Mistake #2: Using Primitive Roles
**Wrong:** Giving "Editor" role to everyone  
**Right:** Use predefined roles (e.g., `roles/compute.instanceAdmin.v1`)

### Mistake #3: Forgetting Storage Class Retrieval Costs
- Archive storage is CHEAP to store
- Archive is EXPENSIVE to retrieve
- **Exam Trap:** "Which is cheapest for rarely accessed data?" → Archive (but clarify if they'll retrieve often!)

### Mistake #4: Not Using Budgets
- Budgets are ALERTS, not limits
- Use Budget Actions to auto-disable billing (requires Cloud Functions)

### Mistake #5: Firewall Rule Priorities
- Priority 1000 (allow SSH) vs Priority 500 (deny all)
- **Lower number wins** → Priority 500 blocks SSH

---

## 🧪 4. Hands-On Review Lab

Complete this mini-project to solidify Week 1 concepts:

### Project: Deploy a Multi-Zone Web Application

**Scenario:** Create a highly available web server accessible from the internet.

**Steps:**

1. **Create VPC Network**
   ```bash
   gcloud compute networks create week1-vpc --subnet-mode=custom
   ```

2. **Create Subnet**
   ```bash
   gcloud compute networks subnets create week1-subnet \
     --network=week1-vpc \
     --region=us-central1 \
     --range=10.0.1.0/24
   ```

3. **Create Firewall Rule (Allow HTTP)**
   ```bash
   gcloud compute firewall-rules create allow-http \
     --network=week1-vpc \
     --allow=tcp:80 \
     --source-ranges=0.0.0.0/0 \
     --target-tags=web-server
   ```

4. **Create VM in Zone A**
   ```bash
   gcloud compute instances create web-vm-a \
     --zone=us-central1-a \
     --subnet=week1-subnet \
     --tags=web-server \
     --metadata=startup-script='#!/bin/bash
     apt-get update
     apt-get install -y nginx
     echo "Hello from Zone A" > /var/www/html/index.html'
   ```

5. **Create VM in Zone B (for HA)**
   ```bash
   gcloud compute instances create web-vm-b \
     --zone=us-central1-b \
     --subnet=week1-subnet \
     --tags=web-server \
     --metadata=startup-script='#!/bin/bash
     apt-get update
     apt-get install -y nginx
     echo "Hello from Zone B" > /var/www/html/index.html'
   ```

6. **Test**: Visit the External IPs of both VMs in your browser

7. **Clean Up**
   ```bash
   gcloud compute instances delete web-vm-a web-vm-b --zone=us-central1-a,us-central1-b
   gcloud compute firewall-rules delete allow-http
   gcloud compute networks subnets delete week1-subnet --region=us-central1
   gcloud compute networks delete week1-vpc
   ```

**What You Practiced:**
- ✅ Custom VPC and Subnet creation
- ✅ Firewall rules (ingress + target tags)
- ✅ Multi-zone deployment (HA)
- ✅ Startup scripts (automation)

---

## 📚 5. Study Tips for Week 2

### Recommended Study Pattern
- **15 min/day:** Review previous day's quiz
- **45 min/day:** Today's new content
- **30 min/day:** Hands-on lab

### Focus on Understanding, Not Memorizing
- Don't memorize every `gcloud` command
- DO understand WHEN to use each service
- Exam tests scenarios, not syntax

### Use the "Explain to a 5-Year-Old" Test
- Can you explain IAM in one sentence?
  - *"IAM decides WHO can do WHAT on which RESOURCES"*
- If you can't simplify it, you don't understand it yet.

---

## 🏆 6. What's Next? Week 2!

Week 2 gets serious. We move from "Basics" to "Management".

**Week 2 Preview:**
- **Day 8:** Managed Instance Groups (MIGs) - Auto-scaling your VMs
- **Day 9:** Load Balancing - Distributing traffic globally
- **Day 10:** Cloud SQL - Managed Databases
- **Day 11:** VPC Deep Dive - Peering, Shared VPCs, Private Google Access
- **Day 12:** App Engine - Fully managed PaaS
- **Day 13:** Cloud Run - Serverless containers
- **Day 14:** Week 2 Review

**Goal for Week 2:** Master **MANAGED services**. Less infrastructure babysitting, more building.

> **🎉 Take a break! You earned it.**

---

## 💡 Pro Tips

1. **Create a 1-page "cheat sheet"** for Week 1 concepts
2. **Join the GCP Community** on Reddit (r/googlecloud) or Discord
3. **Set up billing alerts** BEFORE Week 2 (seriously!)
4. **Take screenshots** of your labs for your portfolio

**You're 15% done with the course. Keep momentum! 🚀**
