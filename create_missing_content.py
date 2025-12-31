
import os

base_path = r"d:\ultimateCode\gcp_study_plan\curriculum\content"

new_content = {
    # DAY 13: Cloud DNS & CDN
    "section_13_dns_cdn.md": """# SECTION 13: Cloud DNS & Cloud CDN

## 1️⃣ Plain-English Explanation
*   **Cloud DNS:** It's the "Phonebook" of the internet. It translates "google.com" to "142.250.x.x". In GCP, it's 100% SLA (never goes down).
*   **Cloud CDN (Content Delivery Network):** It's like having a mini-store in every city. Instead of fetching images from your warehouse in New York every time, you store copies (cache) in London, Tokyo, and Mumbai. Users download fast.

## 2️⃣ Cloud DNS Key Concepts
*   **Managed Zones:** Where you store your records (A, CNAME, TXT).
*   **Public Zones:** Visible to internet.
*   **Private Zones:** Only visible to your VPC. Used for internal services (e.g., `db.internal.corp`).
*   **Split Horizon:** Using the *same* domain name (myapp.com) but returning a private IP for internal users and public IP for external users.

## 3️⃣ Cloud CDN
*   **Works with:** Global HTTP(S) Load Balancer.
*   **Cache Hit:** Content served from edge (Fast!).
*   **Cache Miss:** Content fetched from backend (Slower).
*   **Invalidation:** Manually clearing the cache (e.g., you updated `logo.png` but users still see old one).

## 4️⃣ Exam Scenarios & Traps 🚨
*   **Trap:** "Users are complaining about stale content." -> **Invalidate the cache.**
*   **Trap:** "Need internal DNS names for VMs." -> **Private Managed Zone.**
*   **Trap:** "100% Availability for DNS." -> **Cloud DNS** is the only service with 100% SLA.

## 7️⃣ Checkpoint Questions
1.  **True or False: Cloud CDN can be used with a Regional Load Balancer.**
    *   *Answer: False. Requires Global HTTP(S) Load Balancer.*
2.  **Which DNS record type points a domain to an IP address?**
    *   *Answer: A Record.*
""",

    # DAY 14: Hybrid Connectivity
    "section_14_hybrid_connectivity.md": """# SECTION 14: Hybrid Connectivity (VPN vs Interconnect)

## 1️⃣ Valid Options
Connecting your On-Premises Data Center to Google Cloud.

| Feature | Cloud VPN | Dedicated Interconnect | Partner Interconnect |
| :--- | :--- | :--- | :--- |
| **Speed** | Up to 3 Gbps (HA VPN) | 10 Gbps or 100 Gbps | 50 Mbps - 10 Gbps |
| **Medium** | Public Internet (Encrypted) | Physical Cable (Direct) | Service Provider (ISP) |
| **SLA** | 99.99% (HA) | 99.99% (Requires 4 circuits) | Variable |
| **Use Case** | Cheap, Fast Setup, Backup | Massive Data, Compliance, Low Latency | No Google POP nearby |

## 2️⃣ HA VPN (High Availability)
*   Uses **BGP** (Border Gateway Protocol) to dynamically route traffic.
*   Requires 2 Tunnels for 99.99% SLA.

## 3️⃣ Direct Peering vs Interconnect
*   **Interconnect:** Connects to *your* Private VPC IPs (RFC1918).
*   **Peering:** Connects to *Google's* Public IPs (YouTube, Gmail). DOES NOT give access to your VPC directly.

## 7️⃣ Checkpoint Questions
1.  **Which requires a physical cable connection?**
    *   *Answer: Interconnect.*
2.  **What protocol is used for dynamic routing?**
    *   *Answer: BGP.*
""",

    # DAY 17: Advanced IAM (Workload Identity)
    "section_17_advanced_iam.md": """# SECTION 17: Advanced IAM: Workload Identity & Conditions

## 1️⃣ Workload Identity (The Game Changer)
*   **Old Way:** Download JSON Keys for Service Accounts. (Insecure, Keys leak).
*   **New Way (Workload Identity):** Let GKE or External Clouds (AWS/Azure) impersonate a Google Service Account *without* keys.
*   **How:** It maps a Kubernetes Service Account (KSA) to a Google Service Account (GSA).
*   **Benefit:** Zero key management.

## 2️⃣ IAM Conditions
*   "You are an Editor, BUT ONLY..."
    *   ...on weekdays 9-5.
    *   ...if connecting from Corporate IP.
    *   ...for resources with tag `env:dev`.
*   **Used for:** Temporary access, geographic restrictions.

## 7️⃣ Checkpoint Questions
1.  **What is the secure replacement for exporting JSON keys in GKE?**
    *   *Answer: Workload Identity.*
""",

    # DAY 18: KMS & Encryption
    "section_18_kms_encryption.md": """# SECTION 18: Data Protection & KMS

## 1️⃣ Encryption Levels
1.  **Default Encryption:** Google manages everything. (Standard).
2.  **CMEK (Customer-Managed Encryption Keys):** You manage the key in Cloud KMS. Google uses it. You can rotate/revoke it.
3.  **CSEK (Customer-Supplied Encryption Keys):** You keep the key on your laptop. Google *never* sees the key. If you lose it, data is gone forever.

## 2️⃣ Cloud KMS (Key Management Service)
*   **Key Ring:** Authorization boundary (Grant access to a Ring, not individual keys).
*   **Rotation:** Auto-rotate keys every 90 days.
*   **HSM:** Hardware Security Module (Physical chip) for compliance (FIPS 140-2 Level 3).

## 7️⃣ Checkpoint Questions
1.  **If you lose your CSEK key, can Google recover the data?**
    *   *Answer: No. It is cryptographically shredded.*
""",

    # DAY 20: Security Operations
    "section_20_security_operations.md": """# SECTION 20: Security Command Center & DLP

## 1️⃣ Security Command Center (SCC)
*   The "Dashboard" for security.
*   **Asset Discovery:** "What resources do I have?"
*   **Threat Detection:** "Is someone bitcoin mining on my VM?"
*   **Vulnerability Scan:** "Is my firewall open to 0.0.0.0?"

## 2️⃣ Cloud DLP (Data Loss Prevention)
*   Scans data for **PII** (Credit Cards, SSN, Emails).
*   **Actions:**
    *   **Redact:** Black out the info.
    *   **Mask:** Replace with `###-##-####`.
    *   **Tokenize:** Replace with a reversible token.

## 7️⃣ Checkpoint Questions
1.  **Which tool scans your storage buckets for Credit Card numbers?**
    *   *Answer: Cloud DLP.*
""",

    # DAY 24: Cloud Functions & Eventarc
    "section_24_functions_eventarc.md": """# SECTION 24: Cloud Functions & Eventarc

## 1️⃣ Cloud Functions (Gen 2)
*   **FaaS (Function as a Service):** Upload Python/NodeJS code. Google runs it.
*   **Trigger types:**
    *   **HTTP:** Webhook.
    *   **Background (Eventarc):** "File uploaded to GCS", "Pub/Sub message received".

## 2️⃣ Eventarc
*   The glue between services.
*   **Standardized:** Uses CloudEvents format.
*   **Example:** User uploads image -> Eventarc detects -> Triggers Function -> Resizes image.

## 7️⃣ Checkpoint Questions
1.  **Cloud Functions Gen 2 is built on top of which service?**
    *   *Answer: Cloud Run.*
""",
    
    # DAY 26: Advanced GKE
    "section_26_gke_advanced.md": """# SECTION 26: Advanced GKE networking & Security

## 1️⃣ Private Clusters
*   **Private Nodes:** Nodes have only Internal IPs.
*   **Private Endpoint:** Master API is private.
*   **Access:** Use a Bastion Host or VPN to reach kubectl.

## 2️⃣ Network Policies
*   The "Firewall" inside Kubernetes.
*   Controls which Pods can talk to which Pods.
*   *Default:* All Pods can talk to All Pods (Open).

## 3️⃣ Binary Authorization
*   Ensures only "Trusted Images" are deployed.
*   "This container was scanned and signed by QA. It is safe."

## 7️⃣ Checkpoint Questions
1.  **How do you restrict pod-to-pod communication?**
    *   *Answer: Network Policies.*
""",

    # DAY 32: Dataflow vs Dataproc
    "section_32_dataflow_dataproc.md": """# SECTION 32: Dataflow vs Dataproc

## 1️⃣ The Great Debate
| Feature | Dataflow | Dataproc |
| :--- | :--- | :--- |
| **Technology** | Apache Beam | Apache Spark / Hadoop |
| **Type** | Serverless (No Ops) | Managed Cluster (VMs) |
| **Use Case** | New Pipelines, Streaming | Migrating existing Hadoop/Spark jobs |
| **Scaling** | Per-item (Smooth) | Per-cluster (Step) |

## 2️⃣ Dataflow Features
*   **Streaming:** Exactly-once processing.
*   **Templates:** Create a job once, let non-coders run it via Console.

## 7️⃣ Checkpoint Questions
1.  **You have existing Spark jobs on-prem. Migration path?**
    *   *Answer: Dataproc.*
""",

    # DAY 34: Vertex AI
    "section_34_vertex_ai.md": """# SECTION 34: Vertex AI Basics

## 1️⃣ What is Vertex AI?
*   Unified platform for ML. Replaces "AI Platform".

## 2️⃣ AutoML vs Custom Training
*   **AutoML:** "Here is my data (CSV/Images). Train a model for me." (No Code).
*   **Custom Training:** "Here is my TensorFlow/PyTorch code. Run it on your GPUs."

## 3️⃣ Feature Store
*   Share ML features between teams so you don't re-calculate them.

## 7️⃣ Checkpoint Questions
1.  **Which tool requires NO coding knowledge to build a model?**
    *   *Answer: AutoML.*
""",

    # DAY 35: DB Migration
    "section_35_db_migration.md": """# SECTION 35: Database Migration Strategies

## 1️⃣ Database Migration Service (DMS)
*   **Supported:** MySQL, PostgreSQL, SQL Server, Oracle.
*   **Target:** Cloud SQL or AlloyDB.
*   **Method:** Continuous replication (Change Data Capture) for minimal downtime.

## 2️⃣ BigQuery Transfer Service
*   Moves data from SaaS (Salesforce, Google Ads) or S3/Azure Blob into BigQuery.

## 7️⃣ Checkpoint Questions
1.  **Best tool to migrate AWS RDS MySQL to Cloud SQL?**
    *   *Answer: Database Migration Service (DMS).*
""",

    # DAY 36: SRE & Ops
    "section_36_sre_ops.md": """# SECTION 36: SRE Principles

## 1️⃣ SLI vs SLO vs SLA
*   **SLI (Indicator):** "Latency is 200ms". (The Reality).
*   **SLO (Objective):** "Latency *should* be < 300ms 99% of time". (The Internal Goal).
*   **SLA (Agreement):** "If Latency is > 500ms, we pay you back". (The Contract).

## 2️⃣ Error Budget
*   Allowed failure.
*   If you have 99.9% SLO, you have 0.1% Error Budget.
*   **Burn Rate:** How fast you are using up your budget.

## 7️⃣ Checkpoint Questions
1.  **Which one is legally binding?**
    *   *Answer: SLA.*
""",
    
     # DAY 37: FinOps
    "section_37_finops.md": """# SECTION 37: Cost Management (FinOps)

## 1️⃣ Tools
*   **Budgets:** Alerts (Email/PubSub) when spend hits 50%, 90%.
*   **Quotas:** Hard limits to prevent "Runaway Bill" (e.g., Max 100 CPUs).
*   **Recommendations AI:** "You are using 10% CPU. Downsize this VM."

## 2️⃣ BigQuery Pricing
*   **On-Demand:** Pay per TB scanned (~$5).
*   **Capacity (Slots):** Flat rate monthly.

## 7️⃣ Checkpoint Questions
1.  **How do you prevent a developer from spinning up High-GPU instances?**
    *   *Answer: Set a Quota.*
"""
}

def create_files():
    for filename, content in new_content.items():
        full_path = os.path.join(base_path, filename)
        if not os.path.exists(full_path):
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created {filename}")
        else:
            print(f"Skipped {filename} (Exists)")

if __name__ == "__main__":
    create_files()
