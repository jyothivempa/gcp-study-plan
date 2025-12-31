import os

ARTIFACT_DIR = r"d:\ultimateCode\gcp_study_plan\curriculum\content"

flashcard_data = {
    "section_1_cloud_foundations.md": [
        {"term": "Cloud Computing", "def": "On-demand delivery of compute, storage, applications via the internet. Pay-as-you-go."},
        {"term": "CapEx", "def": "Capital Expenditure. Upfront cost for physical hardware (Data Centers)."},
        {"term": "OpEx", "def": "Operational Expenditure. Ongoing cost for services (Cloud). Pay for what you use."},
        {"term": "TCO", "def": "Total Cost of Ownership. Hidden costs (AC, Security, Staff) + Hardware."},
        {"term": "GCP", "def": "Google Cloud Platform. A suite of cloud services hosted on Google's infrastructure."}
    ],
    "section_2_gcp_structure.md": [
        {"term": "Region", "def": "Specific geographical location (e.g., us-central1). Composed of Zones."},
        {"term": "Zone", "def": "Deplyment area within a region (e.g., us-central1-a). Isolated from failures in other zones."},
        {"term": "Project", "def": "Base-level organizing entity. Contains resources, billing, and permissions."},
        {"term": "Folder", "def": "Grouping mechanism for Projects. Useful for departments/teams."},
        {"term": "Organization", "def": "Root node. Represents the company. Contains Folders and Projects."}
    ],
    "section_3_gcp_billing.md": [
        {"term": "Billing Account", "def": "Pays for GCP usage. Linked to a Credit Card or Invoice."},
        {"term": "Budget", "def": "Set limits on spending. Sends alerts but DOES NOT stop services."},
        {"term": "Alerts", "def": "Notifications (Email/SMS) when spending passes a threshold (e.g., 50%, 90%)."},
        {"term": "Label", "def": "Key-Value pair to organize resources (e.g., env:prod). Helps in billing reports."},
        {"term": "Free Tier", "def": "Always-free usage limits for certain products (e.g., e2-micro instance)."}
    ],
    "section_4_compute_engine.md": [
        {"term": "Compute Engine", "def": "IaaS. Virtual Machines running on Google's infrastructure."},
        {"term": "Machine Type", "def": "Preset combination of CPU and RAM (e.g., e2-medium, n1-standard-1)."},
        {"term": "Preemptible VM", "def": "Short-lived, cheap VM (up to 80% off). Google can stop it anytime."},
        {"term": "Sole Tenant", "def": "Physical server dedicated to your project. Compliance/Licensing needs."},
        {"term": "SSH", "def": "Secure Shell. Protocol to log into a remote Linux machine."}
    ],
    "section_5_storage_basics.md": [
        {"term": "Block Storage", "def": "Like a hard drive. Good for OS and databases. Expensive. (Persistent Disk)."},
        {"term": "Object Storage", "def": "Like Google Drive. Good for files/media. Infinite scale. (Cloud Storage)."},
        {"term": "File Storage", "def": "Network Attached Storage (NAS). Good for shared files. (Filestore)."},
        {"term": "Persistent Disk", "def": "Zonal block storage attached to a VM."},
        {"term": "Local SSD", "def": "Ephemeral, super-fast storage attached physically to the server. Data lost on stop."}
    ],
    "section_6_cloud_storage.md": [
        {"term": "Bucket", "def": "Container for objects. Globally unique name."},
        {"term": "Object", "def": "File stored in Cloud Storage. Immutable (cannot edit, only overwrite)."},
        {"term": "Standard Class", "def": "Hot data. Frequent access. Identifying pattern: Served directly to users."},
        {"term": "Nearline Class", "def": "Infrequent access (once a month). Backups/Documents."},
        {"term": "Coldline Class", "def": "Rare access (once a quarter). Disaster Recovery."}
    ],
    "section_7_week_1_review.md": [
        {"term": "Week 1 Goal", "def": "Foundation. Compute, Storage, and Billing."},
        {"term": "IaaS vs PaaS", "def": "IaaS = Renting Hardware (VMs). PaaS = Renting a Platform (App Engine)."},
        {"term": "Zone vs Region", "def": "Region = City. Zone = Building."},
        {"term": "Spot VM", "def": "Cheap (60-91% off) but can be preempted (stopped) by Google at any time."},
        {"term": "Budget Alert", "def": "Warning email only. Does NOT stop billing."}
    ],
    "section_8_vpc_basics.md": [
        {"term": "VPC", "def": "Virtual Private Cloud. Your private network in Google's cloud."},
        {"term": "subnet", "def": "A regional subdivision of a VPC (e.g., 10.0.1.0/24 in us-central1)."},
        {"term": "Global VPC", "def": "GCP VPCs are global resources, spanning all regions. Subnets are regional."},
        {"term": "Firewall Rule", "def": "Controls traffic to/from VM instances based on IP/Port/Tag."},
        {"term": "Internal IP", "def": "Private IP for communication inside the VPC."}
    ],
    "section_9_subnets_ip.md": [
        {"term": "CIDR Block", "def": "Classless Inter-Domain Routing. Defines IP range (e.g., /24 = 256 IPs)."},
        {"term": "Static IP", "def": "A permanent IP address that doesn't change on reboot."},
        {"term": "Ephemeral IP", "def": "Temporary IP assigned by default. Changes if you stop/start the VM."},
        {"term": "Private Google Access", "def": "Allows private VMs to reach Google APIs (Storage, BigQuery) without internet."},
        {"term": "Alien Range", "def": "IP ranges you can't use (restricted by RFC 1918)."}
    ],
    "section_10_firewall_rules.md": [
        {"term": "Ingress", "def": "Incoming traffic (Example: User visiting your website)."},
        {"term": "Egress", "def": "Outgoing traffic (Example: VM downloading an update)."},
        {"term": "Priority", "def": "Lower number beats Higher number (0-65535). 1000 overrides 65535."},
        {"term": "Implied Deny", "def": "By default, all Ingress is BLOCKED."},
        {"term": "Network Tag", "def": "Label attached to a VM to apply firewall rules (e.g., 'web-server')."}
    ],
    "section_11_load_balancing.md": [
        {"term": "Load Balancer", "def": "Distributes traffic across multiple VMs to prevent overloading."},
        {"term": "Global HTTP(S) LB", "def": "Layer 7 LB. Terminates SSL. Good for web apps."},
        {"term": "Network LB", "def": "Layer 4 LB. TCP/UDP traffic. Ultra low latency."},
        {"term": "Health Check", "def": "Pings instances to see if they are alive. Removes dead ones."},
        {"term": "Backend Service", "def": "The group of instances the LB sends traffic to."}
    ],
    "section_12_cloud_nat_routes.md": [
        {"term": "Cloud NAT", "def": "Allows private VMs to access the internet for updates without a public IP."},
        {"term": "Route", "def": "Rules telling traffic where to go (Next Hop)."},
        {"term": "Dynamic Routing", "def": "Uses Cloud Router & BGP to automatically learn routes."},
        {"term": "System Routes", "def": "Default routes Google creates (e.g., Default Internet Gateway)."},
        {"term": "Bastion Host", "def": "Jump server used to SSH into private VMs securely."}
    ],
    "section_12_iam_core.md": [
        {"term": "IAM", "def": "Identity and Access Management. Who can do what on which resource."},
        {"term": "Principal", "def": "The 'Who' (User, Group, Service Account)."},
        {"term": "Role", "def": "The 'What' (Collection of permissions)."},
        {"term": "Policy", "def": "Binding a Principal to a Role on a Resource."},
        {"term": "Least Privilege", "def": "Giving only the minimum expected permissions."}
    ],
    "section_13_service_accounts.md": [
        {"term": "Service Account", "def": "An identity for a machine/application, not a human."},
        {"term": "Key JSON", "def": "Credential file for Service Accounts. Keep secret!"},
        {"term": "Scopes", "def": "Legacy access method for VMs. Prefer IAM Roles."},
        {"term": "Default SA", "def": "Automatically created SA with Editor role (dangerous)."},
        {"term": "Workload Identity", "def": "Secure way for GKE/External apps to act as a Service Account."}
    ],
    "section_14_logging_monitoring.md": [
        {"term": "Cloud Logging", "def": "Stores and searches logs (text records of events)."},
        {"term": "Cloud Monitoring", "def": "Tracks metrics (CPU, Memory performance)."},
        {"term": "Metric", "def": "A numerical measurement (e.g., CPU Usage %)."},
        {"term": "Uptime Check", "def": "Pings your URL from around the world to check availability."},
        {"term": "Alert Policy", "def": "Rules to notify you when something breaks."}
    ],
    "section_15_cloud_shell.md": [
        {"term": "Cloud Shell", "def": "Free ephemeral Linux VM with gcloud pre-installed."},
        {"term": "gcloud", "def": "Command line tool for Google Cloud."},
        {"term": "gsutil", "def": "Command line tool for Cloud Storage (Legacy)."},
        {"term": "Home Directory", "def": "5GB persistent storage in Cloud Shell."},
        {"term": "Web Preview", "def": "Feature to preview web apps running on port 8080 in Cloud Shell."}
    ],
    "section_16_app_engine.md": [
        {"term": "App Engine", "def": "PaaS. Code-first platform. Standard or Flexible env."},
        {"term": "Standard Env", "def": "Sandboxed, fast scaling (to zero), specific languages."},
        {"term": "Flexible Env", "def": "Docker-based, runs on VMs, any language, slower start."},
        {"term": "Traffic Splitting", "def": "A/B Testing. Send 10% traffic to V2, 90% to V1."},
        {"term": "dispatch.yaml", "def": "Routing rules for microservices in App Engine."}
    ],
    "section_17_cloud_run.md": [
        {"term": "Cloud Run", "def": "Serverless Container platform. Scale to zero. Any language."},
        {"term": "Concurrency", "def": "Handling multiple requests per container instance (Saving money)."},
        {"term": "Revision", "def": "Immutable snapshot of your code/config."},
        {"term": "Service", "def": "The main endpoint that routes traffic to revisions."},
        {"term": "Artifact Registry", "def": "Place to store Docker images before deploying."}
    ],
    "section_18_gke_basics.md": [
        {"term": "GKE", "def": "Google Kubernetes Engine. Managed K8s Service."},
        {"term": "Pod", "def": "Smallest unit in K8s. One or more containers."},
        {"term": "Node", "def": "Worker machine (VM) running the pods."},
        {"term": "Cluster", "def": "Group of Nodes managed by a Control Plane."},
        {"term": "Autopilot", "def": "GKE mode where Google manages Nodes completely."}
    ],
    "section_19_cloud_sql.md": [
        {"term": "Cloud SQL", "def": "Managed Relational DB (MySQL, PostgreSQL, SQL Server)."},
        {"term": "Read Replica", "def": "Copy of DB for Reading only. Scales Read throughput."},
        {"term": "High Availability", "def": "Standby Failover instance in a different Zone."},
        {"term": "Maintenance Window", "def": "Time when Google patches the DB (downtime possible)."},
        {"term": "Cloud Spanner", "def": "Global, Horizontally scalable relational DB (Expensive)."}
    ],
    "section_20_backup_dr.md": [
        {"term": "RTO", "def": "Recovery Time Objective. How long can you be down?"},
        {"term": "RPO", "def": "Recovery Point Objective. How much data can you lose?"},
        {"term": "Snapshot", "def": "Incremental backup of a Persistent Disk."},
        {"term": "Image", "def": "Complete bootable backup of a VM."},
        {"term": "Cross-Region", "def": "Storing backups in a different region for disaster recovery."}
    ],
    "section_21_final_architecture.md": [
        {"term": "Well-Architected", "def": "Framework for building secure, efficient, resilient systems."},
        {"term": "Decoupling", "def": "Separating components so failure doesn't cascade (using Pub/Sub)."},
        {"term": "Statelessness", "def": "Apps that don't store session data locally. Easy to scale."},
        {"term": "Blue/Green", "def": "Deployment strategy with two environments to minimize downtime."},
        {"term": "Circuit Breaker", "def": "Pattern to stop calling a failing service to prevent overload."}
    ],
    "section_22_final_exams.md": [
        {"term": "Elimination Strategy", "def": "Remove 2 obviously wrong answers first."},
        {"term": "Keyword Mapping", "def": "Global + Relational = Spanner. Analytics + SQL = BigQuery."},
        {"term": "Managed over DIY", "def": "Always prefer Managed Services (Cloud SQL) over DIY (VM)."},
        {"term": "Least Privilege", "def": "Always give the minimum permission needed."},
        {"term": "Cost vs Speed", "def": "Know when the exam asks for Cheapest vs Fastest."}
    ],
    "section_week_2_review.md": [
        {"term": "Week 2 Focus", "def": "Networking and Security (IAM)."},
        {"term": "Hops", "def": "Steps traffic takes. Internet -> LB -> VM."},
        {"term": "Public vs Private", "def": "Public = Internet reachable. Private = VPC only."},
        {"term": "Role Binding", "def": "Connecting User + Role + Resource."},
        {"term": "Service Account", "def": "Identity for Apps."}
    ],
    "section_week_3_review.md": [
        {"term": "Week 3 Focus", "def": "Serverless and Compute Options."},
        {"term": "GKE vs Cloud Run", "def": "GKE = Complex orchestration. Cloud Run = Simple container serving."},
        {"term": "App Engine vs Cloud Functions", "def": "App Engine = Full App. Functions = Snippets of code."},
        {"term": "Cloud Build", "def": "CI/CD service to build containers."},
        {"term": "Ops Agent", "def": "Software installed on VM to send logs/metrics to Google."}
    ]
}

def update_flashcards():
    updated_count = 0
    import json
    
    for filename, cards in flashcard_data.items():
        path = os.path.join(ARTIFACT_DIR, filename)
        if not os.path.exists(path):
            print(f"Skipping {filename} (not found)")
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<!-- FLASHCARDS" in content:
            print(f"Skipping {filename} (Already has flashcards)")
            continue
            
        json_str = json.dumps(cards, indent=2)
        flashcard_block = f"\n\n<!-- FLASHCARDS\n{json_str}\n-->\n"
        
        # Append to end of file
        with open(path, "a", encoding="utf-8") as f:
            f.write(flashcard_block)
            
        print(f"Updated {filename}")
        updated_count += 1
        
    print(f"\nSuccessfully populated flashcards for {updated_count} files.")

if __name__ == "__main__":
    update_flashcards()
