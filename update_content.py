import os
import re

CONTENT_DIR = r"d:\GCP\gcp-study-plan\curriculum\content"

# Map file to meaningful module name (Day Removal)
MODULE_MAP = {
    "section_1_cloud_foundations.md": "Module 1: Cloud Foundations",
    "section_2_gcp_projects_billing.md": "Module 2: Projects & Billing",
    "section_2_gcp_structure.md": "Module 3: Resource Hierarchy",
    "section_3_gcp_billing.md": "Module 4: Billing Management",
    "section_4_compute_engine.md": "Module 5: Compute Engine Basics",
    "section_5_vpc_networking.md": "Module 6: VPC Networking",
    "section_6_iam_identity.md": "Module 7: IAM & Identity",
    "section_6_cloud_storage.md": "Module 8: Cloud Storage",
    "section_9_load_balancing.md": "Module 9: Load Balancing",
    "section_10_cloud_sql.md": "Module 10: Cloud SQL Database",
    "section_13_cloud_run.md": "Module 11: Cloud Run Serverless",
    "section_15_containers.md": "Module 12: Containers & GKE",
    "section_22_cloud_ops.md": "Module 13: Cloud Operations",
    "section_24_bigquery_data_warehousing.md": "Module 14: BigQuery Analytics",
    "section_26_infrastructure_as_code_terraform.md": "Module 15: Terraform IaC"
}

def update_modules():
    print("Starting module updates...")
    
    for filename in os.listdir(CONTENT_DIR):
        if not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(CONTENT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        
        # 1. Rename "Day X" to "Module X" in Title
        # Look for "# Day X:" or "# Section X:"
        new_title = None
        if filename in MODULE_MAP:
            new_title = f"# {MODULE_MAP[filename]}"
            content = re.sub(r"^# .*(Day|Section) \d+.*", new_title, content, count=1, flags=re.MULTILINE)

        # 2. Update Time Estimates
        # Replace "Est. Time: 45 mins" blocks
        new_time_block = """
> **⏱️ Time Estimate:** 90-120 mins
> *   Theory: 30 mins
> *   Lab: 60 mins
> *   Quiz/Review: 30 mins
"""
        content = re.sub(r"> \*\*Est\. Time:\*\* .*mins", new_time_block.strip(), content)

        # 3. Inject Navigation (if core module)
        if filename in MODULE_MAP:
             nav_block = """
> **🎯 Objectives:**
> *   Master core concepts
> *   Build hands-on resources
> *   Pass the ACE exam scenarios

| 📚 Concepts | 🧪 Lab | 📝 Quiz | 💼 Interview |
|---|---|---|---|
| [Jump to Theory](#concepts) | [Jump to Lab](#hands-on-lab) | [Jump to Quiz](#knowledge-check) | [Jump to Interview](#interview-questions) |

---
"""
             # Insert after title (find first # Header and newline)
             lines = content.splitlines()
             for i, line in enumerate(lines):
                 if line.startswith("# "):
                     lines.insert(i+1, nav_block)
                     break
             content = "\n".join(lines)

        # 4. Mandatory Lab Cleanup Footer
        cleanup_block = """
---

### 🗑️ Lab Cleanup (Mandatory)

> **⚠️ Critical:** Delete resources to avoid unecessary billing!

1.  **Delete Project:** (Fastest way)
    ```bash
    gcloud projects delete $PROJECT_ID
    ```
2.  **Or Delete Resources Individually:**
    ```bash
    # Example commands (verify before running)
    gcloud compute instances delete [INSTANCE_NAME] --quiet
    gcloud storage rm -r gs://[BUCKET_NAME]
    ```
"""
        # Append if not present and it's a "section_" file
        if filename.startswith("section_") and "Lab Cleanup" not in content:
            content += cleanup_block

        # 5. Inject Decision Tables (Specific Modules)
        if filename == "section_10_cloud_sql.md" and "Decision Table" not in content:
            table_block = """
### 📊 Decision Table: Cloud SQL vs The Rest
| Feature | **Cloud SQL** | **Cloud Spanner** | **BigQuery** | **Firestore** |
|:---|:---|:---|:---|:---|
| **Best For** | Traditional relational apps (CRM, ERP) | Global scale, 99.999% uptime | Analytics | Mobile apps |
| **Scale** | Vertical (bigger machine) | Horizontal (more nodes) | Peta-scale | Auto-scaling |
"""
            # Insert before "## Hands-on Lab"
            content = content.replace("## 🛠️ Hands-On Lab", f"{table_block}\n\n## 🛠️ Hands-On Lab")

        if filename == "section_31_pubsub.md" and "Decision Table" not in content:
            table_block = """
### 📊 Decision Table: Pub/Sub vs Cloud Tasks
| Feature | **Pub/Sub** | **Cloud Tasks** |
|:---|:---|:---|
| **Delivery** | Message Streaming (Many-to-Many) | Task Queues (One-to-One) |
| **Pattern** | Async Event Ingestion | Async Service Invocation |
| **Rate Limit** | No (Fan-out) | Yes (Throttling) |
| **Ordering** | Not guaranteed (unless enabled) | Guaranteed |
"""
            content = content.replace("## 🛠️ Hands-On Lab", f"{table_block}\n\n## 🛠️ Hands-On Lab")

        # 6. Replace Quizzes (Regex Match for "Knowledge Check" block)
        # Compute Engine Quiz
        if filename == "section_4_compute_engine.md":
            new_quiz = """## 📝 7. Knowledge Check

### Level 1: Beginner (Recall)

1.  **Which Compute Engine machine family is best for cost-effective batch processing?**
    *   A. E2
    *   B. C2
    *   C. **Spot VMs** ✅
    *   D. N2

2.  **How do you enable a VM to automatically restart on a different host after a hardware failure?**
    *   A. Enable "Preemptibility"
    *   B. **Set "On Host Maintenance" to "Migrate" and "Automatic Restart" to "On"** ✅
    *   C. Use a Shielded VM
    *   D. Use a Local SSD

### Level 2: ACE Exam (Scenario)

3.  **You need to deploy a web application that requires high availability across three zones. The application is stateless. Which configuration should you choose?**
    *   A. Three standalone VMs in different zones with a DNS round-robin.
    *   B. **A Regional Managed Instance Group (MIG) with an HTTP Load Balancer.** ✅
    *   C. A Zonal MIG with a Network Load Balancer.
    *   D. An Unmanaged Instance Group with a Regional external IP.

4.  **A developer wants to SSH into a VM that has no external IP address. The VM is in a private subnet. What is the most secure way to allow access?**
    *   A. Create a firewall rule allowing 0.0.0.0/0 on port 22.
    *   B. Assign a public IP to the VM temporarily.
    *   C. **Use Identity-Aware Proxy (IAP) TCP forwarding.** ✅
    *   D. Set up a VPN connection just for this single user.

### Level 3: Interview (Reasoning)

5.  **Interviewer: "Why would you choose a Custom Machine Type over a Predefined one?"**
    *   **Strong Answer:** "I would choose a Custom Machine Type when my workload's resource ratio doesn't match predefined types—for example, a memory-intensive cache that needs 64GB RAM but only 2 vCPUs. Using a standard `n2-highmem-8` would force me to pay for 6 extra vCPUs I don't need. Custom types save money by right-sizing resources to the exact application profile."
"""
            # Replace specifically the old Knowledge Check block
            content = re.sub(r"## 📝.*Knowledge Check[\s\S]*?<!-- QUIZ_END -->", new_quiz + "\n<!-- QUIZ_END -->", content)

        # VPC Networking Quiz
        if filename == "section_5_vpc_networking.md":
            new_quiz = """## 📝 8. Knowledge Check

### Level 1: Beginner (Recall)

1.  **What is the scope of a VPC network in GCP?**
    *   A. Zonal
    *   B. Regional
    *   C. **Global** ✅
    *   D. Multi-Cloud

2.  **Which GCP resource creates a private connection between your VPC and on-premises network?**
    *   A. Cloud NAT
    *   B. **Cloud VPN** ✅
    *   C. VPC Peering
    *   D. Cloud CDN

### Level 2: ACE Exam (Scenario)

3.  **You have created a new custom VPC. You create a subnet in `us-central1`. You try to create a VM in `us-east1` but the subnet dropdown is empty. Why?**
    *   A. You reached your quota for subnets.
    *   B. **Subnets are regional. You must create a subnet in `us-east1` first.** ✅
    *   C. The VPC needs to be in "Auto Mode" to support multiple regions.
    *   D. You need to enable "Global Routing" on the VPC.

4.  **You need to allow a web server in a private subnet to download patches from the internet. The server must NOT be accessible from the internet. What should you configure?**
    *   A. Assign an External IP to the VM.
    *   B. Configure a Proxy VM.
    *   C. **Configure Cloud NAT.** ✅
    *   D. Enable Private Google Access.

### Level 3: Interview (Reasoning)

5.  **Interviewer: "Explain the difference between VPC Peering and Shared VPC. When would you use each?"**
    *   **Strong Answer:** "VPC Peering connects two independent VPCs allowing them to talk via private IPs. It's decentralized and good for connecting different organizations (e.g., SaaS provider to customer). Shared VPC is centralized—it allows multiple service projects to consume a single network managed by a host project. I'd use Shared VPC for my company's internal structure to enforce central firewall/security policies while letting devs manage their own resources."
"""
            content = re.sub(r"## 📝.*Knowledge Check[\s\S]*?<!-- QUIZ_END -->", new_quiz + "\n<!-- QUIZ_END -->", content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Updated {filename}")
        else:
            print(f"Skipped {filename} (no changes needed)")

if __name__ == "__main__":
    update_modules()
