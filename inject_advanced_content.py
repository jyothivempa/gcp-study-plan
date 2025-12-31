import os

# Define the root content directory
CONTENT_DIR = r"d:\ultimateCode\gcp_study_plan\curriculum\content"

# Advanced content dictionary mapping Day Number to Markdown Content
advanced_content = {
    1: """
## 🚀 Next-Level: 2025 Exam Update
*   **Shift to Practical Skills:** The new ACE exam focuses less on memorizing limits and more on *how* to fix broken things.
*   **New Topics:** strong emphasis on **Workload Identity Federation** (replacing keys), **Artifact Registry** (replacing Container Registry), and **Cloud Run Jobs**.
""",
    2: """
## 🚀 Next-Level: Global vs Regional Design
*   **Pro Tip:** Always design for failure. If a Zone fails, your Regional MIG saves you. If a Region fails, your Global Load Balancer saves you.
*   **Organization Policies:** As an admin, use Organization Policies to *force* restrictions (e.g., "Restrict Domain Sharing" to prevent public buckets).
""",
    3: """
## 🚀 Next-Level: FinOps & Cost Control
*   **CUDs (Committed Use Discounts):** Know the difference between **Spend-based** (flexible) and **Resource-based** (specific hardware) CUDs.
*   **Billing Export:** The *first* thing you do in a new Org is export billing data to **BigQuery**. You can't analyze costs effectively in the console UI alone.
""",
    4: """
## 🚀 Next-Level: Advanced Compute Engine
*   **Spot VMs:** Save 60-91% cost. Ideal for stateless fault-tolerant workloads. *Caveat:* Google can reclaim them with a 30-second warning.
*   **Sole-Tenant Nodes:** Physical servers dedicated to you. Use for **BYOL** (Bring Your Own License) or strict compliance (HIPAA/Gov) requiring physical isolation.
""",
    5: """
## 🚀 Next-Level: VM Performance & Security
*   **Confidential VMs:** Encrypt data *in-use* (in RAM) using AMD SEV technologies.
*   **VM Manager:** Automated tool to manage OS patches (Patch management) and configuration (OS config) across a massive fleet of 1,000+ VMs.
""",
    6: """
## 🚀 Next-Level: Storage Optimization
*   **Performance:** For uploading terabytes of small files, use `gsutil -m cp` (multi-threaded) or `gcloud storage cp` (faster). For huge files, use **Composite Uploads**.
*   **Security:** Enforce **Uniform Bucket-Level Access** to disable old-school ACLs. Use **CMEK** (Customer Managed Encryption Keys) if you need to control the key rotation.
""",
    7: """
## 🚀 Next-Level: VPC Design Patterns
*   **Shared VPC:** Centralized control. Host Project holds the Network; Service Projects hold the VMs. *Use this for Enteprrises.*
*   **VPC Peering:** Decentralized connection. Two separate VPCs talk privately. *Caveat:* **NOT Transitive**. If A peers B, and B peers C, A cannot talk to C.
""",
    8: """
## 🚀 Next-Level: Hybrid Connectivity
*   **Cloud VPN:** Cheap, encrypted, over public internet. 3Gbps max per tunnel.
*   **Cloud Interconnect:** Expensive, physical cable. **Dedicated** (10/100 Gbps) direct to Google. **Partner** (via ISP) for lower speeds.
*   **Private Google Access:** Allows VMs *without* public IPs to reach Google APIs (Storage/BigQuery) internally.
""",
    10: """
## 🚀 Next-Level: Firewall Insights
*   **Firewall Rules Logging:** Turn this on to debug "Why can't I connect?". It logs every allowed/denied packet.
*   **Hierarchical Firewall Policies:** Define firewall rules at the **Organization** level (e.g., "Allow SSH from Corporate IP") that descend to all projects.
""",
    11: """
## 🚀 Next-Level: Advanced Load Balancing
*   **Global vs Regional:**
    *   **External HTTP(S) LB:** Global (Anycast IP). Stops DDoS at the edge (Cloud Armor).
    *   **Regional External LB:** Good for compliance (traffic stays in region).
*   **Private Service Connect (PSC):** The modern way to expose services privately across VPCs without Peering headaches.
""",
    12: """
## 🚀 Next-Level: IAM Security
*   **Workload Identity Federation (WIF):** The 2025 standard. allows AWS/Azure/GitHub to login to GCP *without* a Service Account Key. Safe & Secure.
*   **ABAC (Attribute Based Access Control):** Using **IAM Conditions**. "Grant Access IF `request.time < 17:00` AND `resource.name.startsWith('dev')`".
""",
    13: """
## 🚀 Next-Level: Service Account Security
*   **Short-Lived Credentials:** Instead of downloading a key (valid for 10 years), use `gcloud auth print-access-token` (valid for 1 hour).
*   **Impersonation:** Human users should "impersonate" a Service Account for risky tasks rather than downloading its keys.
""",
    14: """
## 🚀 Next-Level: Observability Strategy
*   **Cloud Trace:** Mandatory for **Microservices**. Visualizes the "Waterfall" of latency between Service A -> Service B -> Service C.
*   **Cloud Profiler:** The "Cost Cutter". It tells you: "Your Java function spends 80% of CPU time on String Concatenation."
""",
    17: """
## 🚀 Next-Level: Cloud Run Deep Dive
*   **Jobs vs Services:**
    *   **Service:** Listens for HTTP requests (Waiters). scales to zero.
    *   **Job:** doing work and quitting (Janitors). Video rendering, database migration.
*   **Direct VPC Egress:** New feature allowing Cloud Run to talk to private VPC IPs directly (faster/cheaper than Serverless VP Connector).
""",
    18: """
## 🚀 Next-Level: GKE Advanced
*   **GKE Autopilot:** The default for new clusters. Google handles nodes, security, patches. You just send Pods.
*   **Multi-Cluster Ingress (MCI):** One Load Balancer fronting GKE clusters in US, EU, and Asia. True Global Scale.
""",
    19: """
## 🚀 Next-Level: Database Decision 2025
*   **AlloyDB:** Identifying the Gap. Cloud SQL is great, but AlloyDB is **4x faster for transactions** and **100x faster for analytics** than standard Postgres. Use for high-end enterprise apps.
*   **BMS (Bare Metal Solution):** For when you need to lift-and-shift Oracle workloads that are too stubborn for VMs.
""",
    23: """
## 🚀 Next-Level: Spanner & Bigtable Internals
*   **Spanner TrueTime:** Uses Atomic clocks to guarantee consistency across the globe. No other database does this.
*   **Bigtable Hotspotting:** The #1 exam question. If you use sequential keys (User-1, User-2), all traffic hits one node. *Solution:* Hash/Reverse the keys.
""",
    24: """
## 🚀 Next-Level: BigQuery Optimization
*   **Partitioning:** Divide table by Date. "Scan only today's data". Drastically reduces cost.
*   **Clustering:** Sort data within partitions (e.g., by UserID). "Find User-123 in today's data".
*   **BigQuery Omni:** Analyze data sitting in AWS S3 or Azure Blob *without moving it*.
""",
    26: """
## 🚀 Next-Level: Terraform in Production
*   **Remote State:** NEVER store `terraform.tfstate` on your laptop. Store it in a **GCS Bucket** with **Object Versioning** enabled (to rollback if state corrupts).
*   **Modules:** Don't copy-paste. Create a "Company Standard VM" module and reuse it.
""",
    28: """
## 🚀 Next-Level: Security Command Center (SCC)
*   **Standard vs Premium:**
    *   **Standard:** Free. Finds basic misconfigs (Public Buckets, Firewall 0.0.0.0).
    *   **Premium:** Paid. Event Threat Detection (Crypto mining malware), Container Threat Detection.
"""
}

def inject_content():
    print("Starting Advanced Content Injection...")
    files_modified = 0
    
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md") and filename.startswith("section_"):
            
            # Extract Day Number from filename logic (section_X_...)
            try:
                parts = filename.split("_")
                day_num = int(parts[1])
            except ValueError:
                continue

            # Check if we have advanced content for this day
            if day_num in advanced_content:
                file_path = os.path.join(CONTENT_DIR, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Basic check to avoid double injection
                if "Next-Level:" in content:
                    print(f"Skipping Day {day_num} (Already Injected)")
                    continue

                new_block = advanced_content[day_num]

                # Inject BEFORE the Flashcards or at the end
                if "<!-- FLASHCARDS" in content:
                    new_content = content.replace("<!-- FLASHCARDS", f"{new_block}\n\n<!-- FLASHCARDS")
                else:
                    new_content = content + "\n" + new_block

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                print(f"[Done] Injected Day {day_num}")
                files_modified += 1

    print(f"\nCompleted. Modified {files_modified} files.")

if __name__ == "__main__":
    inject_content()
