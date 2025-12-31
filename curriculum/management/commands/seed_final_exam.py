from django.core.management.base import BaseCommand
from curriculum.models import Day, QuizQuestion

class Command(BaseCommand):
    help = 'Seeds Day 45 with a 60-question Final Exam'

    def handle(self, *args, **kwargs):
        day_num = 45
        try:
            day = Day.objects.get(number=day_num)
        except Day.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Day {day_num} does not exist.'))
            return

        # Update Title
        day.title = "Final Exam: Associate Cloud Engineer"
        day.description = "The Ultimate 60-Question Mock Exam"
        day.save()

        # Clear existing
        day.quiz_questions.all().delete()
        
        self.stdout.write('Seeding 60 Questions...')

        questions_data = [
            # IAM & Security (1-10)
            {
                "text": "Your organization wants to prevent any developer from creating a Service Account Key in any project. Which tool should you use?",
                "options": ["VPC Service Controls", "Organization Policy Constraint", "IAM Deny Policy", "Cloud Armor"],
                "correct": 2
            },
            {
                "text": "You need to grant a user access to view a specific bucket 'gs://hr-files', but they should not see other buckets in the project. What is the best practice?",
                "options": ["Grant 'Storage Object Viewer' at the Project level", "Grant 'Storage Object Viewer' on the Bucket itself", "Use an ACL on every file", "Grant 'Viewer' role at the Project level"],
                "correct": 2
            },
            {
                "text": "Which IAM role allows a user to create new projects?",
                "options": ["Project Creator", "Folder Creator", "Organization Administrator", "Billing Account User"],
                "correct": 1
            },
            {
                "text": "You are deploying an app on GKE that needs to access BigQuery. You want to avoid managing JSON keys. What should you configure?",
                "options": ["Node Service Account", "Workload Identity", "Cloud SQL Proxy", "Identity Aware Proxy"],
                "correct": 2
            },
            {
                "text": "A user accidentally deleted a custom IAM role. Can you recover it?",
                "options": ["No, it is permanently deleted.", "Yes, within 7 days using the undelete API.", "Yes, within 30 days but only via Support.", "Yes, automatically restored after 24 hours."],
                "correct": 2
            },
            {
                "text": "What is the hierarchy of IAM policy enforcement?",
                "options": ["Union of Parent and Child policies (Allow is additive)", "Child overrides Parent", "Parent overrides Child", "Most restrictive wins"],
                "correct": 1
            },
            {
                "text": "You need to store encryption keys in a hardware module validated to FIPS 140-2 Level 3. Which Cloud KMS protection level do you choose?",
                "options": ["Software", "HSM", "External", "Imported"],
                "correct": 2
            },
            {
                "text": "Which service helps protect your application from DDoS attacks and SQL injection?",
                "options": ["VPC Firewall", "Cloud Armor", "Cloud NAT", "Identity Aware Proxy"],
                "correct": 2
            },
            {
                "text": "You want to audit usage of your service account keys. Which log do you check?",
                "options": ["VPC Flow Logs", "Cloud Audit Logs (Policy Denied)", "Key Access Justifications", "Cloud Audit Logs (Data Access)"],
                "correct": 4
            },
            {
                "text": "A developer needs temporary access to a production VM. What is the most secure method?",
                "options": ["Share the SSH key", "Grant 'Compute Instance Admin' permanently", "Use OS Login with 2FA", "Just-In-Time (JIT) Privilege Escalation tool"],
                "correct": 3
            },

            # Compute & Networking (11-25)
            {
                "text": "You need to resize a Persistent Disk attached to a running VM. What must you do first?",
                "options": ["Stop the VM", "Take a snapshot", "Nothing, you can resize online", "Detach the disk"],
                "correct": 3
            },
            {
                "text": "Which Load Balancer is appropriate for a global HTTPs application?",
                "options": ["External Passthrough Network Filter", "External Application Load Balancer", "Internal Application Load Balancer", "Proxy Network Load Balancer"],
                "correct": 2
            },
            {
                "text": "Two VPCs need to communicate privately. They have overlapping IP ranges. What can you use?",
                "options": ["VPC Peering", "Shared VPC", "Private Service Connect", "Cloud VPN"],
                "correct": 3
            },
            {
                "text": "You want to run a batch job that can be interrupted. Saving cost is the priority. Which VM type?",
                "options": ["E2-Standard", "Spot VM", "Committed Use Discount", "Sole Tenant Node"],
                "correct": 2
            },
            {
                "text": "How do you connect an on-premises network to GCP with the highest reliability (99.99%)?",
                "options": ["Cloud VPN (HA)", "Dedicated Interconnect", "Partner Interconnect", "Direct Peering"],
                "correct": 2
            },
            {
                "text": "Which feature allows VMs in a subnet to access the internet without a public IP?",
                "options": ["Cloud VPN", "Cloud NAT", "VPC Peering", "Private Google Access"],
                "correct": 2
            },
            {
                "text": "You need to verify the latency between two regions. What is the simple command?",
                "options": ["ping", "gcloud networking ping", "Network Intelligence Center (Performance Dashboard)", "traceroute"],
                "correct": 3
            },
            {
                "text": "A firewall rule allows port 80 from 0.0.0.0/0 with priority 1000. Another denies port 80 with priority 100. What happens?",
                "options": ["Traffic is Allowed", "Traffic is Denied", "Traffic is Allowed only for authenticated users", "Error: Conflict"],
                "correct": 2
            },
            {
                "text": "App Engine Standard vs Flexible. Which one supports Docker containers directly?",
                "options": ["Standard", "Flexible", "Both", "Neither"],
                "correct": 2
            },
            {
                "text": "You want to deploy a container that scales down to zero when not in use. Which service?",
                "options": ["GKE Standard", "GKE Autopilot", "Cloud Run", "Compute Engine"],
                "correct": 3
            },
            {
                "text": "What is the maximum number of VPC networks in a project?",
                "options": ["1", "5", "50", "Unlimited (Quota based)"],
                "correct": 2
            },
            {
                "text": "Which GKE mode abstracts away node management entirely?",
                "options": ["GKE Standard", "GKE Autopilot", "Anthos", "Kubespray"],
                "correct": 2
            },
            {
                "text": "You need to store container images. Which is the modern recommended service?",
                "options": ["Container Registry", "Artifact Registry", "Cloud Storage", "Docker Hub"],
                "correct": 2
            },
            {
                "text": "How do you securely connect to a VM without opening port 22 to the internet?",
                "options": ["Bastion Host", "IAP (Identity Aware Proxy) for TCP Forwarding", "Cloud VPN", "Cloud Shell"],
                "correct": 2
            },
            {
                "text": "Which Google Cloud service provides a managed DNS service?",
                "options": ["Cloud CDNS", "Cloud DNS", "Cloud Domains", "Route53"],
                "correct": 2
            },

            # Storage & Databases (26-40)
            {
                "text": "You need a relational database that scales globally (horizontally). High cost is acceptable.",
                "options": ["Cloud SQL", "Bigtable", "Spanner", "BigQuery"],
                "correct": 3
            },
            {
                "text": "You have 50TB of IoT sensor data (Time-series). You need < 10ms writes. Queries are by row key.",
                "options": ["Cloud SQL", "Bigtable", "Firestore", "Spanner"],
                "correct": 2
            },
            {
                "text": "You need to migrate an Oracle DB to GCP with minimal downtime.",
                "options": ["Database Migration Service (DMS)", "BigQuery Data Transfer", "Transfer Appliance", "gsutil cp"],
                "correct": 1
            },
            {
                "text": "Which Storage Class is best for data accessed once a year for compliance?",
                "options": ["Standard", "Nearline", "Coldline", "Archive"],
                "correct": 4
            },
            {
                "text": "You need to query data sitting in Cloud Storage using SQL without loading it.",
                "options": ["BigQuery External Table", "Dataflow", "Dataproc", "Cloud SQL"],
                "correct": 1
            },
            {
                "text": "Best database for a mobile game backend (NoSQL, User Profiles, Offline Sync)?",
                "options": ["Bigtable", "Firestore", "Cloud SQL", "Memorystore"],
                "correct": 2
            },
            {
                "text": "You need a fast in-memory cache for Redis.",
                "options": ["Cloud SQL", "Memorystore", "Bigtable", "Spanner"],
                "correct": 2
            },
            {
                "text": "What is the default retention period of a Cloud Storage bucket?",
                "options": ["30 days", "1 year", "Unlimited (Forever)", "7 days"],
                "correct": 3
            },
            {
                "text": "Which object versioning state effectively deletes a file?",
                "options": ["Archive", "Noncurrent", "Delete Marker", "Soft Delete"],
                "correct": 3
            },
            {
                "text": "You need to transfer 1 PB of data from on-prem to GCP. Internet is slow (100 Mbps).",
                "options": ["gsutil -m cp", "Storage Transfer Service", "Transfer Appliance", "Cloud VPN"],
                "correct": 3
            },
            {
                "text": "Cloud SQL High Availability (HA) creates a standby in:",
                "options": ["A different Region", "A different Zone", "The same Zone", "On-Premises"],
                "correct": 2
            },
            {
                "text": "You specifically want to run 'Apache Hadoop' workloads. Which service?",
                "options": ["Dataflow", "Dataproc", "BigQuery", "Composer"],
                "correct": 2
            },
            {
                "text": "Which BigQuery feature improves query cost/performance by grouping data by date?",
                "options": ["Clustering", "Partitioning", "Sharding", "Indexing"],
                "correct": 2
            },
            {
                "text": "How do you restrict a bucket so objects cannot be deleted for 5 years?",
                "options": ["ACLs", "Retention Policy (Locked)", "IAM Deny", "Lifecycle Rule"],
                "correct": 2
            },
            {
                "text": "Which database is compatible with PostgreSQL?",
                "options": ["Cloud Spanner", "Cloud SQL", "Firestore", "Bigtable"],
                "correct": 2
            },

            # Operations & Billing (41-50)
            {
                "text": "You want to receive an email when your bill exceeds $1000.",
                "options": ["Budgets & Alerts", "Cloud Monitoring", "Billing Export", "Cost Table"],
                "correct": 1
            },
            {
                "text": "Which tool provides recommendations to resize idle VMs?",
                "options": ["Cost Explorer", "Recommender API", "Cloud Monitoring", "Active Assist"],
                "correct": 4
            },
            {
                "text": "You need to export billing data to BigQuery. How often is it updated?",
                "options": ["Real-time", "Every 10 minutes", "Automatically throughout the day", "Once a month"],
                "correct": 3
            },
            {
                "text": "Which metric verifies if your service is meeting the SLA?",
                "options": ["SLI", "SLO", "Error Budget", "Latency"],
                "correct": 1
            },
            {
                "text": "A deployment failed. You want to view the build logs. Where do you look?",
                "options": ["Cloud Build History", "Container Registry", "Source Repositories", "Compute Engine Logs"],
                "correct": 1
            },
            {
                "text": "What is the fastest way to troubleshoot a '502 Bad Gateway' text error?",
                "options": ["Cloud Trace", "Cloud Logging (Error Reporting)", "Cloud Profiler", "Cloud Monitoring"],
                "correct": 2
            },
            {
                "text": "You want to trace a request across microservices to find latency bottlenecks.",
                "options": ["Cloud Logging", "Cloud Trace", "Cloud Debugger", "Cloud Profiler"],
                "correct": 2
            },
            {
                "text": "What is best practice for labeling resources for billing?",
                "options": ["No labels needed", "Label by Department/Environment", "Label with random IDs", "Use Tags instead"],
                "correct": 2
            },
            {
                "text": "Can you use the Free Tier for production?",
                "options": ["Yes, up to the limits", "No, it's dev only", "No, it has no SLA", "Yes, but you need approval"],
                "correct": 1
            },
            {
                "text": "How do you ensure a specific number of pods are always running?",
                "options": ["Horizontal Pod Autoscaler", "Deployment (Replicas)", "StatefulSet", "DaemonSet"],
                "correct": 2
            },

            # Scenarios & Advanced (51-60)
            {
                "text": "You need a serverless workflow to chain together Cloud Functions and BigQuery.",
                "options": ["Cloud Scheduler", "Cloud Tasks", "Cloud Workflows", "Eventarc"],
                "correct": 3
            },
            {
                "text": "You want to run a script every morning at 8 AM.",
                "options": ["Cloud Workflows", "Cloud Scheduler", "Cloud Pub/Sub", "App Engine Cron"],
                "correct": 2
            },
            {
                "text": "Which service creates a dedicated private connection between your on-prem HW and Google?",
                "options": ["Cloud VPN", "Cloud Interconnect", "Peering", "Carrier Peering"],
                "correct": 2
            },
            {
                "text": "You have a requirement to filter outgoing traffic to specific domains only (FQDN).",
                "options": ["Cloud NAT", "VPC Firewall", "Secure Web Proxy / FQDN Firewall", "Cloud Router"],
                "correct": 3
            },
            {
                "text": "What is the command to initialize the SDK?",
                "options": ["gcloud init", "gcloud start", "gcloud auth login", "gcloud config set"],
                "correct": 1
            },
            {
                "text": "You need to reduce the startup time of your GKE pods.",
                "options": ["Use smaller images (Distroless)", "Increase CPU", "Use Image Streaming", "Use Preemptible Nodes"],
                "correct": 3
            },
            {
                "text": "Where are Cloud Storage encryption keys managed if you use CMEK?",
                "options": ["IAM", "Cloud KMS", "Secret Manager", "Compute Engine"],
                "correct": 2
            },
            {
                "text": "You need to store an API Key. Where is the safest place?",
                "options": ["Environment Variables", "Code", "Secret Manager", "Cloud Storage"],
                "correct": 3
            },
            {
                "text": "Which load balancer preserves the Client IP by default?",
                "options": ["External Passthrough Network Internal LB", "External HTTP(S) LB", "Internal HTTP(S) LB", "SSL Proxy"],
                "correct": 1
            },
            {
                "text": "Final Question: What is the GCP motto for reliability?",
                "options": ["Move fast and break things", "Hope is not a strategy", "Uptime is money", "Google never fails"],
                "correct": 2
            }
        ]

        count = 0
        for q_data in questions_data:
            q = QuizQuestion.objects.create(
                day=day,
                question_text=q_data["text"],
                option_1=q_data["options"][0],
                option_2=q_data["options"][1],
                option_3=q_data["options"][2],
                option_4=q_data["options"][3],
                correct_option=q_data["correct"]
            )
            count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} exam questions for Day 45.'))
