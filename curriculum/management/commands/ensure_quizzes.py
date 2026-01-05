import os
import json
from django.core.management.base import BaseCommand
from curriculum.models import Day, QuizQuestion

class Command(BaseCommand):
    help = 'Ensures every day has at least 3 quiz questions'

    def handle(self, *args, **kwargs):
        self.stdout.write('Checking and populating quizzes for all days...')

        # QUIZ DATA BANK (3 Questions per day)
        quiz_data = {
            1: [
                {"q": "What is the main difference between CapEx and OpEx?", "o1": "CapEx is pay-as-you-go, OpEx is upfront", "o2": "OpEx is monthly expense, CapEx is upfront investment", "o3": "They are the same", "o4": "CapEx is for software only", "ans": 2},
                {"q": "Which characteristic allows scaling up automatically?", "o1": "Button click", "o2": "Elasticity", "o3": "Pooling", "o4": "Broad Access", "ans": 2},
                {"q": "Who manages the hard drives in Google Cloud?", "o1": "The User", "o2": "The Government", "o3": "Google / Provider", "o4": "Your ISP", "ans": 3},
                {"q": "NEXT LEVEL: What is 'Workload Identity Federation' used for?", "o1": "Federating billing accounts.", "o2": "Allowing AWS/GitHub to login to GCP without Service Account Keys.", "o3": "Merging two GCP organizations.", "o4": "Federating SQL databases.", "ans": 2},
                {"q": "NEXT LEVEL: You need to set a hard limit on how many vCPUs a project can use. What do you configure?", "o1": "Budget Alert.", "o2": "Quota.", "o3": "Firewall Rule.", "o4": "IAM Policy.", "ans": 2},
                {"q": "NEXT LEVEL: Which resource defaults to 'Zonal' availability?", "o1": "Images.", "o2": "Snapshots.", "o3": "Virtual Machine Instances.", "o4": "VPC Networks.", "ans": 3}
            ],
            2: [
                {"q": "What is a GCP Project?", "o1": "Resource container", "o2": "VM only", "o3": "User account", "o4": "Billing", "ans": 1, "explanation": "A project is the fundamental container for all resources in Google Cloud. Billing and APIs are managed at this level."},
                {"q": "What is the top level of the Resource Hierarchy?", "o1": "Organization", "o2": "Folder", "o3": "Project", "o4": "Resource", "ans": 1, "explanation": "The Organization is the root node of the Google Cloud resource hierarchy, typically representing a company."},
                {"q": "What is a Zone in Google Cloud?", "o1": "A group of regions", "o2": "A single failure domain (datacenter building)", "o3": "A region", "o4": "A project", "ans": 2, "explanation": "A zone is a deployment area within a region. Deploying across multiple zones ensures High Availability (HA)."},
                {"q": "What is the primary benefit of a Multi-Region deployment?", "o1": "Low cost", "o2": "Maximum High Availability", "o3": "Simplicity", "o4": "Local access", "ans": 2, "explanation": "Multi-region deployments provide the highest level of availability and disaster recovery across geographical distances."},
                {"q": "What does a Region contain?", "o1": "Multiple zones", "o2": "One zone", "o3": "Projects", "o4": "Users", "ans": 1, "explanation": "A region is a geographical location that consists of three or more zones."}
            ],
            3: [
                {"q": "What is used to organize all resources in GCP?", "o1": "Folders", "o2": "Projects", "o3": "Buckets", "o4": "Nodes", "ans": 2},
                {"q": "How can you prevent overspending?", "o1": "Stop using GCP", "o2": "Set Budgets & Alerts", "o3": "Delete everything daily", "o4": "Use only free tier", "ans": 2},
                {"q": "Everything in GCP must belong to a...?", "o1": "User", "o2": "Project", "o3": "Region", "o4": "Zone", "ans": 2},
                {"q": "NEXT LEVEL: You tried to create a bucket but got a 'Policy Restricted' error. What is the likely cause?", "o1": "You are out of money.", "o2": "An Organization Policy (e.g., Domain Restricted Sharing) is blocking it.", "o3": "GCP is down.", "o4": "You need a reboot.", "ans": 2},
                {"q": "NEXT LEVEL: Which discount is 'Spend-Based' rather than 'Resource-Based'?", "o1": "Committed Use Discount (CUD) for specific Hardware.", "o2": "Spot VM Discount.", "o3": "Sustained Use Discount.", "o4": "Flexible Committed Use Discount (Spend-based).", "ans": 4},
                {"q": "NEXT LEVEL: To analyze billing data with SQL, what must you do first?", "o1": "Enable Billing Export to BigQuery.", "o2": "Download the CSV.", "o3": "Use Data Studio.", "o4": "You cannot use SQL.", "ans": 1},
                {"q": "SCENARIO: You have 20 projects and need to allocate costs by 'Business Unit' and alert on bad spending. Best structure?", "o1": "Separate Billing Accounts for each unit.", "o2": "Labels for everything.", "o3": "Manual spreadsheet.", "o4": "Use Folders per Business Unit, Cloud Billing account per folder, and Budget Alerts.", "ans": 4},
                {"q": "SCENARIO: Finance team wants a detailed breakdown of costs by Service (SQL, GKE) and Team (Frontend, Backend). Best tool?", "o1": "Export Cloud Billing to BigQuery + Custom Reports.", "o2": "Cloud Monitoring.", "o3": "Check Console monthly.", "o4": "AWS Cost Explorer.", "ans": 1}
            ],
            4: [
                {"q": "Which service offers raw Virtual Machines?", "o1": "App Engine", "o2": "Compute Engine", "o3": "Cloud Run", "o4": "GKE", "ans": 2},
                {"q": "What is a Preemptible/Spot VM?", "o1": "A faster VM", "o2": "A short-lived cheap VM (up to 91% off)", "o3": "A VIP VM", "o4": "A broken VM", "ans": 2},
                {"q": "Can you change the machine type of a running VM?", "o1": "Yes, instantly", "o2": "No, you must stop it first", "o3": "No, never", "o4": "Only on Sundays", "ans": 2},
                {"q": "NEXT LEVEL: How much warning time does a Spot VM get before termination?", "o1": "10 minutes.", "o2": "30 seconds.", "o3": "1 hour.", "o4": "Zero warning.", "ans": 2},
                {"q": "NEXT LEVEL: You have a strict compliance requirement to run on a physical server dedicated ONLY to your company. What do you use?", "o1": "Shielded VM.", "o2": "Sole-Tenant Node.", "o3": "Dedicated Interconnect.", "o4": "Private Google Access.", "ans": 2},
                {"q": "NEXT LEVEL: You want to prevent a VM from being accidentally deleted. What do you set?", "o1": "IAM Policy.", "o2": "Deletion Protection flag.", "o3": "Firewall Rule.", "o4": "Shutdown Script.", "ans": 2}
            ],
            5: [
                {"q": "Which disk type is fastest?", "o1": "Standard HDD", "o2": "Balanced Persistent Disk", "o3": "Local SSD", "o4": "Cloud Storage", "ans": 3},
                {"q": "If you delete a VM, what happens to the external Persistent Disk?", "o1": "Always deleted", "o2": "Depends on the 'Delete boot disk' flag (defaults to Keep for non-boot).", "o3": "It is archived", "o4": "It explodes", "ans": 2},
                {"q": "Can Local SSDs survive a VM stop/start?", "o1": "Yes", "o2": "No, data is lost (Ephemeral).", "o3": "Maybe", "o4": "Only if encrypted", "ans": 2},
                {"q": "NEXT LEVEL: What is a 'Confidential VM'?", "o1": "A VM with no public IP.", "o2": "A VM that encrypts data in-use (in RAM).", "o3": "A VM inside a VPN.", "o4": "A secret VM.", "ans": 2},
                {"q": "NEXT LEVEL: You need to patch the OS of 1,000 VMs automatically. What tool do you use?", "o1": "SSH loop.", "o2": "VM Manager (OS Config).", "o3": "Cloud Functions.", "o4": "Manually.", "ans": 2},
                {"q": "NEXT LEVEL: You need to resize a Persistent Disk. Can you decrease its size?", "o1": "Yes.", "o2": "No, you can only increase size.", "o3": "Yes, if you stop the VM.", "o4": "Only for SSD.", "ans": 2}
            ],
            6: [
                {"q": "What is the primary container for objects in Cloud Storage?", "o1": "Folder", "o2": "Bucket", "o3": "Box", "o4": "Bin", "ans": 2},
                {"q": "Which storage class is cheapest for long-term archives?", "o1": "Standard", "o2": "Nearline", "o3": "Coldline", "o4": "Archive", "ans": 4},
                {"q": "Cloud Storage objects are immutable. What does this mean?", "o1": "You cannot edit them, only replace them", "o2": "They live forever", "o3": "They cannot be moved", "o4": "They are invisible", "ans": 1},
                {"q": "NEXT LEVEL: How do you enforce that no objects in a bucket can be publicly accessible?", "o1": "Use ACLs.", "o2": "Enforce 'Uniform Bucket-Level Access' & Org Policy 'Enforce Public Access Prevention'.", "o3": "Delete the bucket.", "o4": "Make the name secret.", "ans": 2},
                {"q": "NEXT LEVEL: You need to upload 10 TB of small files. What command is fastest?", "o1": "gsutil cp", "o2": "gsutil -m cp (Multithreaded)", "o3": "Upload via Console", "o4": "Email them.", "ans": 2},
                {"q": "NEXT LEVEL: What feature protects against accidental deletion of objects?", "o1": "Object Versioning.", "o2": "Lifecycle Policy.", "o3": "CMEK.", "o4": "Hashing.", "ans": 1},
                {"q": "SCENARIO: Regulation requires: Data at rest encrypted with Customer-Managed Keys (CMK), Data in transit TLS, Audit logs. Config?", "o1": "Default Encryption + ACLs.", "o2": "Cloud KMS with CMK + Cloud Audit Logs (Data Access).", "o3": "Google Managed Keys + IAM.", "o4": "App-layer encryption + Secrets.", "ans": 2},
                {"q": "SCENARIO: Logs older than 90 days are rare, delete after 7 years. Minimize cost.", "o1": "Manual delete.", "o2": "Lifecycle: 90 days -> Archive, 2555 days -> Delete.", "o3": "Lifecycle: 7 years -> Delete (Standard storage).", "o4": "Weekly backups.", "ans": 2}
            ],
            7: [
                {"q": "Q1. You need to ensure your application can survive if the entire 'us-central1' region goes offline. What should you do?", "o1": "Deploy resources in multiple Zones within us-central1.", "o2": "Deploy resources in us-central1 and us-east1.", "o3": "Use a Preemptible VM.", "o4": "Take a snapshot every hour.", "ans": 2},
                {"q": "Q2. You have a legacy application that requires a specific version of the Linux Kernel. Which compute service should you use?", "o1": "App Engine", "o2": "Cloud Run", "o3": "Compute Engine", "o4": "Cloud Functions", "ans": 3},
                {"q": "NEXT LEVEL: Shared VPC vs VPC Peering. Which one allows Centralized Administration (Host Project)?", "o1": "VPC Peering.", "o2": "Shared VPC.", "o3": "Cloud VPN.", "o4": "Both.", "ans": 2},
                {"q": "NEXT LEVEL: Is VPC Peering transitive? (If A peers B, and B peers C, can A talk to C?)", "o1": "Yes.", "o2": "No.", "o3": "Only if using BGP.", "o4": "Only in the same region.", "ans": 2},
                {"q": "Q5. A startup wants to host a simple promotional website (HTML/CSS) with $0 budget. What do you recommend?", "o1": "Compute Engine (N1-standard).", "o2": "Google Kubernetes Engine (GKE).", "o3": "Cloud Storage (Static Website Hosting).", "o4": "Cloud SQL.", "ans": 3},
                {"q": "Q6. You received a 'Quota Exceeded' error when creating a VM. What does this mean?", "o1": "You ran out of money.", "o2": "You hit the hard limit of resources allowed for your project.", "o3": "The region is down.", "o4": "You chose an invalid machine type.", "ans": 2},
                {"q": "NEXT LEVEL: A VM without a Public IP needs to access a Cloud Storage Bucket. What do you enable?", "o1": "Cloud NAT.", "o2": "Private Google Access.", "o3": "A Jump Host.", "o4": "You must give it a Public IP.", "ans": 2},
                {"q": "Q8. Which usage type best fits a 'Preemptible' VM?", "o1": "The main database for your bank.", "o2": "A batch job that can resume if interrupted.", "o3": "The checkout page of an e-commerce site.", "o4": "A VPN server.", "ans": 2},
                {"q": "Q9. What is the difference between CapEx and OpEx?", "o1": "CapEx is monthly bills; OpEx is upfront cost.", "o2": "CapEx is buying hardware; OpEx is renting services (Cloud).", "o3": "CapEx is for startups; OpEx is for enterprises.", "o4": "There is no difference.", "ans": 2},
                {"q": "Q10. You need a specific GPU in us-west1-a but can't find it. What is likely the reason?", "o1": "GPUs are not supported in GCP.", "o2": "Not all hardware is available in all Zones.", "o3": "You didn't pay enough.", "o4": "You need to use a Local SSD.", "ans": 2}
            ],
            8: [
                {"q": "A VPC Network is...", "o1": "Regional", "o2": "Zonal", "o3": "Global", "o4": "Local", "ans": 3},
                {"q": "Default VPC comes with...?", "o1": "No subnets", "o2": "One subnet per region", "o3": "100 subnets", "o4": "A firewall blocking everything", "ans": 2},
                {"q": "Can two VPCs talk to each other by default?", "o1": "Yes", "o2": "No, they are isolated", "o3": "Only on Tuesdays", "o4": "If they share a project", "ans": 2},
                {"q": "NEXT LEVEL: What is the Max Transmission Unit (MTU) for a standard VPC?", "o1": "1500 bytes.", "o2": "1460 bytes (Standard).", "o3": "9000 bytes (Jumbo).", "o4": "8896 bytes.", "ans": 2},
                {"q": "NEXT LEVEL: Which Hybrid Connectivity option requires a physical cable to a Google facility?", "o1": "Cloud VPN.", "o2": "Dedicated Interconnect.", "o3": "Carrier Peering.", "o4": "Cloud Router.", "ans": 2},
                {"q": "NEXT LEVEL: Cloud VPN uses which protocol?", "o1": "SSL.", "o2": "IPsec (IKEv2).", "o3": "SSH.", "o4": "TLS.", "ans": 2}
            ],
            9: [
                {"q": "Subnets are...?", "o1": "Global", "o2": "Regional", "o3": "Zonal", "o4": "Universal", "ans": 2},
                {"q": "Which IP is internal to the VPC?", "o1": "Public IP", "o2": "Private IP", "o3": "Broadcast IP", "o4": "Google IP", "ans": 2},
                {"q": "What is CIDR notation?", "o1": "A way to define IP ranges", "o2": "A coding language", "o3": "A cloud region", "o4": "A database", "ans": 1},
                {"q": "NEXT LEVEL: Can you expand a subnet's IP range after creation?", "o1": "No.", "o2": "Yes, but you cannot shrink it.", "o3": "Yes, expand and shrink.", "o4": "Only if you delete all VMs.", "ans": 2},
                {"q": "NEXT LEVEL: What are 'Secondary IP Ranges' used for in GKE?", "o1": "External IPs.", "o2": "Alias IPs for Pods and Services.", "o3": "Admin IPs.", "o4": "Backup IPs.", "ans": 2},
                {"q": "NEXT LEVEL: Which CIDR is larger (more IPs)?", "o1": "/24", "o2": "/20", "o3": "/32", "o4": "/16", "ans": 4},
                {"q": "SCENARIO: Subnet 10.0.0.0/24 is running out of IPs. You have 50 VMs, 20 SQL, 30 Pods. Best Fix?", "o1": "Switch to IPv6.", "o2": "Create secondary subnet 10.1.0.0/24.", "o3": "Expand existing subnet to 10.0.0.0/22.", "o4": "Split VPC.", "ans": 3}
            ],
            10: [
                {"q": "Firewalls apply to...?", "o1": "Subnets", "o2": "VM Instances (via tags/SA)", "o3": "Projects", "o4": "Users", "ans": 2},
                {"q": "The default firewall rule for RDP allows traffic on port...", "o1": "80", "o2": "22", "o3": "3389", "o4": "443", "ans": 3},
                {"q": "Are firewall rules stateful?", "o1": "Yes", "o2": "No", "o3": "Only egress", "o4": "Only ingress", "ans": 1},
                {"q": "NEXT LEVEL: You want to block a specific IP from accessing ALL projects in your Organization. What do you use?", "o1": "VPC Firewall Rule.", "o2": "Hierarchical Firewall Policy.", "o3": "Cloud Armor.", "o4": "IAM Policy.", "ans": 2},
                {"q": "NEXT LEVEL: Firewall Log shows traffic is 'Allowed' but your app can't see it. Why?", "o1": "The application itself isn't listening on that port.", "o2": "Firewall logs are fake.", "o3": "Google blocked it.", "o4": "The VM is off.", "ans": 1},
                {"q": "NEXT LEVEL: How do you allow SSH access without opening Port 22 to the public internet?", "o1": "Identity-Aware Proxy (IAP) TCP Forwarding.", "o2": "Open 0.0.0.0/0.", "o3": "Use Telnet.", "o4": "You can't.", "ans": 1}
            ],
            11: [
                {"q": "Which Load Balancer is Global & HTTP(S)?", "o1": "Network Load Balancer", "o2": "Internal Load Balancer", "o3": "Global External HTTP(S) LB", "o4": "TCP Proxy", "ans": 3},
                {"q": "To distribute traffic to VMs in different regions, use...", "o1": "Regional LB", "o2": "Global LB", "o3": "VPN", "o4": "Interconnect", "ans": 2},
                {"q": "What checks the health of backends?", "o1": "Doctor Service", "o2": "Health Check", "o3": "Ping", "o4": "Uptime Check", "ans": 2},
                {"q": "NEXT LEVEL: What feature protects your Backend Service from DDoS attacks?", "o1": "Cloud Armor.", "o2": "Cloud CDN.", "o3": "Cloud NAT.", "o4": "VPC Peering.", "ans": 1},
                {"q": "NEXT LEVEL: You need to route traffic to a private GKE cluster in another VPC. What do you use?", "o1": "VPC Peering.", "o2": "Private Service Connect (PSC).", "o3": "Cloud VPN.", "o4": "External IP.", "ans": 2},
                {"q": "NEXT LEVEL: What is 'Anycast IP'?", "o1": "A random IP.", "o2": "A single IP that is advertised from multiple locations worldwide.", "o3": "A broadcast IP.", "o4": "A private IP.", "ans": 2},
                {"q": "SCENARIO: Backend instances are missing the 'X-Forwarded-For' header. Fix?", "o1": "Use Cloud Armor.", "o2": "Enable it in OS.", "o3": "Configure LB Backend Service to add the header.", "o4": "Firewall rule.", "ans": 3},
                {"q": "SCENARIO: Users in US and EU need lowest latency to their region. Some routing is wrong. Fix?", "o1": "Manual DNS.", "o2": "Global HTTP LB + Traffic Director (Geolocation routing).", "o3": "Session Affinity.", "o4": "Cloud CDN.", "ans": 2},
                {"q": "SCENARIO: You must enforce HTTPS only. Current LB accepts HTTP. Simplest fix?", "o1": "Block Port 80 firewall.", "o2": "LB URL Redirect Policy (HTTP->HTTPS).", "o3": "Disable IP.", "o4": "App code redirect.", "ans": 2}
            ],
            12: [
                {"q": "Cloud NAT allows...", "o1": "Inbound connections only", "o2": "Outbound connection for private VMs", "o3": "VPN connections", "o4": "Public IPs for everyone", "ans": 2},
                {"q": "Cloud Router is used for...", "o1": "Static routing", "o2": "Dynamic routing (BGP)", "o3": "WiFi", "o4": "DNS", "ans": 2},
                {"q": "Which route has the highest priority?", "o1": "1000", "o2": "100", "o3": "0", "o4": "500", "ans": 3},
                {"q": "NEXT LEVEL: How do you grant access based on 'Time of Day'?", "o1": "You can't.", "o2": "Use IAM Conditions (Attribute Based Access Control).", "o3": "Use a cron job.", "o4": "Use Billing Alerts.", "ans": 2},
                {"q": "NEXT LEVEL: Which is safer: Service Account Keys or Workload Identity Federation?", "o1": "Keys.", "o2": "Workload Identity Federation (No long-lived keys).", "o3": "Both are same.", "o4": "None.", "ans": 2},
                {"q": "NEXT LEVEL: What is 'Policy Intelligence'?", "o1": "AI that writes code.", "o2": "Tools like 'IAM Recommender' that suggest removing unused roles.", "o3": "A chatbot.", "o4": "A limit.", "ans": 2}
            ],
            13: [
                {"q": "Q1. You want to deploy a web application to users globally. You need a single IP address that routes users to the closest datacenter. Which Load Balancer should you choose?", "o1": "Network TCP Load Balancer", "o2": "Internal HTTP Load Balancer", "o3": "External Global HTTP(S) Load Balancer", "o4": "UDP Load Balancer", "ans": 3},
                {"q": "Q2. You have a VM in a private subnet. It needs to download security patches from the internet. It must NOT have a public IP address. What do you configure?", "o1": "Cloud VPN", "o2": "Cloud NAT", "o3": "VPC Peering", "o4": "External Load Balancer", "ans": 2},
                {"q": "Q3. A firewall rule with Priority 1000 allows traffic on Port 80. A rule with Priority 100 denies traffic on Port 80. What happens?", "o1": "Traffic is Allowed", "o2": "Traffic is Denied", "o3": "Traffic is allowed only for Admins", "o4": "The rules conflict and error out", "ans": 2},
                {"q": "Q4. Can a VPC span multiple regions?", "o1": "No, VPCs are Zonal", "o2": "No, VPCs are Regional", "o3": "Yes, VPCs are Global", "o4": "Only if you use VPC Peering", "ans": 3},
                {"q": "Q5. You need to restrict access to a database server so only the 'Web Server' group can connect. What is the best practice?", "o1": "Create a firewall rule allowing the specific IP addresses of the web servers", "o2": "Create a firewall rule allowing traffic from 0.0.0.0/0", "o3": "Add a Network Tag 'web-server' to the web VMs, and allow ingress from that Tag", "o4": "Put them in the same Zone", "ans": 3},
                {"q": "Q6. What is the default route (0.0.0.0/0) used for?", "o1": "Routing traffic to the local subnet", "o2": "Routing traffic to the Internet Gateway", "o3": "Routing traffic to Google Services (APIs)", "o4": "Routing traffic to a VPN", "ans": 2},
                {"q": "Q7. Which Load Balancer is best for non-HTTP traffic (e.g., a Database or Gaming Server)?", "o1": "HTTP(S) Load Balancer", "o2": "Network (TCP/UDP) Load Balancer", "o3": "SSL Proxy Load Balancer", "o4": "Cloud CDN", "ans": 2},
                {"q": "Q8. True or False: You can expand the IP range of a subnet after it has been created.", "o1": "True", "o2": "False", "o3": "Only if empty", "o4": "Only if regional", "ans": 1},
                {"q": "Q9. If you delete a VPC, what happens to the Subnets inside it?", "o1": "They are moved to the 'Default' VPC", "o2": "They are deleted", "o3": "They become orphaned resources", "o4": "Nothing, Subnets are independent", "ans": 2},
                {"q": "Q10. You are creating a custom VPC. How many subnets does it have by default?", "o1": "One per region", "o2": "One per zone", "o3": "Zero", "o4": "Ten", "ans": 3}
            ],
            14: [
                {"q": "What is the equation for an IAM Policy?", "o1": "User + Password = Access", "o2": "Principal + Role = Access (Binding)", "o3": "Group + Zone = Permission", "o4": "VM + Disk = Storage", "ans": 2},
                {"q": "Which type of Role is considered a 'Best Practice' to use?", "o1": "Primitive Roles (Owner)", "o2": "Predefined Roles (Least Privilege)", "o3": "Super Admin Roles", "o4": "No Roles", "ans": 2},
                {"q": "If I am an Owner at the Organization level, can a Project Admin deny my access to a specific project?", "o1": "Yes, by adding a Deny rule", "o2": "No, permissions flow down and cannot be blocked by standard IAM (Allow policies are additive).", "o3": "Only if they use a firewall", "o4": "Yes, if the project is private", "ans": 2},
                {"q": "NEXT LEVEL: What is 'Attribute Based Access Control' (ABAC)?", "o1": "Granting access based on Attributes like Time or IP (using Conditions).", "o2": "Granting access to everyone.", "o3": "Granting access based on Job Title.", "o4": "Granting access based on Payment.", "ans": 1},
                {"q": "NEXT LEVEL: If you delete a user from your Google Workspace, what happens to their IAM access?", "o1": "It remains active.", "o2": "It is immediately revoked because they cannot authenticate.", "o3": "It is paused.", "o4": "Google sends an email.", "ans": 2},
                {"q": "NEXT LEVEL: What is the 'Policy Simulator' used for?", "o1": "A game.", "o2": "Testing IAM changes before applying them to see impact.", "o3": " simulating hacks.", "o4": "Training AI.", "ans": 2},
                {"q": "SCENARIO: Developer granted 'Editor' role to a CI/CD Service Account. Security flagged it. Fix?", "o1": "Change to 'Viewer'.", "o2": "Use Personal Account.", "o3": "Create Custom Role with least privilege (e.g. Instance Admin).", "o4": "Use VPC Service Controls.", "ans": 3}
            ],
            15: [
                {"q": "What is a Service Account?", "o1": "A User Account for Google employees", "o2": "An Identity for a robot/application", "o3": "A billing account", "o4": "A secure password", "ans": 2},
                {"q": "What is the most secure way to authenticate an application on a VM?", "o1": "Embed the JSON key in the code", "o2": "Create a text file with the password", "o3": "Attach a Service Account to the VM", "o4": "Login manually every time", "ans": 3},
                {"q": "If you delete a Service Account, what happens to applications using it?", "o1": "They switch to a backup account", "o2": "They break immediately (Auth fails)", "o3": "Nothing", "o4": "Google sends a warning email", "ans": 2},
                {"q": "NEXT LEVEL: What is 'Service Account Impersonation'?", "o1": "A hacker stealing keys.", "o2": "A user creating short-lived credentials to act as the Service Account (safer than keys).", "o3": "A user pretending to be another user.", "o4": "A bug.", "ans": 2},
                {"q": "NEXT LEVEL: You have a stored JSON key for a Service Account. It was leaked to GitHub. What do you do?", "o1": "Panic.", "o2": "Revoke/Delete the key immediately in the Console.", "o3": "Change the password.", "o4": "Delete the VM.", "ans": 2},
                {"q": "SCENARIO: VM logs 'Permission denied' when writing to GCS. VM uses default Service Account. Root cause?", "o1": "Missing 'storage.buckets.get'.", "o2": "Service Account missing 'roles/storage.objectCreator'.", "o3": "Need API Key.", "o4": "Using personal account.", "ans": 2}   
            ],
            16: [
                {"q": "What is the difference between Logging and Monitoring?", "o1": "Logging is for numbers, Monitoring is for text", "o2": "Logging is for text events, Monitoring is for metrics (numbers)", "o3": "They are the same", "o4": "Logging is expensive, Monitoring is free", "ans": 2},
                {"q": "You need to store logs for 5 years. Cloud Logging retains them for 30 days. What do you do?", "o1": "Print them out", "o2": "Create a Log Sink to export to Archive Storage", "o3": "Email them to yourself", "o4": "Upgrade to Premium Logging", "ans": 2},
                {"q": "Which tool would you use to find out why a specific HTTP request took 5 seconds?", "o1": "Cloud Trace", "o2": "Cloud Profiler", "o3": "Cloud Build", "o4": "Cloud Source Repositories", "ans": 1},
                {"q": "NEXT LEVEL: Cloud Profiler helps you...?", "o1": "Find security bugs.", "o2": "Optimize code performance (CPU/RAM usage) to save money.", "o3": "Profile users.", "o4": "Profile disk speed.", "ans": 2},
                {"q": "NEXT LEVEL: What does 'Cloud Error Reporting' do?", "o1": "Sends errors to Google.", "o2": "Groups similar stack traces together so you see '1000 occurrences of NPE' instead of 1000 logs.", "o3": "Deletes errors.", "o4": "Ignores errors.", "ans": 2}
            ],
            17: [
                {"q": "Cloud Shell provides a persistent home directory of what size?", "o1": "1 GB", "o2": "5 GB", "o3": "100 GB", "o4": "Temporary only", "ans": 2},
                {"q": "Which command initializes the gcloud configuration?", "o1": "gcloud start", "o2": "gcloud init", "o3": "gcloud login", "o4": "gcloud go", "ans": 2},
                {"q": "Is Cloud Shell free?", "o1": "No, charged per minute", "o2": "Yes, completely free", "o3": "Free for 1 hour only", "o4": "Only for new users", "ans": 2},
                {"q": "NEXT LEVEL: If you install a tool in the root directory (/) of Cloud Shell, will it persist after a restart?", "o1": "Yes.", "o2": "No, only the $HOME directory is persistent.", "o3": "Yes, if you pay.", "o4": "Maybe.", "ans": 2},
                {"q": "NEXT LEVEL: What is 'Cloud Shell Web Preview'?", "o1": "A browser for Google.", "o2": "A way to view web apps running on port 8080 in Cloud Shell via a proxy URL.", "o3": "A video player.", "o4": "A debugger.", "ans": 2}
            ],
            18: [
                {"q": "Q1. You need to give a consultant read-only access to a specific Cloud Storage bucket. You do not want them to see anything else in the project. What should you do?", "o1": "Assign roles/viewer at the Project level.", "o2": "Assign roles/storage.objectViewer at the Bucket level.", "o3": "Create a Service Account for them.", "o4": "Assign roles/owner at the Bucket level.", "ans": 2},
                {"q": "Q2. Your application running on a VM needs to write data to BigQuery. What is the most secure method to authenticate?", "o1": "Embed a Service Account JSON key in the source code.", "o2": "Store the JSON key in a text file on the VM.", "o3": "Create a Service Account with the BigQuery Data Editor role and attach it to the VM.", "o4": "Use your personal Gmail account credentials.", "ans": 3},
                {"q": "Q3. You want to receive an email notification whenever a specific error message appears in your application logs. Which tool should you use?", "o1": "Cloud Monitoring (Alerting Policy) based on a Log-based Metric.", "o2": "Cloud Trace.", "o3": "Cloud Profiler.", "o4": "VPC Flow Logs.", "ans": 1},
                {"q": "Q4. Who is responsible for securing the underlying physical hardware of the data center?", "o1": "You (The Customer).", "o2": "Google.", "o3": "Both (Shared Responsibility).", "o4": "The ISP.", "ans": 2},
                {"q": "Q5. A user left your company. You deleted their Google Account. What happens to the IAM policies that referenced that user?", "o1": "They act as 'orphaned' entries but effectively deny access.", "o2": "The policies are automatically deleted.", "o3": "The Project is suspended.", "o4": "The user can still log in.", "ans": 1},
                {"q": "Q6. Which command would you use to list all the VMs in your project?", "o1": "gcloud compute instances list", "o2": "gcloud vm show", "o3": "kubectl get pods", "o4": "gsutil ls", "ans": 1},
                {"q": "Q7. You need to store audit logs for 7 years to meet compliance regulations. What should you do?", "o1": "Do nothing; Cloud Logging keeps them forever.", "o2": "Create a Log Sink to export logs to a Cloud Storage bucket with an Archive lifecycle policy.", "o3": "Print them out.", "o4": "Export them to BigQuery.", "ans": 2},
                {"q": "Q8. What is the difference between a Role and a Permission?", "o1": "They are the same.", "o2": "A Role contains many Permissions. You assign Roles to users.", "o3": "A Permission contains many Roles.", "o4": "Permissions are for users; Roles are for robots.", "ans": 2},
                {"q": "Q9. Provide the CLI command to initialize the configuration (login, set project/region).", "o1": "gcloud start", "o2": "gcloud login", "o3": "gcloud init", "o4": "gcloud config set", "ans": 3},
                {"q": "Q10. Can you restrict an IAM Role to be active only during working hours (e.g., 9 AM to 5 PM)?", "o1": "No, IAM is permanent.", "o2": "Yes, using IAM Conditions.", "o3": "Only for Billing roles.", "o4": "Yes, by using a cron job to delete the user every night.", "ans": 2}
            ],
            19: [
                {"q": "Q1. You need to view logs for a specific error. Which tool?", "o1": "Cloud Trace.", "o2": "Cloud Logging.", "o3": "Cloud Profiler.", "o4": "Cloud Monitoring.", "ans": 2},
                {"q": "Q2. You want to be alerted via email when CPU > 90%.", "o1": "Cloud Logging.", "o2": "Cloud Monitoring Alerting Policy.", "o3": "Cloud Trace.", "o4": "Error Reporting.", "ans": 2}
            ],
            20: [
                {"q": "Q1. Security Command Center (SCC) Standard Tier includes?", "o1": "Event Threat Detection.", "o2": "Security Health Analytics (SHA) for common misconfigurations.", "o3": "Container Threat Detection.", "o4": "Compliance Dashboard.", "ans": 2},
                {"q": "Q2. Which tool scans Cloud Storage for Credit Card numbers?", "o1": "Cloud Armor.", "o2": "Cloud DLP (Data Loss Prevention).", "o3": "VPC Service Controls.", "o4": "Identity-Aware Proxy.", "ans": 2}
            ],
            21: [
                 {"q": "Q1. Which command lists all active instances?", "o1": "gcloud compute instances list", "o2": "gcloud list instances", "o3": "gcloud show vms", "o4": "kubectl get pods", "ans": 1},
                 {"q": "Q2. How do you set the default project in Cloud Shell?", "o1": "gcloud config set project [ID]", "o2": "gcloud project set [ID]", "o3": "export PROJECT=[ID]", "o4": "It is automatic", "ans": 1}
            ],
            22: [
                {"q": "Q1. App Engine Standard supports which languages?", "o1": "Any language (Docker).", "o2": "Specific versions of Python, Java, Node, Go, PHP, Ruby.", "o3": "Only Java.", "o4": "Only Go.", "ans": 2},
                {"q": "Q2. When should you choose App Engine Flexible?", "o1": "For immediate scaling to zero.", "o2": "When you need a custom runtime or Docker container.", "o3": "It is cheaper.", "o4": "For static websites.", "ans": 2}
            ],
            23: [
                {"q": "Q1. Cloud Run is based on...?", "o1": "Virtual Machines.", "o2": "Knative (Kubernetes).", "o3": "App Engine.", "o4": "Cloud Functions.", "ans": 2},
                {"q": "Q2. To allow unauthenticated access to Cloud Run, you must...?", "o1": "Do nothing.", "o2": "Add IAM policy binding 'allUsers' -> 'Cloud Run Invoker'.", "o3": "Turn off the firewall.", "o4": "Use a VPC.", "ans": 2}   
            ],
            24: [
                 {"q": "Q1. Which trigger source is used for 'Background' Cloud Functions regarding GCS events?", "o1": "HTTP Trigger.", "o2": "Eventarc / Cloud Storage Notification.", "o3": "Cloud Scheduler.", "o4": "Cloud Tasks.", "ans": 2},
                 {"q": "Q2. Cloud Functions (2nd Gen) allows you to process requests for up to...?", "o1": "9 minutes.", "o2": "60 minutes.", "o3": "30 seconds.", "o4": "24 hours.", "ans": 2}
            ],
            25: [
                {"q": "Q1. In GKE, what manages the Pods?", "o1": "The Master Node (Control Plane).", "o2": "The user.", "o3": "The VPC.", "o4": "Cloud Run.", "ans": 1},
                {"q": "Q2. Difference between GKE Standard and Autopilot?", "o1": "Autopilot manages nodes/security/capacity for you.", "o2": "Standard is free.", "o3": "Standard has no nodes.", "o4": "Autopilot is slower.", "ans": 1}
            ],
            26: [
                 {"q": "Q1. How do you restrict network traffic *between* Pods in GKE?", "o1": "VPC Firewall Rules.", "o2": "Kubernetes Network Policies.", "o3": "Cloud Armor.", "o4": "You cannot.", "ans": 2},
                 {"q": "Q2. What is a GKE 'Private Cluster'?", "o1": "It costs money.", "o2": "Nodes have only Internal IPs and are isolated from public internet.", "o3": "It is for one user only.", "o4": "It runs on your laptop.", "ans": 2}
            ],
            27: [
                {"q": "Q1. Where does Terraform store the knowledge of your resources?", "o1": "In your brain", "o2": "In the State File (.tfstate)", "o3": "It doesn't", "o4": "On Google's servers only", "ans": 2},
                {"q": "Q2. Why store state in a GCS bucket?", "o1": "Cheaper.", "o2": "Locking & consistency for teams.", "o3": "Faster.", "o4": "Required.", "ans": 2}
            ],
            28: [
                {"q": "Q1. Cloud Build configuration is defined in?", "o1": "Dockerfile", "o2": "cloudbuild.yaml", "o3": "Makefile", "o4": "package.json", "ans": 2},
                {"q": "Q2. Where are container images stored?", "o1": "Cloud Storage.", "o2": "Artifact Registry (or Container Registry).", "o3": "Cloud SQL.", "o4": "Local disk.", "ans": 2}
            ],
            29: [
                {"q": "Q1. Which database is best for 'Lift and Shift' of existing MySQL?", "o1": "Cloud Spanner.", "o2": "Cloud SQL.", "o3": "BigQuery.", "o4": "Firestore.", "ans": 2},
                {"q": "Q2. What is AlloyDB?", "o1": "A NoSQL DB.", "o2": "A PostgreSQL-compatible DB with high performance & availability.", "o3": "A Redis cache.", "o4": "A tape storage.", "ans": 2}
            ],
            30: [
                 {"q": "Q1. When do you choose Spanner over Cloud SQL?", "o1": "To save money.", "o2": "For Global Scale + Strong Consistency (Relational).", "o3": "For NoSQL data.", "o4": "For caching.", "ans": 2},
                 {"q": "Q2. What is the anti-pattern in Bigtable Schema design?", "o1": "Tall and narrow tables.", "o2": "Hotspotting (Sequential keys).", "o3": "Using wide columns.", "o4": "Storing time-series.", "ans": 2}
            ],
            31: [
                 {"q": "Q1. BigQuery uses which language?", "o1": "Java.", "o2": "Standard SQL.", "o3": "Python.", "o4": "Go.", "ans": 2},
                 {"q": "Q2. BigQuery storage cost is cheaper for...?", "o1": "Active storage (90 days).", "o2": "Long-term storage (>90 days no modification).", "o3": "Tables starting with 'A'.", "o4": "It is flat rate.", "ans": 2}
            ],
            32: [
                {"q": "Q1. Dataflow is best for?", "o1": "Running existing Hadoop clusters.", "o2": "New Serverless Streaming/Batch pipelines (Apache Beam).", "o3": "Hosting websites.", "o4": "Storing video.", "ans": 2},
                {"q": "Q2. Dataproc is best for?", "o1": "Migrating existing Spark/Hadoop jobs to Managed Hadoop.", "o2": "Serverless ETL.", "o3": "Global messaging.", "o4": "NoSQL.", "ans": 1}
            ],
            33: [
                {"q": "Q1. Pub/Sub pattern is...?", "o1": "Point-to-Point.", "o2": "Publisher-Subscriber (Many-to-Many Decoupled).", "o3": "Request-Response.", "o4": "Batch.", "ans": 2},
                {"q": "Q2. Push vs Pull subscription?", "o1": "Push sends to an endpoint (webhook). Pull requires subscriber to ask.", "o2": "They are same.", "o3": "Push is slower.", "o4": "Pull is deprecated.", "ans": 1}
            ],
            34: [
                 {"q": "Q1. Vertex AI Feature Store allows you to...?", "o1": "Build UI.", "o2": "Share and reuse ML features across teams.", "o3": "Store Docker images.", "o4": "Back up VMs.", "ans": 2},
                 {"q": "Q2. AutoML is for...?", "o1": "Experts who want full control.", "o2": "Users with limited ML expertise (No-code model training).", "o3": "Robots.", "o4": "Self-driving cars.", "ans": 2}  
            ],
            35: [
                 {"q": "Q1. Database Migration Service (DMS) supports continuous replication via...?", "o1": "Snapshots.", "o2": "Change Data Capture (CDC).", "o3": "Copy-paste.", "o4": "FTP.", "ans": 2}
            ],
            36: [
                 {"q": "Q1. What is an Error Budget?", "o1": "Money you pay when you fail.", "o2": "100% minus your SLO. The amount of failure you can tolerate.", "o3": "The developer salary.", "o4": "A budget for buying errors.", "ans": 2}
            ],
            37: [
                {"q": "Q1. If a BigQuery query scans 1TB, how much does it cost (On-Demand)?", "o1": "$1.", "o2": "~$5.", "o3": "$50.", "o4": "$0.", "ans": 2},
                {"q": "Q2. How do you visualize GCP costs?", "o1": "Cloud Billing Reports.", "o2": "Compute Engine.", "o3": "VPC Flow Logs.", "o4": "IAM.", "ans": 1}
            ],
            38: [
                {"q": "Q1. Cloud Armor is a...?", "o1": "WAF & DDoS Protection service.", "o2": "Antivirus.", "o3": "VPN.", "o4": "Password manager.", "ans": 1},
                {"q": "Q2. BeyondCorp represents which security model?", "o1": "Castle and Moat.", "o2": "Zero Trust.", "o3": "Trust but Verify.", "o4": "Open Access.", "ans": 2}
            ],
            39: [
                {"q": "Q1. Mountkirk Games needed global scale. They chose?", "o1": "Preemptible VMs.", "o2": "Managed Instance Groups (MIGs) + Global LB + Spanner/Datastore.", "o3": "A single giant VM.", "o4": "Cloud CDN only.", "ans": 2}
            ],
            40: [
                {"q": "Scenario: A developer needs full control over the operating system to install custom software.\n\nQuestion: Which GCP service should be used?", "o1": "Cloud Run", "o2": "App Engine Standard", "o3": "Compute Engine", "o4": "Cloud Functions", "ans": 3},
                {"q": "Scenario: You want a user to view resources but not modify anything.\n\nQuestion: Which IAM role is appropriate?", "o1": "Owner", "o2": "Editor", "o3": "Viewer", "o4": "Security Admin", "ans": 3},
                {"q": "Scenario: You want to store large media files cheaply with high durability.\n\nQuestion: Which service should you use?", "o1": "Persistent Disk", "o2": "Filestore", "o3": "Cloud Storage", "o4": "Bigtable", "ans": 3},
                {"q": "Scenario: Your app must automatically scale to zero and requires minimal ops effort.\n\nQuestion: Which service should you choose?", "o1": "Compute Engine", "o2": "GKE Standard", "o3": "App Engine Flexible", "o4": "Cloud Run", "ans": 4},
                {"q": "Scenario: A MySQL database needs automated backups and high availability.\n\nQuestion: Which service should be used?", "o1": "Compute Engine + MySQL", "o2": "Cloud SQL", "o3": "Firestore", "o4": "Bigtable", "ans": 2},
                {"q": "Scenario: VMs without public IPs must access Google APIs.\n\nQuestion: What should you enable?", "o1": "Cloud NAT", "o2": "Private Google Access", "o3": "VPN", "o4": "Interconnect", "ans": 2},
                {"q": "Scenario: A globally distributed system requires strong consistency and SQL.\n\nQuestion: Which database should be used?", "o1": "Cloud SQL", "o2": "Firestore", "o3": "Bigtable", "o4": "Cloud Spanner", "ans": 4},
                {"q": "Scenario: You want VMs that automatically heal and scale.\n\nQuestion: Which feature provides this?", "o1": "Single VM", "o2": "Managed Instance Group", "o3": "App Engine", "o4": "Cloud Functions", "ans": 2},
                {"q": "Scenario: A static website must be globally accessible at low cost.\n\nQuestion: Best architecture?", "o1": "Compute Engine", "o2": "Cloud Storage + HTTPS Load Balancer", "o3": "App Engine Flexible", "o4": "GKE", "ans": 2},
                {"q": "Scenario: You need to know who deleted a VM.\n\nQuestion: Which log should you check?", "o1": "Cloud Monitoring", "o2": "VPC Flow Logs", "o3": "Cloud Audit Logs", "o4": "Error Reporting", "ans": 3},
                {"q": "Scenario: You want to restrict a service account to read objects only.\n\nQuestion: Which role should you grant?", "o1": "Storage Admin", "o2": "Storage Object Admin", "o3": "Storage Object Viewer", "o4": "Editor", "ans": 3},
                {"q": "Scenario: You want Kubernetes without managing nodes.\n\nQuestion: Which option is best?", "o1": "GKE Standard", "o2": "GKE Autopilot", "o3": "Compute Engine", "o4": "Cloud Run", "ans": 2},
                {"q": "Scenario: You need shared storage across multiple VMs.\n\nQuestion: Which service?", "o1": "Persistent Disk", "o2": "Filestore", "o3": "Cloud Storage", "o4": "Bigtable", "ans": 2},
                {"q": "Scenario: You need lowest-cost compute for fault-tolerant batch jobs.\n\nQuestion: What should you use?", "o1": "Standard VM", "o2": "Preemptible VM", "o3": "GKE Autopilot", "o4": "App Engine", "ans": 2},
                {"q": "Scenario: You want network traffic logs for auditing.\n\nQuestion: What should you enable?", "o1": "Cloud Audit Logs", "o2": "VPC Flow Logs", "o3": "Stackdriver Logging", "o4": "Error Reporting", "ans": 2}
            ],
            41: [
                {"q": "Scenario: You need to allow traffic only from IP range 203.0.113.0/24 to a VM on port 443.\n\nQuestion: What should you configure?", "o1": "Route", "o2": "Firewall rule", "o3": "Load balancer", "o4": "VPC peering", "ans": 2},
                {"q": "Scenario: A VM without public IP needs internet access for OS updates.\n\nQuestion: What should you use?", "o1": "VPN", "o2": "Interconnect", "o3": "Cloud NAT", "o4": "Private Google Access", "ans": 3},
                {"q": "Scenario: Multiple projects must share a central VPC while keeping billing separate.\n\nQuestion: Which feature should you use?", "o1": "VPC peering", "o2": "Shared VPC", "o3": "VPN", "o4": "Interconnect", "ans": 2},
                {"q": "Scenario: You want to enforce VM labels across all projects.\n\nQuestion: Where should this be configured?", "o1": "Project IAM", "o2": "Firewall rules", "o3": "Organization Policy", "o4": "Cloud Monitoring", "ans": 3},
                {"q": "Scenario: A team needs time-based IAM access to a bucket.\n\nQuestion: What should you use?", "o1": "Custom role", "o2": "IAM Conditions", "o3": "Signed URLs", "o4": "Storage Admin", "ans": 2},
                {"q": "Scenario: You need HTTP(S) load balancing across regions.\n\nQuestion: Which load balancer should you choose?", "o1": "Internal TCP/UDP", "o2": "Network Load Balancer", "o3": "HTTP(S) Load Balancer", "o4": "Internal HTTP(S)", "ans": 3},
                {"q": "Scenario: You want health checks to auto-replace unhealthy VMs.\n\nQuestion: Which component enables this?", "o1": "Instance template", "o2": "Managed Instance Group", "o3": "Firewall rule", "o4": "Snapshot", "ans": 2},
                {"q": "Scenario: You want automated daily backups of a VM disk.\n\nQuestion: What should you configure?", "o1": "Snapshots", "o2": "Images", "o3": "Persistent disk resize", "o4": "Filestore", "ans": 1},
                {"q": "Scenario: You want to store logs long-term for analytics.\n\nQuestion: Where should logs be exported?", "o1": "Cloud Monitoring", "o2": "Cloud Storage", "o3": "BigQuery", "o4": "Error Reporting", "ans": 3},
                {"q": "Scenario: A batch job can tolerate interruptions and must be cheap.\n\nQuestion: Best compute option?", "o1": "Standard VM", "o2": "Committed Use VM", "o3": "Preemptible VM", "o4": "Cloud Run", "ans": 3},
                {"q": "Scenario: You want to prevent accidental project deletion.\n\nQuestion: What should you use?", "o1": "IAM Viewer", "o2": "Org Policy constraint", "o3": "Firewall rule", "o4": "Budget alert", "ans": 2},
                {"q": "Scenario: A service account key was accidentally exposed.\n\nQuestion: What is the FIRST action?", "o1": "Delete project", "o2": "Rotate key", "o3": "Change role", "o4": "Ignore", "ans": 2},
                {"q": "Scenario: You want serverless event-driven execution.\n\nQuestion: Which service should you use?", "o1": "Compute Engine", "o2": "Cloud Run", "o3": "Cloud Functions", "o4": "GKE", "ans": 3},
                {"q": "Scenario: You want budget alerts when spending exceeds 80%.\n\nQuestion: What should you configure?", "o1": "Quotas", "o2": "IAM", "o3": "Budgets & alerts", "o4": "Billing export", "ans": 3},
                {"q": "Scenario: You want rolling updates with zero downtime.\n\nQuestion: Which deployment method?", "o1": "Recreate", "o2": "Blue/Green", "o3": "Rolling update", "o4": "Stop/start VM", "ans": 3},
                {"q": "Scenario: You need private connectivity from on-prem to GCP.\n\nQuestion: Which solution is fastest to set up?", "o1": "Interconnect", "o2": "VPN", "o3": "Peering", "o4": "NAT", "ans": 2},
                {"q": "Scenario: You want strict least privilege for a custom workflow.\n\nQuestion: What should you create?", "o1": "Editor role", "o2": "Owner role", "o3": "Custom IAM role", "o4": "Viewer role", "ans": 3},
                {"q": "Scenario: You need shared NFS storage for GKE.\n\nQuestion: Which service?", "o1": "Persistent Disk", "o2": "Filestore", "o3": "Cloud Storage", "o4": "Bigtable", "ans": 2},
                {"q": "Scenario: You want to monitor VM CPU usage.\n\nQuestion: Which service?", "o1": "Cloud Logging", "o2": "Cloud Monitoring", "o3": "Error Reporting", "o4": "Trace", "ans": 2},
                {"q": "Scenario: An internal app must be load balanced within VPC only.\n\nQuestion: Which LB should you use?", "o1": "External HTTP(S)", "o2": "Internal TCP/UDP", "o3": "Network LB", "o4": "External TCP", "ans": 2},
                {"q": "Scenario: You want to prevent VM creation without labels.\n\nQuestion: What enforces this?", "o1": "IAM", "o2": "Firewall", "o3": "Organization Policy", "o4": "Monitoring", "ans": 3},
                {"q": "Scenario: A Firestore database needs strong consistency.\n\nQuestion: Which mode?", "o1": "Datastore mode", "o2": "Native mode", "o3": "Bigtable", "o4": "Cloud SQL", "ans": 2},
                {"q": "Scenario: A service must authenticate to another GCP service securely.\n\nQuestion: Best practice?", "o1": "API key", "o2": "Service account impersonation", "o3": "Hardcoded credentials", "o4": "User login", "ans": 2},
                {"q": "Scenario: You want alerts when a service is down.\n\nQuestion: What should you configure?", "o1": "Logs", "o2": "Uptime check", "o3": "Trace", "o4": "Debugger", "ans": 2},
                {"q": "Scenario: You want automatic SSL certificates.\n\nQuestion: What should you use?", "o1": "Self-signed cert", "o2": "Managed SSL cert", "o3": "VPN cert", "o4": "IAM", "ans": 2},
                {"q": "Scenario: Logs must be retained for 7 years.\n\nQuestion: What should you use?", "o1": "Logging retention", "o2": "BigQuery sink", "o3": "Error Reporting", "o4": "Monitoring", "ans": 2},
                {"q": "Scenario: You want to lower VM costs automatically over time.\n\nQuestion: Which discount applies?", "o1": "Committed use", "o2": "Sustained use", "o3": "Preemptible", "o4": "Free tier", "ans": 2},
                {"q": "Scenario: You want predictable discounts for 3 years.\n\nQuestion: Which option?", "o1": "Sustained use", "o2": "Committed use", "o3": "Preemptible", "o4": "Budget", "ans": 2},
                {"q": "Scenario: You want to troubleshoot application crashes.\n\nQuestion: Which tool?", "o1": "Monitoring", "o2": "Logging", "o3": "Error Reporting", "o4": "Trace", "ans": 3},
                {"q": "Scenario: You want a container platform with full control.\n\nQuestion: Which option?", "o1": "Cloud Run", "o2": "GKE Standard", "o3": "App Engine", "o4": "Cloud Functions", "ans": 2},
                {"q": "Scenario: You want zero-trust access to internal apps.\n\nQuestion: Which service?", "o1": "VPN", "o2": "Cloud IAP", "o3": "Firewall", "o4": "NAT", "ans": 2},
                {"q": "Scenario: You want immutable VM deployments.\n\nQuestion: What should you use?", "o1": "Startup scripts", "o2": "Instance templates", "o3": "SSH access", "o4": "Resize disk", "ans": 2},
                {"q": "Scenario: You want to control firewall evaluation order.\n\nQuestion: What determines priority?", "o1": "Name", "o2": "Creation time", "o3": "Priority number", "o4": "Network tag", "ans": 3},
                {"q": "Scenario: You want audit logs across all projects.\n\nQuestion: Where configure?", "o1": "Project level", "o2": "Folder level", "o3": "Organization level", "o4": "IAM role", "ans": 3},
                {"q": "Scenario: You want fast key-value lookups at scale.\n\nQuestion: Which database?", "o1": "Firestore", "o2": "Cloud SQL", "o3": "Bigtable", "o4": "Spanner", "ans": 3},
                {"q": "Scenario: You want to debug live app code without redeploying.\n\nQuestion: Which tool?", "o1": "Logging", "o2": "Debugger", "o3": "Monitoring", "o4": "Trace", "ans": 2},
                {"q": "Scenario: A workload needs millisecond latency worldwide.\n\nQuestion: Best solution?", "o1": "Cloud SQL", "o2": "Firestore", "o3": "Spanner", "o4": "Bigtable", "ans": 3},
                {"q": "Scenario: You want to prevent accidental deletion of storage.\n\nQuestion: What should you enable?", "o1": "Versioning", "o2": "Lifecycle rules", "o3": "IAM", "o4": "Monitoring", "ans": 1},
                {"q": "Scenario: You want temporary access to private objects.\n\nQuestion: What should you use?", "o1": "IAM Viewer", "o2": "Signed URLs", "o3": "Public bucket", "o4": "ACL", "ans": 2},
                {"q": "Scenario: You want to minimize operational overhead.\n\nQuestion: Which compute option?", "o1": "Compute Engine", "o2": "GKE Standard", "o3": "Cloud Run", "o4": "VM MIG", "ans": 3},
                {"q": "Scenario: A company requires separation of duties.\n\nQuestion: Best practice?", "o1": "Owner role", "o2": "Editor role", "o3": "Custom IAM roles", "o4": "Shared accounts", "ans": 3},
                {"q": "Scenario: You want to trace slow HTTP requests.\n\nQuestion: Which tool?", "o1": "Logging", "o2": "Trace", "o3": "Monitoring", "o4": "Debugger", "ans": 2},
                {"q": "Scenario: You want to stop runaway costs immediately.\n\nQuestion: What should you configure?", "o1": "Quotas", "o2": "Budgets", "o3": "IAM", "o4": "Logs", "ans": 1},
                {"q": "Scenario: You want blue/green deployment with instant rollback.\n\nQuestion: Which strategy?", "o1": "Rolling", "o2": "Canary", "o3": "Blue/Green", "o4": "Recreate", "ans": 3},
                {"q": "Scenario: You want centralized security governance.\n\nQuestion: Which level should IAM be managed?", "o1": "Resource", "o2": "Project", "o3": "Folder", "o4": "Organization", "ans": 4}
            ]
        }

        # No Filler Logic neeeded anymore, we cover 1-41.
        # But keeping a safe fallback just in case
        for day_num in range(1, 42):
             if day_num not in quiz_data:
                # Should not happen given the updates above, but safe
                 quiz_data[day_num] = [
                    {"q": f"Q1: Content is loading for Day {day_num}...", "o1": "Ok", "o2": "Ok", "o3": "Ok", "o4": "Ok", "ans": 1}
                ]

        for day_num, questions in quiz_data.items():
            try:
                day = Day.objects.get(number=day_num)
                # Clear existing old questions to avoid duplicates if re-run
                day.quiz_questions.all().delete()
                
                for q in questions:
                    QuizQuestion.objects.create(
                        day=day,
                        question_text=q['q'],
                        option_1=q['o1'],
                        option_2=q['o2'],
                        option_3=q['o3'],
                        option_4=q['o4'],
                        correct_option=q['ans'],
                        explanation=q.get('explanation', '')
                    )
                self.stdout.write(self.style.SUCCESS(f'Created quiz for Day {day_num}'))
            except Day.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Day {day_num} not found, skipping.'))

        self.stdout.write(self.style.SUCCESS('All quizzes refreshed.'))
