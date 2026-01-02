import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

# Clear all existing quizzes
QuizQuestion.objects.all().delete()
print("[OK] Cleared all existing quizzes")

# Quiz data for all days (Days 1-8 initially, can add more)
QUIZZES = {
    1: [  # Day 1 - 5 quizzes
        {"question_text": "What is cloud computing?", "options": ["A. Remote servers", "B. Physical hardware", "C. Local storage", "D. None"], "correct_answer": 1},
        {"question_text": "Which is a Google Cloud region?", "options": ["A. us-east1", "B. aws-west", "C. azure-central", "D. None"], "correct_answer": 1},
        {"question_text": "What is GCP Console?", "options": ["A. Web UI", "B. Command line", "C. API", "D. SDK"], "correct_answer": 1},
        {"question_text": "Cloud storage benefit?", "options": ["A. Scalability", "B. Fixed cost", "C. Local only", "D. Limited"], "correct_answer": 1},
        {"question_text": "GCP stands for?", "options": ["A. Google Cloud Platform", "B. General Computing", "C. Global CPU", "D. None"], "correct_answer": 1},
    ],
    2: [  # Day 2 - 5 quizzes
        {"question_text": "What is a GCP Project?", "options": ["A. Resource container", "B. VM only", "C. User account", "D. Billing"], "correct_answer": 1},
        {"question_text": "Resource Hierarchy top level?", "options": ["A. Organization", "B. Folder", "C. Project", "D. Resource"], "correct_answer": 1},
        {"question_text": "What is a Zone?", "options": ["A. Datacenter", "B. Region", "C. Project", "D. Folder"], "correct_answer": 1},
        {"question_text": "Multi-region benefit?", "options": ["A. High availability", "B. Low cost", "C. Simple", "D. Local"], "correct_answer": 1},
        {"question_text": "Region contains?", "options": ["A. Multiple zones", "B. One zone", "C. Projects", "D. Users"], "correct_answer": 1},
    ],
    3: [  # Day 3 - 5 quizzes  
        {"question_text": "Compute Engine provides?", "options": ["A. Virtual machines", "B. Containers", "C. Serverless", "D. Desktop"], "correct_answer": 1},
        {"question_text": "Machine type defines?", "options": ["A. CPU & Memory", "B. Storage only", "C. Network", "D. Region"], "correct_answer": 1},
        {"question_text": "Preemptible VM use case?", "options": ["A. Batch processing", "B. Production DB", "C. Critical app", "D. User auth"], "correct_answer": 1},
        {"question_text": "VM can be?", "options": ["A. Started/Stopped", "B. Only running", "C. Never stopped", "D. Deleted auto"], "correct_answer": 1},
        {"question_text": "Custom machine type?", "options": ["A. Custom CPU/RAM", "B. Fixed only", "C. Not possible", "D. Auto-sized"], "correct_answer": 1},
    ],
    4: [  # Day 4 - 5 quizzes
        {"question_text": "Cloud Storage class for archival?", "options": ["A. Standard", "B. Nearline", "C. Coldline", "D. Archive"], "correct_answer": 4},
        {"question_text": "Default storage class?", "options": ["A. Standard", "B. Nearline", "C. Coldline", "D. Archive"], "correct_answer": 1},
        {"question_text": "Lifecycle policy enables?", "options": ["A. Bucket Lock", "B. Auto-delete/transition", "C. Versioning", "D. Retention"], "correct_answer": 2},
        {"question_text": "Nearline minimum duration?", "options": ["A. 0 days", "B. 30 days", "C. 90 days", "D. 365 days"], "correct_answer": 2},
        {"question_text": "Upload large files with?", "options": ["A. gcloud storage", "B. gsutil", "C. Both A and B", "D. bq"], "correct_answer": 3},
    ],
    5: [  # Day 5 - 3 quizzes
        {"question_text": "Persistent Disk types?", "options": ["A. Standard & SSD", "B. HDD only", "C. RAM only", "D. Network"], "correct_answer": 1},
        {"question_text": "Local SSD is?", "options": ["A. Ephemeral", "B. Persistent", "C. Network", "D. Cloud"], "correct_answer": 1},
        {"question_text": "Disk can be?", "options": ["A. Attached to VM", "B. Standalone", "C. Both", "D. Neither"], "correct_answer": 3},
    ],
    6: [  # Day 6 - 5 quizzes
        {"question_text": "IAM stands for?", "options": ["A. Identity & Access Management", "B. Internet Access", "C. Internal Auth", "D. IP Address"], "correct_answer": 1},
        {"question_text": "IAM Role contains?", "options": ["A. Permissions", "B. Users", "C. Resources", "D. Regions"], "correct_answer": 1},
        {"question_text": "Service Account is for?", "options": ["A. Applications", "B. Humans only", "C. VMs only", "D. Networks"], "correct_answer": 1},
        {"question_text": "Principle of least privilege?", "options": ["A. Minimum access needed", "B. Maximum access", "C. No access", "D. Full admin"], "correct_answer": 1},
        {"question_text": "Predefined roles are?", "options": ["A. Google-managed", "B. User-created", "C. Auto-deleted", "D. None"], "correct_answer": 1},
    ],
    7: [  # Day 7 - 10 quizzes (Week 1 exam)
        {"question_text": "Cloud computing delivery model?", "options": ["A. IaaS, PaaS, SaaS", "B. On-premise only", "C. Desktop only", "D. Mobile only"], "correct_answer": 1},
        {"question_text": "GCP global infrastructure includes?", "options": ["A. Regions & Zones", "B. Cities only", "C. Countries", "D. Continents"], "correct_answer": 1},
        {"question_text": "Compute Engine best for?", "options": ["A. VMs & control", "B. Serverless", "C. Mobile apps", "D. Desktop"], "correct_answer": 1},
        {"question_text": "Cloud Storage object storage?", "options": ["A. Scalable files", "B. Block storage", "C. VM disks", "D. Databases"], "correct_answer": 1},
        {"question_text": "Persistent Disk vs Local SSD?", "options": ["A. Network vs Physical", "B. Same thing", "C. Both ephemeral", "D. Both network"], "correct_answer": 1},
        {"question_text": "IAM best practice?", "options": ["A. Regular audits", "B. Never review", "C. One-time setup", "D. Ignore"], "correct_answer": 1},
        {"question_text": "Project ID must be?", "options": ["A. Globally unique", "B. Local only", "C. Reusable", "D. Numeric"], "correct_answer": 1},
        {"question_text": "Preemptible VM can run?", "options": ["A. Up to 24 hours", "B. Forever", "C. 1 hour max", "D. 1 minute"], "correct_answer": 1},
        {"question_text": "Cloud Console is?", "options": ["A. Web-based UI", "B. CLI only", "C. Desktop app", "D. Mobile only"], "correct_answer": 1},
        {"question_text": "Resource hierarchy order?", "options": ["A. Org > Folder > Project > Resource", "B. Resource > Project", "C. Zone > Region", "D. Random"], "correct_answer": 1},
    ],
    8: [  # Day 8 - 5 quizzes
        {"question_text": "Instance Group purpose?", "options": ["A. Manage VM groups", "B. Storage", "C. Networking", "D. IAM"], "correct_answer": 1},
        {"question_text": "MIG stands for?", "options": ["A. Managed Instance Group", "B. Manual Instance", "C. Multiple IP", "D. None"], "correct_answer": 1},
        {"question_text": "Autoscaling based on?", "options": ["A. CPU, Traffic", "B. Time only", "C. Manual", "D. None"], "correct_answer": 1},
        {"question_text": "Health check monitors?", "options": ["A. VM availability", "B. Cost", "C. Region", "D. IAM"], "correct_answer": 1},
        {"question_text": "Auto-healing does?", "options": ["A. Recreates failed VMs", "B. Deletes VMs", "C. Nothing", "D. Stops VMs"], "correct_answer": 1},
    ],
    9: [  # Day 9 - 5 quizzes (Load Balancing)
        {"question_text": "Global Load Balancer type?", "options": ["A. HTTP(S)", "B. Network TCP", "C. Internal", "D. UDP"], "correct_answer": 1},
        {"question_text": "Regional Load Balancer?", "options": ["A. Network TCP/UDP", "B. Global HTTP", "C. SSL Proxy", "D. TCP Proxy"], "correct_answer": 1},
        {"question_text": "Cloud Armor protects?", "options": ["A. HTTP(S) LB", "B. VMs directly", "C. Cloud Storage", "D. VPC"], "correct_answer": 1},
        {"question_text": "LB backend can be?", "options": ["A. Instance Groups", "B. Single VM", "C. Local file", "D. None"], "correct_answer": 1},
        {"question_text": "Session affinity ensures?", "options": ["A. User requests go to same VM", "B. Faster speed", "C. Encryption", "D. Logging"], "correct_answer": 1},
    ],
    10: [  # Day 10 - 5 quizzes (Cloud SQL)
        {"question_text": "Cloud SQL supports?", "options": ["A. MySQL, PostgreSQL, SQL Server", "B. Oracle", "C. DB2", "D. Access"], "correct_answer": 1},
        {"question_text": "Cloud SQL is?", "options": ["A. Fully managed", "B. Self-managed", "C. Serverless", "D. Flat file"], "correct_answer": 1},
        {"question_text": "High Availability means?", "options": ["A. Failover replica", "B. Read replica", "C. Backup", "D. Export"], "correct_answer": 1},
        {"question_text": "Read Replica purpose?", "options": ["A. Scale reads", "B. Failover", "C. Backup", "D. Write speed"], "correct_answer": 1},
        {"question_text": "Maintenance window?", "options": ["A. Define update time", "B. Never updates", "C. Random updates", "D. Always down"], "correct_answer": 1},
    ],
    11: [  # Day 11 - 5 quizzes (VPC Networking)
        {"question_text": "VPC stands for?", "options": ["A. Virtual Private Cloud", "B. Virtual Public Cloud", "C. Very Personal Cloud", "D. None"], "correct_answer": 1},
        {"question_text": "VPC is?", "options": ["A. Global resource", "B. Regional", "C. Zonal", "D. Local"], "correct_answer": 1},
        {"question_text": "Subnet is?", "options": ["A. Regional resource", "B. Global", "C. Zonal", "D. Local"], "correct_answer": 1},
        {"question_text": "Firewall rules apply to?", "options": ["A. VPC network", "B. Region", "C. Disk", "D. User"], "correct_answer": 1},
        {"question_text": "Shared VPC allows?", "options": ["A. Share subnet across projects", "B. Share VM", "C. Share Disk", "D. Share IAM"], "correct_answer": 1},
    ],
    12: [  # Day 12 - 5 quizzes (App Engine)
        {"question_text": "App Engine Standard scales to?", "options": ["A. Zero", "B. One", "C. Two", "D. Fixed"], "correct_answer": 1},
        {"question_text": "App Engine Flexible uses?", "options": ["A. Docker containers", "B. Sandboxed runtimes", "C. VMs only", "D. SQL"], "correct_answer": 1},
        {"question_text": "Traffic splitting used for?", "options": ["A. A/B Testing", "B. Load balancing", "C. Cost", "D. Security"], "correct_answer": 1},
        {"question_text": "dispatch.yaml used for?", "options": ["A. Routing rules", "B. Database", "C. Storage", "D. IAM"], "correct_answer": 1},
        {"question_text": "Standard env startup?", "options": ["A. Seconds", "B. Minutes", "C. Hours", "D. Days"], "correct_answer": 1},
    ],
    13: [  # Day 13 - 5 quizzes (Cloud Run)
        {"question_text": "Cloud Run runs?", "options": ["A. Stateless containers", "B. Stateful VMs", "C. Databases", "D. Functions"], "correct_answer": 1},
        {"question_text": "Cloud Run pricing?", "options": ["A. Pay per use (100ms)", "B. Hourly", "C. Monthly", "D. Fixed"], "correct_answer": 1},
        {"question_text": "Concurrency means?", "options": ["A. Requests per container", "B. Total containers", "C. Total users", "D. CPU speed"], "correct_answer": 1},
        {"question_text": "Cloud Run Service handles?", "options": ["A. Web requests", "B. Background jobs", "C. Storage", "D. Networking"], "correct_answer": 1},
        {"question_text": "Min instances setting?", "options": ["A. Avoid cold starts", "B. Save cost", "C. Max speed", "D. None"], "correct_answer": 1},
    ],
    14: [  # Day 14 - 10 quizzes (Week 2 Review)
        {"question_text": "VPC scope is?", "options": ["A. Global", "B. Regional", "C. Zonal", "D. Project"], "correct_answer": 1},
        {"question_text": "Subnet scope is?", "options": ["A. Regional", "B. Global", "C. Zonal", "D. Project"], "correct_answer": 1},
        {"question_text": "Cloud SQL failover uses?", "options": ["A. Standby instance", "B. Read replica", "C. Backup", "D. Snapshot"], "correct_answer": 1},
        {"question_text": "App Engine versioning?", "options": ["A. Traffic splitting", "B. Not supported", "C. Manual only", "D. Auto-delete"], "correct_answer": 1},
        {"question_text": "Cloud Run artifact source?", "options": ["A. Artifact Registry", "B. Local disk", "C. Git repo", "D. Cloud Storage"], "correct_answer": 1},
        {"question_text": "Internal Load Balancer?", "options": ["A. Private IPs only", "B. Public IPs", "C. Global", "D. Hybrid"], "correct_answer": 1},
        {"question_text": "Firewall rule direction?", "options": ["A. Ingress & Egress", "B. Input only", "C. Output only", "D. None"], "correct_answer": 1},
        {"question_text": "Cloud SQL backup types?", "options": ["A. Automated & On-demand", "B. Manual only", "C. None", "D. Tape"], "correct_answer": 1},
        {"question_text": "App Engine cron usage?", "options": ["A. Scheduled tasks", "B. User auth", "C. Database", "D. Networking"], "correct_answer": 1},
        {"question_text": "Cloud Run concurrency default?", "options": ["A. 80", "B. 1", "C. 1000", "D. Unlimited"], "correct_answer": 1},
    ],
    15: [  # Day 15 - 5 quizzes (Docker/Containers)
        {"question_text": "Docker image is?", "options": ["A. Read-only template", "B. Running instance", "C. Virtual Machine", "D. Database"], "correct_answer": 1},
        {"question_text": "Dockerfile purpose?", "options": ["A. Build instructions", "B. Runtime config", "C. Network setup", "D. Storage"], "correct_answer": 1},
        {"question_text": "Container vs VM?", "options": ["A. Shared OS kernel", "B. Separate OS", "C. Slower", "D. Larger"], "correct_answer": 1},
        {"question_text": "K8s Pod is?", "options": ["A. Smallest deployable unit", "B. Virtual Machine", "C. Network rule", "D. Storage volume"], "correct_answer": 1},
        {"question_text": "Registry stores?", "options": ["A. Container images", "B. Code", "C. Logs", "D. Metrics"], "correct_answer": 1},
    ],
    16: [  # Day 16 - 5 quizzes (GKE Intro)
        {"question_text": "GKE manages?", "options": ["A. Kubernetes clusters", "B. VMs", "C. Functions", "D. Storage"], "correct_answer": 1},
        {"question_text": "GKE Master node?", "options": ["A. Google-managed", "B. User-managed", "C. Doesn't exist", "D. Optional"], "correct_answer": 1},
        {"question_text": "Node Pool is?", "options": ["A. Group of worker nodes", "B. Storage pool", "C. Network pool", "D. Admin group"], "correct_answer": 1},
        {"question_text": "kubectl is?", "options": ["A. CLI tool for K8s", "B. Web UI", "C. Database", "D. Network tool"], "correct_answer": 1},
        {"question_text": "Pod contains?", "options": ["A. One or more containers", "B. VMs", "C. Clusters", "D. Regions"], "correct_answer": 1},
    ],
    17: [  # Day 17 - 5 quizzes (GKE Autopilot)
        {"question_text": "GKE Autopilot manages?", "options": ["A. Nodes & Cluster", "B. Master only", "C. Nothing", "D. Network only"], "correct_answer": 1},
        {"question_text": "Autopilot pricing?", "options": ["A. Per Pod resources", "B. Per Node", "C. Flat fee", "D. Free"], "correct_answer": 1},
        {"question_text": "Standard mode allows?", "options": ["A. Full node access", "B. No node access", "C. API only", "D. None"], "correct_answer": 1},
        {"question_text": "Cluster upgrades?", "options": ["A. Auto in Autopilot", "B. Manual only", "C. Never", "D. Reinstall"], "correct_answer": 1},
        {"question_text": "SLA guarantee?", "options": ["A. Higher for Autopilot", "B. Same", "C. Lower", "D. None"], "correct_answer": 1},
    ],
    18: [  # Day 18 - 5 quizzes (K8s Objects)
        {"question_text": "Deployment manages?", "options": ["A. Replicas & Updates", "B. Network", "C. Storage", "D. Nodes"], "correct_answer": 1},
        {"question_text": "Service type ClusterIP?", "options": ["A. Internal only", "B. External", "C. Load Balancer", "D. Node Port"], "correct_answer": 1},
        {"question_text": "Service type LoadBalancer?", "options": ["A. Expose externally", "B. Internal only", "C. Database", "D. Storage"], "correct_answer": 1},
        {"question_text": "Label used for?", "options": ["A. Selecting objects", "B. Security", "C. Encryption", "D. Speed"], "correct_answer": 1},
        {"question_text": "Namespace provides?", "options": ["A. Logical isolation", "B. Physical isolation", "C. Network speed", "D. Redundancy"], "correct_answer": 1},
    ],
    19: [  # Day 19 - 5 quizzes (StatefulSets)
        {"question_text": "StatefulSet guarantees?", "options": ["A. Stable network ID", "B. Fastest startup", "C. Random names", "D. Statelessness"], "correct_answer": 1},
        {"question_text": "Headless Service uses?", "options": ["A. ClusterIP: None", "B. LoadBalancer", "C. NodePort", "D. ExternalName"], "correct_answer": 1},
        {"question_text": "DaemonSet runs?", "options": ["A. One pod per node", "B. One pod per cluster", "C. Randomly", "D. On master only"], "correct_answer": 1},
        {"question_text": "PersistentVolume (PV)?", "options": ["A. Cluster storage resource", "B. Local disk", "C. Memory", "D. CPU"], "correct_answer": 1},
        {"question_text": "PVC stands for?", "options": ["A. PersistentVolumeClaim", "B. Private Virtual Cloud", "C. Public Volume", "D. None"], "correct_answer": 1},
    ],
    20: [  # Day 20 - 5 quizzes (ConfigMaps/Secrets)
        {"question_text": "ConfigMap stores?", "options": ["A. Non-sensitive config", "B. Passwords", "C. Images", "D. Logs"], "correct_answer": 1},
        {"question_text": "Secret stores?", "options": ["A. Sensitive data", "B. Public HTML", "C. Metrics", "D. Images"], "correct_answer": 1},
        {"question_text": "Inject ConfigMap as?", "options": ["A. Env var or File", "B. Database", "C. Service", "D. Node"], "correct_answer": 1},
        {"question_text": "Secret encoding?", "options": ["A. Base64", "B. Encrypted", "C. Plaintext", "D. Hashed"], "correct_answer": 1},
        {"question_text": "Update ConfigMap?", "options": ["A. Pod restart needed usually", "B. Auto-update always", "C. Impossible", "D. Deletes pod"], "correct_answer": 1},
    ],
    21: [  # Day 21 - 10 quizzes (Week 3 Review)
        {"question_text": "GKE Standard vs Autopilot?", "options": ["A. User vs Google Managed Nodes", "B. Same", "C. Pricing only", "D. Speed only"], "correct_answer": 1},
        {"question_text": "Docker image layers?", "options": ["A. Cached & Reused", "B. Always rebuilt", "C. Single file", "D. Encrypted"], "correct_answer": 1},
        {"question_text": "K8s Service discovery?", "options": ["A. DNS names", "B. IP list", "C. Manual config", "D. Broadcast"], "correct_answer": 1},
        {"question_text": "StatefulSet usage?", "options": ["A. Databases", "B. Web servers", "C. Functions", "D. Load balancers"], "correct_answer": 1},
        {"question_text": "ConfigMap vs Secret?", "options": ["A. Plain vs Sensitive", "B. File vs Env", "C. Large vs Small", "D. None"], "correct_answer": 1},
        {"question_text": "DaemonSet usage?", "options": ["A. Logging agents", "B. Web app", "C. Database", "D. Cron job"], "correct_answer": 1},
        {"question_text": "HPA stands for?", "options": ["A. Horizontal Pod Autoscaler", "B. High Performance App", "C. Host Port Access", "D. None"], "correct_answer": 1},
        {"question_text": "Ingress resource?", "options": ["A. HTTP/S Routing", "B. TCP Load Balance", "C. Firewall", "D. Storage"], "correct_answer": 1},
        {"question_text": "Container Registry vs Artifact Registry?", "options": ["A. Legacy vs New", "B. Same", "C. New vs Legacy", "D. None"], "correct_answer": 1},
        {"question_text": "Pod lifecycle?", "options": ["A. Pending-Running-Succeeded", "B. Born-Live-Die", "C. Start-Stop", "D. On-Off"], "correct_answer": 1},
    ],
    22: [  # Day 22 - 5 quizzes (Cloud Operations)
        {"question_text": "Cloud Logging stores?", "options": ["A. Logs from resources", "B. Metrics", "C. User data", "D. Images"], "correct_answer": 1},
        {"question_text": "Cloud Monitoring tracks?", "options": ["A. Performance metrics", "B. Text logs", "C. Billing", "D. Code"], "correct_answer": 1},
        {"question_text": "Uptime Check verifies?", "options": ["A. Service availability", "B. Disk space", "C. CPU usage", "D. RAM usage"], "correct_answer": 1},
        {"question_text": "Alerting Policy does?", "options": ["A. Notifies on incidents", "B. Fixes bugs", "C. Stops VMs", "D. Deletes logs"], "correct_answer": 1},
        {"question_text": "Trace is for?", "options": ["A. Latency analysis", "B. Log search", "C. Cost analysis", "D. Network security"], "correct_answer": 1},
    ],
    23: [  # Day 23 - 5 quizzes (Cloud Functions)
        {"question_text": "Cloud Functions is?", "options": ["A. Serverless FaaS", "B. Container service", "C. VM service", "D. Database"], "correct_answer": 1},
        {"question_text": "Trigger types?", "options": ["A. HTTP, Pub/Sub, Storage", "B. Manual only", "C. Time only", "D. None"], "correct_answer": 1},
        {"question_text": "Function timeout limit?", "options": ["A. 9 mins (Gen 1) / 60 mins (Gen 2)", "B. Unlimited", "C. 30 secs", "D. 24 hours"], "correct_answer": 1},
        {"question_text": "Cold start mitigation?", "options": ["A. Min instances", "B. Max instances", "C. More RAM", "D. Keep warm script"], "correct_answer": 1},
        {"question_text": "Gen 2 based on?", "options": ["A. Cloud Run", "B. App Engine", "C. GKE", "D. Compute Engine"], "correct_answer": 1},
    ],
    24: [  # Day 24 - 5 quizzes (Network Security)
        {"question_text": "Firewall Rule priority?", "options": ["A. Lower number = Higher priority", "B. Higher number = Higher priority", "C. Random", "D. None"], "correct_answer": 1},
        {"question_text": "IAP stands for?", "options": ["A. Identity-Aware Proxy", "B. Internet Access Point", "C. Internal App Protocol", "D. None"], "correct_answer": 1},
        {"question_text": "IAP allows SSH without?", "options": ["A. Public IP", "B. Private IP", "C. VPC", "D. Firewall"], "correct_answer": 1},
        {"question_text": "Cloud NAT Usage?", "options": ["A. Internet for private VMs", "B. Inbound access", "C. Load balancing", "D. DNS"], "correct_answer": 1},
        {"question_text": "VPC Service Controls?", "options": ["A. Prevent data exfiltration", "B. Firewall only", "C. User auth", "D. Faster network"], "correct_answer": 1},
    ],
    25: [  # Day 25 - 5 quizzes (Cloud Armor)
        {"question_text": "Cloud Armor acts as?", "options": ["A. WAF & DDoS protection", "B. Antivirus", "C. Firewall only", "D. IAM"], "correct_answer": 1},
        {"question_text": "Security Policy targets?", "options": ["A. Load Balancer Backend", "B. VM directly", "C. VPC", "D. Cloud SQL"], "correct_answer": 1},
        {"question_text": "Preconfigured rules?", "options": ["A. XSS, SQLi protection", "B. User password", "C. Network speed", "D. None"], "correct_answer": 1},
        {"question_text": "Adaptive Protection?", "options": ["A. ML-based threat detection", "B. Manual rules", "C. Static list", "D. None"], "correct_answer": 1},
        {"question_text": "Allowed action?", "options": ["A. Deny (403/404/502)", "B. Delete user", "C. Stop VM", "D. Encrypt data"], "correct_answer": 1},
    ],
    26: [  # Day 26 - 5 quizzes (Billing)
        {"question_text": "Budgets & Alerts?", "options": ["A. Notify on spending", "B. Stop spending hard limit", "C. Delete resources", "D. Free credits"], "correct_answer": 1},
        {"question_text": "Billing Export?", "options": ["A. Send data to BigQuery", "B. Send invoice email", "C. Download PDF", "D. None"], "correct_answer": 1},
        {"question_text": "Committed Use Discount?", "options": ["A. 1 or 3 year commitment", "B. Monthly only", "C. Daily", "D. None"], "correct_answer": 1},
        {"question_text": "Sustained Use Discount?", "options": ["A. Auto for running VMs", "B. Manual application", "C. Pre-pay", "D. None"], "correct_answer": 1},
        {"question_text": "Label usage in billing?", "options": ["A. Cost allocation/breakdown", "B. Discount code", "C. Payment method", "D. Currency"], "correct_answer": 1},
    ],
    27: [  # Day 27 - 5 quizzes (Cloud Build)
        {"question_text": "Cloud Build is?", "options": ["A. Serverless CI/CD", "B. VM builder", "C. Storage service", "D. Database"], "correct_answer": 1},
        {"question_text": "Build config file?", "options": ["A. cloudbuild.yaml", "B. Dockerfile", "C. build.json", "D. makefile"], "correct_answer": 1},
        {"question_text": "Build triggers?", "options": ["A. Git push/tag", "B. Manual only", "C. Time only", "D. None"], "correct_answer": 1},
        {"question_text": "Build steps run in?", "options": ["A. Docker containers", "B. VMs", "C. Local machine", "D. Browser"], "correct_answer": 1},
        {"question_text": "Artifact storage?", "options": ["A. Container/Artifact Registry", "B. Local disk", "C. RAM", "D. Database"], "correct_answer": 1},
    ],
    28: [  # Day 28 - 10 quizzes (Week 4 Review)
        {"question_text": "Cloud Logging export sink?", "options": ["A. BigQuery, Storage, Pub/Sub", "B. Local file", "C. Email", "D. Printer"], "correct_answer": 1},
        {"question_text": "Cloud Functions use case?", "options": ["A. Event-driven processing", "B. Long running server", "C. Database hosting", "D. VPN"], "correct_answer": 1},
        {"question_text": "IAP SSH benefit?", "options": ["A. No public IP needed", "B. Faster", "C. No VPC", "D. No Firewall"], "correct_answer": 1},
        {"question_text": "Cloud Armor attaches to?", "options": ["A. Global HTTP(S) LB", "B. VM NIC", "C. Cloud Router", "D. Cloud NAT"], "correct_answer": 1},
        {"question_text": "Pricing calculator?", "options": ["A. Estimate costs", "B. Pay bills", "C. View history", "D. Stop resources"], "correct_answer": 1},
        {"question_text": "Cloud Build timeout?", "options": ["A. Default 10m, Max 24h", "B. Unlimited", "C. 1 min", "D. 1 hour"], "correct_answer": 1},
        {"question_text": "Alert policy notification?", "options": ["A. Email, SMS, Slack, PagerDuty", "B. Console only", "C. Log only", "D. None"], "correct_answer": 1},
        {"question_text": "Private Google Access?", "options": ["A. Access Google APIs via private IP", "B. Internet access", "C. VPN", "D. SSH"], "correct_answer": 1},
        {"question_text": "Cloud NAT purpose?", "options": ["A. Outbound internet for private VMs", "B. Inbound internet", "C. Load balancing", "D. Storage"], "correct_answer": 1},
        {"question_text": "Project Label purpose?", "options": ["A. Cost tracking", "B. Security", "C. Performance", "D. Networking"], "correct_answer": 1},
    ],
    29: [  # Day 29 - 5 quizzes (Architect Case Studies)
        {"question_text": "Mountkirk Games priority?", "options": ["A. Scaling & Global", "B. Local only", "C. Cost only", "D. Static content"], "correct_answer": 1},
        {"question_text": "TerramEarth priority?", "options": ["A. IoT streaming data", "B. Web hosting", "C. Employee email", "D. CRM"], "correct_answer": 1},
        {"question_text": "EHR Healthcare priority?", "options": ["A. Compliance & Security", "B. Open access", "C. Speed only", "D. Social media"], "correct_answer": 1},
        {"question_text": "Helicopter Racing priority?", "options": ["A. Low latency real-time", "B. Batch processing", "C. Archival", "D. Print logs"], "correct_answer": 1},
        {"question_text": "Case Study strategy?", "options": ["A. Map requirements to services", "B. Guess", "C. Ignore constraints", "D. Use defaults"], "correct_answer": 1},
    ],
    30: [  # Day 30 - 5 quizzes (BigQuery)
        {"question_text": "BigQuery is?", "options": ["A. Serverless Data Warehouse", "B. NoSQL DB", "C. Transactional DB", "D. File storage"], "correct_answer": 1},
        {"question_text": "BigQuery usage?", "options": ["A. Analytics & SQL", "B. Web app backend", "C. Session cache", "D. CDNs"], "correct_answer": 1},
        {"question_text": "BigQuery storage?", "options": ["A. Columnar", "B. Row-based", "C. Flat file", "D. Graph"], "correct_answer": 1},
        {"question_text": "Dataset contains?", "options": ["A. Tables & Views", "B. Projects", "C. VMs", "D. Networks"], "correct_answer": 1},
        {"question_text": "Partitioning improves?", "options": ["A. Query cost & performance", "B. Storage size", "C. Security", "D. Networking"], "correct_answer": 1},
    ],
    31: [  # Day 31 - 5 quizzes (Pub/Sub)
        {"question_text": "Pub/Sub ensures?", "options": ["A. Decoupled messaging", "B. Database storage", "C. VM hosting", "D. Load balancing"], "correct_answer": 1},
        {"question_text": "Push subscription?", "options": ["A. Pub/Sub sends to endpoint", "B. App polls server", "C. Manual check", "D. None"], "correct_answer": 1},
        {"question_text": "Pull subscription?", "options": ["A. App requests messages", "B. Server pushes to app", "C. Email alert", "D. None"], "correct_answer": 1},
        {"question_text": "Message ordering?", "options": ["A. Guaranteed with Ordering Key", "B. Always random", "C. Never possible", "D. FIFO always"], "correct_answer": 1},
        {"question_text": "Dead Letter Topic?", "options": ["A. Stores unprocessable messages", "B. Deleted messages", "C. Archive", "D. Admin logs"], "correct_answer": 1},
    ],
    32: [  # Day 32 - 5 quizzes (Dataflow)
        {"question_text": "Dataflow is based on?", "options": ["A. Apache Beam", "B. Apache Spark", "C. Hadoop", "D. Kafka"], "correct_answer": 1},
        {"question_text": "Processing modes?", "options": ["A. Batch & Stream", "B. Batch only", "C. Stream only", "D. Manual"], "correct_answer": 1},
        {"question_text": "Dataflow is?", "options": ["A. Fully Managed Serverless", "B. VM based", "C. Docker container", "D. Local app"], "correct_answer": 1},
        {"question_text": "Windowing used for?", "options": ["A. Aggregating stream data", "B. GUI display", "C. Storage", "D. Authentication"], "correct_answer": 1},
        {"question_text": "Update running pipeline?", "options": ["A. Drain or Cancel", "B. Stop only", "C. Pause", "D. Impossible"], "correct_answer": 1},
    ],
    33: [  # Day 33 - 5 quizzes (Hybrid Connectivity)
        {"question_text": "Cloud VPN connects?", "options": ["A. On-prem to VPC via Internet", "B. VPC to VPC", "C. VM to VM", "D. Internet to VM"], "correct_answer": 1},
        {"question_text": "Interconnect offers?", "options": ["A. Dedicated physical link", "B. VPN over public internet", "C. Wireless", "D. Satellite"], "correct_answer": 1},
        {"question_text": "Direct Peering?", "options": ["A. Connect to Google Edge", "B. VPN", "C. SSH", "D. Public Wi-Fi"], "correct_answer": 1},
        {"question_text": "VPN HA reliability?", "options": ["A. 99.99% SLA", "B. 50%", "C. 100%", "D. No SLA"], "correct_answer": 1},
        {"question_text": "Partner Interconnect?", "options": ["A. Via Service Provider", "B. Direct cable", "C. VPN", "D. Satellite"], "correct_answer": 1},
    ],
    34: [  # Day 34 - 5 quizzes (DB Migration)
        {"question_text": "DMS stands for?", "options": ["A. Database Migration Service", "B. Data Manage System", "C. Disk Move Service", "D. None"], "correct_answer": 1},
        {"question_text": "Homogeneous migration?", "options": ["A. Same engine (e.g. MySQL to MySQL)", "B. Different engine", "C. File to DB", "D. None"], "correct_answer": 1},
        {"question_text": "Continuous replication?", "options": ["A. Minimized downtime", "B. Offline only", "C. Manual copy", "D. Slow"], "correct_answer": 1},
        {"question_text": "DMS supports?", "options": ["A. MySQL, PostgreSQL, SQL Server, Oracle", "B. Excel", "C. Flat files", "D. NoSQL"], "correct_answer": 1},
        {"question_text": "Lift and Shift?", "options": ["A. Move with minimal change", "B. Rewrite app", "C. Delete data", "D. Archive"], "correct_answer": 1},
    ],
    35: [  # Day 35 - 10 quizzes (Week 5 Review)
        {"question_text": "BigQuery export format?", "options": ["A. CSV, JSON, Avro, Parquet", "B. Word Doc", "C. MP4", "D. EXE"], "correct_answer": 1},
        {"question_text": "Pub/Sub max message size?", "options": ["A. 10 MB", "B. 1 KB", "C. 1 GB", "D. Unlimited"], "correct_answer": 1},
        {"question_text": "Dataflow autoscaling?", "options": ["A. Horizontal worker scaling", "B. Vertical RAM only", "C. Manual only", "D. None"], "correct_answer": 1},
        {"question_text": "Cloud VPN bandwidth?", "options": ["A. up to 3 Gbps per tunnel", "B. 100 Gbps", "C. 1 Mbps", "D. Unlimited"], "correct_answer": 1},
        {"question_text": "Dedicated Interconnect speed?", "options": ["A. 10 Gbps or 100 Gbps", "B. 1 Gbps", "C. 50 Mbps", "D. Dial-up"], "correct_answer": 1},
        {"question_text": "DMS serverless?", "options": ["A. Yes", "B. No", "C. Sometimes", "D. VM based"], "correct_answer": 1},
        {"question_text": "BigQuery slot?", "options": ["A. Unit of computational capacity", "B. Storage unit", "C. Time unit", "D. Money"], "correct_answer": 1},
        {"question_text": "Apache Beam languages?", "options": ["A. Java, Python, Go", "B. C++ only", "C. Ruby only", "D. Swift"], "correct_answer": 1},
        {"question_text": "Pub/Sub at-least-once?", "options": ["A. Message delivered 1+ times", "B. Exactly once always", "C. Maybe delivered", "D. None"], "correct_answer": 1},
        {"question_text": "Hybrid Connect use case?", "options": ["A. Extend on-prem to cloud", "B. Web hosting", "C. Gaming", "D. Storage"], "correct_answer": 1},
    ],
    36: [  # Day 36 - 5 quizzes (SRE/Ops)
        {"question_text": "SLO stands for?", "options": ["A. Service Level Objective", "B. Service Log Option", "C. Slow Level Out", "D. None"], "correct_answer": 1},
        {"question_text": "SLi stands for?", "options": ["A. Service Level Indicator", "B. Service Log Input", "C. Slow Link In", "D. None"], "correct_answer": 1},
        {"question_text": "Error Budget?", "options": ["A. Allowed failure rate (1 - SLO)", "B. Financial budget", "C. Coding errors", "D. None"], "correct_answer": 1},
        {"question_text": "Toil is?", "options": ["A. Manual, repetitive work", "B. Hard coding", "C. CPU load", "D. Storage"], "correct_answer": 1},
        {"question_text": "Blameless Postmortem?", "options": ["A. Focus on process improvement", "B. Blame developer", "C. Fire staff", "D. Ignore error"], "correct_answer": 1},
    ],
    37: [  # Day 37 - 5 quizzes (FinOps)
        {"question_text": "FinOps goal?", "options": ["A. Maximize business value of cloud", "B. Reduce cost to zero", "C. Stop cloud use", "D. Buy hardware"], "correct_answer": 1},
        {"question_text": "CUD (Committed Use)?", "options": ["A. Commit usage for discount", "B. Pay as you go", "C. Free tier", "D. Spot instance"], "correct_answer": 1},
        {"question_text": "Identify idle VMs?", "options": ["A. Recommender VPA/Idle", "B. Guess", "C. Wait for crash", "D. Billing support"], "correct_answer": 1},
        {"question_text": "BigQuery cost control?", "options": ["A. Custom quotas & Partitioning", "B. Delete all data", "C. Run more queries", "D. None"], "correct_answer": 1},
        {"question_text": "Labeling strategy?", "options": ["A. Consistent keys (env, team)", "B. Random names", "C. No labels", "D. Emojis"], "correct_answer": 1},
    ],
    38: [  # Day 38 - 5 quizzes (Network Capstone)
        {"question_text": "Hub and Spoke topo?", "options": ["A. Central VPC connected to others", "B. Mesh", "C. Linear", "D. Isolated"], "correct_answer": 1},
        {"question_text": "Global VPC peering?", "options": ["A. Connect VPCs across regions", "B. Zones only", "C. Projects only", "D. Impossible"], "correct_answer": 1},
        {"question_text": "Private Service Access?", "options": ["A. Reach Google Managed Services (SQL) privately", "B. Public IP", "C. VPN", "D. SSH"], "correct_answer": 1},
        {"question_text": "Shared VPC Host?", "options": ["A. Controls network resources", "B. Uses resources", "C. Admin only", "D. None"], "correct_answer": 1},
        {"question_text": "Firewall logging?", "options": ["A. Detailed traffic analysis", "B. Block traffic", "C. Speed up", "D. None"], "correct_answer": 1},
    ],
    39: [  # Day 39 - 5 quizzes (Security Capstone)
        {"question_text": "KMS Key Rotation?", "options": ["A. Auto-rotate cryptographic keys", "B. Manual only", "C. Never", "D. Delete key"], "correct_answer": 1},
        {"question_text": "VPC Service Perimeter?", "options": ["A. Restrict API access to trusted networks", "B. Firewall only", "C. IAM only", "D. Public access"], "correct_answer": 1},
        {"question_text": "Binary Authorization?", "options": ["A. Ensure trusted container images", "B. Binary code check", "C. Network check", "D. None"], "correct_answer": 1},
        {"question_text": "Secret Manager versioning?", "options": ["A. Multiple secret versions enabled", "B. Single version only", "C. Text file", "D. None"], "correct_answer": 1},
        {"question_text": "Org Policy Constraint?", "options": ["A. Restrict resource configs across Org", "B. User permissions", "C. Billing", "D. Logging"], "correct_answer": 1},
    ],
    40: [  # Day 40 - 5 quizzes (DevOps Capstone)
        {"question_text": "Terraform State file?", "options": ["A. Tracks resource state", "B. Code file", "C. Log file", "D. Image"], "correct_answer": 1},
        {"question_text": "Cloud Build build step?", "options": ["A. Executable container action", "B. Manual click", "C. VM boot", "D. Login"], "correct_answer": 1},
        {"question_text": "Canary Deployment?", "options": ["A. Gradual traffic shift", "B. All at once", "C. Downtime update", "D. Manual copy"], "correct_answer": 1},
        {"question_text": "Source Repository?", "options": ["A. Git version control", "B. File storage", "C. Docker registry", "D. Database"], "correct_answer": 1},
        {"question_text": "Infrastructure as Code?", "options": ["A. Manage infra via config files", "B. Click ops", "C. Manual setup", "D. Sticky notes"], "correct_answer": 1},
    ],
    41: [  # Day 41 - 5 quizzes (Data Capstone)
        {"question_text": "Dataproc is?", "options": ["A. Managed Hadoop/Spark", "B. Serverless SQL", "C. NoSQL", "D. Queue"], "correct_answer": 1},
        {"question_text": "Dataflow Windowing?", "options": ["A. Slice data by time", "B. GUI window", "C. Storage partition", "D. None"], "correct_answer": 1},
        {"question_text": "Pub/Sub into BigQuery?", "options": ["A. Dataflow subscription or BigQuery subscription", "B. Manual copy", "C. Email", "D. Print"], "correct_answer": 1},
        {"question_text": "Composer is?", "options": ["A. Managed Airflow", "B. Music app", "C. Database", "D. Firewall"], "correct_answer": 1},
        {"question_text": "Data Catalog?", "options": ["A. Discovery & Metadata management", "B. Shopping app", "C. Database", "D. Storage"], "correct_answer": 1},
    ],
    42: [  # Day 42 - 10 quizzes (Week 6 Review)
        {"question_text": "SRE main focus?", "options": ["A. reliability & automation", "B. Speed only", "C. Cost only", "D. Manual work"], "correct_answer": 1},
        {"question_text": "Spot VM usage?", "options": ["A. Fault-tolerant batch jobs", "B. Database", "C. Critical API", "D. DNS"], "correct_answer": 1},
        {"question_text": "Terraform provider?", "options": ["A. Plugin for API interaction (e.g. Google)", "B. Internet provider", "C. User", "D. Server"], "correct_answer": 1},
        {"question_text": "Least Privilege?", "options": ["A. Minimal necessary access", "B. Full admin", "C. No access", "D. Random"], "correct_answer": 1},
        {"question_text": "Cloud NAT limitation?", "options": ["A. Outbound only (mostly)", "B. Inbound only", "C. Both equal", "D. None"], "correct_answer": 1},
        {"question_text": "DDoS protection?", "options": ["A. Cloud Armor", "B. Cloud Functions", "C. Cloud SQL", "D. Pub/Sub"], "correct_answer": 1},
        {"question_text": "Cloud Build trigger?", "options": ["A. Auto-run on commit", "B. Never runs", "C. Manual only", "D. Paid only"], "correct_answer": 1},
        {"question_text": "Dataproc vs Dataflow?", "options": ["A. Existing Hadoop vs New Beam", "B. Same", "C. SQL vs NoSQL", "D. None"], "correct_answer": 1},
        {"question_text": "Service Account Key?", "options": ["A. Credentials for app auth", "B. User password", "C. SSH key", "D. Door key"], "correct_answer": 1},
        {"question_text": "Org Policy inheritance?", "options": ["A. Org -> Folder -> Project", "B. Project -> Org", "C. Flat", "D. Random"], "correct_answer": 1},
    ],
    43: [  # Day 43 - 5 quizzes (Mock Exam 1)
        {"question_text": "Preemptible vs Spot?", "options": ["A. Legacy vs New (flexible duration)", "B. Same", "C. Spot is more expensive", "D. None"], "correct_answer": 1},
        {"question_text": "Coldline vs Archive?", "options": ["A. 90 days vs 365 days min", "B. 30 vs 90", "C. Same", "D. 1 year vs 10 years"], "correct_answer": 1},
        {"question_text": "Cloud Run Scale to Zero?", "options": ["A. Yes, save money", "B. No, always 1", "C. Manual", "D. Impossible"], "correct_answer": 1},
        {"question_text": "GKE Node Auto-provisioning?", "options": ["A. Auto create new node pools", "B. Scale existing only", "C. Manual", "D. None"], "correct_answer": 1},
        {"question_text": "Custom Role?", "options": ["A. Combine specific permissions", "B. Pre-made", "C. Google maintained", "D. None"], "correct_answer": 1},
    ],
    44: [  # Day 44 - 5 quizzes (Mock Exam 2)
        {"question_text": "Private Google Access?", "options": ["A. Private IP access to Google Services", "B. Public IP", "C. VPN", "D. Interconnect"], "correct_answer": 1},
        {"question_text": "Cloud Scheduler?", "options": ["A. Managed cron jobs", "B. Calendar", "C. Email", "D. Database"], "correct_answer": 1},
        {"question_text": "Memorystore?", "options": ["A. Managed Redis/Memcached", "B. SQL DB", "C. Disk", "D. Tape"], "correct_answer": 1},
        {"question_text": "Cloud Spanner?", "options": ["A. Global Relational (SQL) & Horizontal Scale", "B. NoSQL", "C. Local DB", "D. File"], "correct_answer": 1},
        {"question_text": "Firestore mode?", "options": ["A. Native or Datastore", "B. SQL or NoSQL", "C. Text or Binary", "D. None"], "correct_answer": 1},
    ],
    45: [  # Day 45 - 5 quizzes (Final Tips)
        {"question_text": "Official docs URL?", "options": ["A. cloud.google.com/docs", "B. google.com", "C. gcp.com", "D. docs.com"], "correct_answer": 1},
        {"question_text": "Exam format?", "options": ["A. Multiple choice/select", "B. Essay", "C. Coding", "D. Interview"], "correct_answer": 1},
        {"question_text": "ACE focus?", "options": ["A. Implementation & Management", "B. Architecture design", "C. Sales", "D. Machine Learning deep dive"], "correct_answer": 1},
        {"question_text": "Project hygiene?", "options": ["A. Shut down unused projects", "B. Keep running", "C. Ignore billing", "D. Share passwords"], "correct_answer": 1},
        {"question_text": "Certification validity?", "options": ["A. 2 years", "B. Lifetime", "C. 1 year", "D. 5 years"], "correct_answer": 1},
    ],

}

# Create quizzes
total_created = 0
for day_number, quizzes in QUIZZES.items():
    try:
        day = Day.objects.get(number=day_number)
        for quiz_data in quizzes:
            QuizQuestion.objects.create(
                day=day,
                question_text=quiz_data["question_text"],
                question_type="mcq",
                option_1=quiz_data["options"][0] if len(quiz_data["options"]) > 0 else None,
                option_2=quiz_data["options"][1] if len(quiz_data["options"]) > 1 else None,
                option_3=quiz_data["options"][2] if len(quiz_data["options"]) > 2 else None,
                option_4=quiz_data["options"][3] if len(quiz_data["options"]) > 3 else None,
                correct_option=quiz_data["correct_answer"]
            )
            total_created += 1
        print(f"[OK] Day {day_number}: {len(quizzes)} quizzes created")
    except Day.DoesNotExist:
       print(f"[ERROR] Day {day_number} not found in database")

print(f"\n[SUCCESS] Total quizzes created: {total_created}")
