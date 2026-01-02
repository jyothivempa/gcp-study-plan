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
| **11** | **VPC Deep Dive** | Shared VPC (central control) vs VPC Peering (decentralized). |
| **12** | **App Engine** | PaaS. Standard (Scale to 0) vs Flexible (Docker). Traffic Splitting. |
| **13** | **Cloud Run** | Serverless Containers. Portable. Best for modern microservices. |

---

## dart 2. Exam Focus Areas

### Critical Concepts for ACE Exam

#### Managed Instance Groups (MIGs)
- **Stateless (Cattle):** VMs can be deleted/recreated at any time.
- **Auto-healing:** Replaces unhealthy VMs automatically (requires Health Check).
- **Auto-scaling:** Scales based on CPU, Load Balancing Capacity, or Custom Metrics.
- **Regional vs Zonal:** Regional MIGs survive zone failures (HA).

**Exam Tip:** "VMs need to process distinct tasks from a queue and shut down" → Use MIG with Scaling based on Pub/Sub queue depth.

#### Load Balancing Tree
Quick decision guide for the exam:
1. **HTTP/HTTPS Traffic?** → **External HTTP(S) LB** (Global, Layer 7)
2. **TCP/UDP (Non-HTTP)?** → **Network Load Balancer** (Regional, Layer 4)
3. **Internal Only?** → **Internal TCP/UDP LB** (for internal apps)
4. **SSL Offloading?** → **SSL Proxy LB**

**Exam Tip:** If the question mentions "Global" and "Single Anycast IP", think HTTP(S) Global LB.

#### Cloud SQL High Availability
- **HA configuration:** Active instance (Zone A) + Standby instance (Zone B).
- **Read Replicas:** Scale READ traffic only. Does NOT provide failover by default (unless promoted).
- **Backups:** Automated vs On-demand. Point-in-time recovery requires binary logging.

**Exam Trap:** "Need to handle more write traffic?" → Cloud SQL cannot horizontally scale writes (easily). Vertical scale (bigger machine) or migrate to Spanner for massive write scale.

#### Serverless Showdown: App Engine vs Cloud Run vs Functions

| Feature | App Engine Standard | App Engine Flex | Cloud Run | Cloud Functions |
| :--- | :--- | :--- | :--- | :--- |
| **Code** | Language Specific (Py, Java, Go) | Docker Container | Docker Container | Small Code Snippets |
| **Startup** | Seconds (Fast) | Minutes (Slow) | Seconds (Fast) | Seconds (Fast) |
| **Scale to 0** | Yes (Free tier) | No (Min 1 instance) | Yes | Yes |
| **Max Timeout** | 10 mins (HTTP) | 60 mins | 60 mins | 9 mins |

**Exam Tip:** "Deploy existing container" + "HTTP" → **Cloud Run**. "Legacy Java 8 app" -> **App Engine**.

---

## ⚠️ 3. Common Mistakes

### Mistake #1: Confusing HA with Read Replicas
**Wrong:** "I added a Read Replica for Disaster Recovery."  
**Right:** "I enabled High Availability (HA) for failover. I added Read Replicas to offload reporting queries."

### Mistake #2: Configuring the Wrong Load Balancer
**Wrong:** Using HTTP LB for a gaming UDP server.  
**Right:** Use Network Load Balancer (UDP supported).

### Mistake #3: Ignoring Health Checks
- If a firewall blocks the Health Check IP ranges (`130.211.0.0/22`, `35.191.0.0/16`), the LB considers ALL instances dead.
- **Result:** 502 Bad Gateway errors.

### Mistake #4: App Engine Flex Scaling
- People forget Flex CANNOT scale to zero. It always costs money for at least 1 VM.

---

## 🧪 4. Hands-On Review Lab

Build a scalable, load-balanced web service.

### Project: Auto-Healing Web Server Group

**Steps:**

1. **Create Instance Template**
   ```bash
   gcloud compute instance-templates create my-web-template \
     --tags=http-server,lb-health-check \
     --metadata=startup-script='#!/bin/bash
     apt-get update && apt-get install -y apache2
     echo "Web Server" > /var/www/html/index.html'
   ```

2. **Create Health Check**
   ```bash
   gcloud compute health-checks create-http my-health-check --port=80
   ```

3. **Create Managed Instance Group (Regional)**
   ```bash
   gcloud compute instance-groups managed create my-mig \
     --template=my-web-template \
     --size=2 \
     --region=us-central1 \
     --health-check=my-health-check \
     --initial-delay=300
   ```

4. **Set Firewall Rule (Allow LB Health Checks)**
   ```bash
   gcloud compute firewall-rules create allow-lb-health-check \
     --allow=tcp:80 \
     --source-ranges=130.211.0.0/22,35.191.0.0/16 \
     --target-tags=lb-health-check
   ```

5. **Verify Auto-Healing**
   - Go to Console. Delete one VM in the group.
   - Watch the MIG automatically recreate it!

---

## 📚 5. Study Tips for Week 3

- **Week 3 is Kubernetes (GKE).** It is often the hardest week for beginners.
- **Docker:** If you don't know Docker, spend 1 hour this weekend learning basic `Dockerfile` syntax.
- **YAML:** Love it or hate it, K8s runs on YAML. Be ready to read lots of indentation.

---

## 🏆 6. What's Next? Week 3!

Week 3 is **Kubernetes Week**.

*   **Docker & Containers:** Understanding the box.
*   **GKE (Google Kubernetes Engine):** The industry standard for container orchestration.
*   **Pods, Services, Deployments:** The K8s vocabulary.
*   **GKE Modes:** Standard vs Autopilot.

> **🎉 Great job! You are halfway to becoming a Cloud Engineer.**
