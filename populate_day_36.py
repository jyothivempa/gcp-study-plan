import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz_part6():
    try:
        day = Day.objects.get(number=36)
    except Day.DoesNotExist:
        print("Day 36 not found.")
        return

    questions = [
        {
            "q": "You have an application that uses Cloud Spanner as a database backend to keep current state information about users. Cloud Bigtable logs all events triggered by users. You export Cloud Spanner data to Cloud Storage during daily backups. One of your analysts asks you to join data from Cloud Spanner and Cloud Bigtable for specific users. You want to complete this ad hoc request as efficiently as possible. What should you do?",
            "o1": "Use BigQuery to process the data. Create a Federated Table for the Spanner export (Avro/CSV) and a Federated Table for Bigtable, then JOIN them.",
            "o2": "Load data into Cloud SQL.",
            "o3": "Write a Dataflow job.",
            "o4": "Use Dataproc.",
            "ans": 1
        },
        {
            "q": "You are hosting an application from Compute Engine Virtual Machines (VMs) in us-central1-a. You want to adjust your design to support the failure of a single Compute Engine zone, eliminate downtime, and minimize cost. What should you do?",
            "o1": "Create a Managed Instance Group (MIG) and select 'Multiple zones' (Regional MIG).",
            "o2": "Create a Snapshot schedule.",
            "o3": "Create a second VM in another zone and failover manually.",
            "o4": "Use App Engine.",
            "ans": 1
        },
        {
            "q": "A colleague handed over a Google Cloud Platform project for you to maintain. As part of a security checkup, you want to review who has been granted the Project Owner role. What should you do?",
            "o1": "Use the IAM & Admin page in the Console and filter by Role: Owner.",
            "o2": "Check the Activity Log.",
            "o3": "Check Deployment Manager.",
            "o4": "Run 'gcloud compute instances describe'.",
            "ans": 1
        },
        {
            "q": "You are running multiple VPC-native Google Kubernetes Engine clusters in the same subnet. The IPs available for the nodes are exhausted, and you want to ensure that the clusters can grow in nodes when needed. What should you do?",
            "o1": "Expand the subnet's primary CIDR range (if using a large enough Private RFC range initially) or create a new subnet/node pool.",
            "o2": "You cannot expand a subnet. Create a new VPC.",
            "o3": "Use Public IPs.",
            "o4": "Delete other clusters.",
            "ans": 1
        },
        {
            "q": "You have a batch workload that runs every night and uses a large number of Virtual Machines (VMs). It is fault-tolerant and can tolerate some of the VMs being terminated. The current cost of VMs is too high. What should you do?",
            "o1": "Use Preemptible VMs (Spot VMs) in a Managed Instance Group.",
            "o2": "Use Custom Machine Types.",
            "o3": "Use Committed Use Discounts.",
            "o4": "Use Shielded VMs.",
            "ans": 1
        },
        {
            "q": "You are working with a user to set up an application in a new VPC behind a firewall. The user is concerned about data egress. You want to configure the fewest open egress ports. What should you do?",
            "o1": "Block all egress traffic and allow only necessary ports (Deny All implied, create Allow rules).",
            "o2": "Allow all egress.",
            "o3": "Use Cloud IAP.",
            "o4": "Use Cloud Armor.",
            "ans": 1
        },
        {
            "q": "Your company runs its Linux workloads on Compute Engine instances. Your company will be working with a new operations partner that does not use Google Accounts. You need to grant access to the instances to your operations partner so they can maintain the installed tooling. What should you do?",
            "o1": "Ask the partner for their public SSH keys and add them to the Project/Instance Metadata.",
            "o2": "Create Google Accounts for them.",
            "o3": "Share the root password.",
            "o4": "Use OS Login.",
            "ans": 1
        },
        {
            "q": "You have created a code snippet that should be triggered whenever a new file is uploaded to a Cloud Storage bucket. You want to deploy this code snippet. What should you do?",
            "o1": "Deploy a Cloud Function triggered by 'google.storage.object.finalize'.",
            "o2": "Use App Engine.",
            "o3": "Use Cloud Run directly.",
            "o4": "Use a VM with a cron job.",
            "ans": 1
        },
        {
            "q": "You have been asked to set up Object Lifecycle Management for objects stored in storage buckets. The objects are written once and accessed frequently for 30 days. After 30 days, the objects are not read again unless there is a special need. The objects should be kept for three years, and you need to minimize cost. What should you do?",
            "o1": "Set a Lifecycle rule: Age > 30 days -> Set to Archive (or Coldline).",
            "o2": "Set a Lifecycle rule: Age > 30 days -> Delete.",
            "o3": "Use Nearline immediately.",
            "o4": "Use Multi-Regional bucket.",
            "ans": 1
        },
        {
            "q": "You are storing sensitive information in a Cloud Storage bucket. For legal reasons, you need to be able to record all requests that read any of the stored data. You want to make sure you comply with these requirements. What should you do?",
            "o1": "Enable Data Access Logs (Audit Logs) for the Cloud Storage bucket.",
            "o2": "Enable Admin Activity Logs.",
            "o3": "Enable Versioning.",
            "o4": "Use Cloud Trace.",
            "ans": 1
        },
        {
            "q": "You are the team lead of a group of 10 developers. You provided each developer with an individual Google Cloud Project that they can use as their personal sandbox to experiment with different Google Cloud solutions. You want to be notified if any of the developers are spending above $500 per month on their sandbox environment. What should you do?",
            "o1": "Set a Budget Alert for 500, grouped by Project, and select 'Email to Billing Admins/Users'.",
            "o2": "Check the Billing report daily.",
            "o3": "Use Cloud Functions.",
            "o4": "Set a Quota.",
            "ans": 1
        },
        {
            "q": "You are deploying a production application on Compute Engine. You want to prevent anyone from accidentally destroying the instance by clicking the wrong button. What should you do?",
            "o1": "Enable 'Deletion Protection' in the instance properties.",
            "o2": "Revoke Editor role.",
            "o3": "Use a Shielded VM.",
            "o4": "Use a Preemptible VM.",
            "ans": 1
        },
        {
            "q": "Your company uses a large number of Google Cloud services centralized in a single project. All teams have specific projects for testing and development. The DevOps team needs access to all of the production services in order to perform their job. You want to prevent Google Cloud product changes from broadening their permissions in the future. You want to follow Google-recommended practices. What should you do?",
            "o1": "Create a Custom Role with the specific permissions required.",
            "o2": "Grant 'Project Editor' role.",
            "o3": "Grant 'Project Owner' role.",
            "o4": "Use Basic Roles.",
            "ans": 1
        },
        {
            "q": "You are building an application that processes data files uploaded from thousands of suppliers. Your primary goals for the application are data security and the expiration of aged data. You need to design the application to: Restrict access so that suppliers can access only their own data. Give suppliers write access to data only for 30 minutes. Delete data that is over 45 days old. You have a very short development cycle, and you need to make sure that the application requires minimal maintenance. Which two strategies should you use? (Choose two.)",
            "o1": "Use Signed URLs (for temp access) and Object Lifecycle Management (for expiry).",
            "o2": "Use ACLs and Cron jobs.",
            "o3": "Use IAM Conditions and Cloud Functions.",
            "o4": "Use a dedicated bucket for each supplier.",
            "ans": 1
        },
        {
            "q": "Your company wants to standardize the creation and management of multiple Google Cloud resources using Infrastructure as Code. You want to minimize the amount of repetitive code needed to manage the environment. What should you do?",
            "o1": "Use Terraform modules or Deployment Manager templates.",
            "o2": "Use simple shell scripts.",
            "o3": "Use the Cloud Console.",
            "o4": "Clone repositories.",
            "ans": 1
        },
        {
            "q": "You are performing a monthly security check of your Google Cloud environment and want to know who has access to view data stored in your Google Cloud Project. What should you?",
            "o1": "Use the IAM Policy Analyzer (Network Intelligence Center) or review IAM roles.",
            "o2": "Check Cloud Storage logs.",
            "o3": "Ask the team.",
            "o4": "Check Billing.",
            "ans": 1
        },
        {
            "q": "Your company has embraced a hybrid cloud strategy where some of the applications are deployed on Google Cloud. A Virtual Private Network (VPN) tunnel connects your Virtual Private Cloud (VPC) in Google Cloud with your company's on-premises network. Multiple applications in Google Cloud need to connect to an on-premises database server, and you want to avoid having to change the IP configuration in all of your applications when the IP of the database changes. What should you do?",
            "o1": "Configure Cloud DNS with a private zone (forwarding zone) to resolve the on-premises database hostname.",
            "o2": "Use a hardcoded IP.",
            "o3": "Use /etc/hosts.",
            "o4": "Use Cloud NAT.",
            "ans": 1
        },
        {
            "q": "You have developed a containerized web application that will serve internal colleagues during business hours. You want to ensure that no costs are incurred outside of the hours the application is used. You have just created a new Google Cloud project and want to deploy the application. What should you do?",
            "o1": "Use Cloud Run (fully managed). It scales to 0 when not requested.",
            "o2": "Use GKE.",
            "o3": "Use App Engine Flexible.",
            "o4": "Use Compute Engine.",
            "ans": 1
        },
        {
            "q": "You have experimented with Google Cloud using your own credit card and expensed the costs to your company. Your company wants to streamline the billing process and charge the costs of your projects to their monthly invoice. What should you do?",
            "o1": "Change the Billing Account of your projects to the Company's Billing Account.",
            "o2": "Transfer the project ownership.",
            "o3": "Delete the project and recreate it.",
            "o4": "Send the invoice to Finance.",
            "ans": 1
        },
        {
            "q": "You are running a data warehouse on BigQuery. A partner company is offering a recommendation engine based on the data in your data warehouse. The partner company is also running their application on Google Cloud. They manage the resources in their own project, but they need access to the BigQuery dataset in your project. You want to provide the partner company with access to the dataset. What should you do?",
            "o1": "Grant the 'BigQuery Data Viewer' role to the Service Account of the partner.",
            "o2": "Make the dataset public.",
            "o3": "Use Cloud VPN.",
            "o4": "Copy data to their project.",
            "ans": 1
        },
        {
            "q": "Your web application has been running successfully on Cloud Run for Anthos. You want to evaluate an updated version of the application with a specific percentage of your production users (canary deployment). What should you do?",
            "o1": "Use Cloud Run traffic splitting features (revisons).",
            "o2": "Use Istio/Anthos Service Mesh traffic management.",
            "o3": "Deploy a new service.",
            "o4": "Use DNS round robin.",
            "ans": 1
        },
        {
            "q": "Your company developed a mobile game that is deployed on Google Cloud. Gamers are connecting to the game with their personal phones over the Internet. The game sends UDP packets to update the servers about the gamers' actions while they are playing in multiplayer mode. Your game backend can scale over multiple Virtual Machines (VMs), and you want to expose the VMs over a single IP address. What should you do?",
            "o1": "Use External Network Load Balancing (UDP).",
            "o2": "Use HTTP(S) Load Balancing.",
            "o3": "Use SSL Proxy.",
            "o4": "Use Internal Load Balancing.",
            "ans": 1
        },
        {
            "q": "You are working for a hospital that stores its medical images in an on-premises data room. The hospital wants to use Cloud Storage for archival storage of these images. The hospital wants an automated process to upload any new medical images to Cloud Storage. You need to design and implement a solution. What should you do?",
            "o1": "Write a script using 'gsutil rsync' scheduled via cron.",
            "o2": "Use Transfer Service for On-premises Data.",
            "o3": "Drag and drop in Console.",
            "o4": "Use BigQuery.",
            "ans": 1
        },
        {
            "q": "Your auditor wants to view your organization's use of data in Google Cloud. The auditor is most interested in auditing who accessed data in Cloud Storage buckets. You need to help the auditor access the data they need. What should you do?",
            "o1": "Enable Data Access Logs for Cloud Storage and grant the auditor access to view logs.",
            "o2": "Check IAM roles.",
            "o3": "Check Usage logs.",
            "o4": "Check Billing.",
            "ans": 1
        },
        {
            "q": "You received a JSON file that contained a private key of a Service Account in order to get access to several resources in a Google Cloud project. You downloaded and installed the Cloud SDK and want to use this private key for authentication and authorization when performing gcloud commands. What should you do?",
            "o1": "Run 'gcloud auth activate-service-account --key-file=KEY_FILE'.",
            "o2": "Run 'gcloud auth login'.",
            "o3": "Place the file in ~/.gcloud/keys.",
            "o4": "Set GOOGLE_APPLICATION_CREDENTIALS.",
            "ans": 1
        },
        {
            "q": "You are working with a Cloud SQL MySQL database at your company. You need to retain a month-end copy of the database for three years for audit purposes. What should you do?",
            "o1": "Export the database to Cloud Storage (SQL dump) and set appropriate Lifecycle rules.",
            "o2": "Use Automated Backups (retention max is 1 year usually/limited).",
            "o3": "Keep the instance running for 3 years.",
            "o4": "Use BigQuery.",
            "ans": 1
        },
        {
            "q": "You are monitoring an application and receive user feedback that a specific error is spiking. You notice that the error is caused by a Service Account having insufficient permissions. You are able to solve the problem but want to be notified if the problem recurs. What should you do?",
            "o1": "Create a Log-based Metric for the error and create an Alerting Policy on it.",
            "o2": "Check logs daily.",
            "o3": "Use Error Reporting.",
            "o4": "Ask users to email you.",
            "ans": 1
        },
        {
            "q": "You are developing a financial trading application that will be used globally. Data is stored and queried using a relational structure, and clients from all over the world should get the exact identical state of the data. The application will be deployed in multiple regions to provide the lowest latency to end users. You need to select a storage option for the application data while minimizing latency. What should you do?",
            "o1": "Cloud Spanner (Global consistency, relational).",
            "o2": "Cloud SQL (Regional).",
            "o3": "BigQuery.",
            "o4": "Firestore.",
            "ans": 1
        },
        {
            "q": "You are about to deploy a new Enterprise Resource Planning (ERP) system on Google Cloud. The application holds the full database in-memory for fast data access, and you need to configure the most appropriate resources on Google Cloud for this application. What should you do?",
            "o1": "Use Compute Engine Memory-optimized machine types (M1 or M2).",
            "o2": "Use n1-highcpu.",
            "o3": "Use Cloud Run.",
            "o4": "Use App Engine.",
            "ans": 1
        },
        {
            "q": "You have developed an application that consists of multiple microservices, with each microservice packaged in its own Docker container image. You want to deploy the entire application on Google Kubernetes Engine so that each microservice can be scaled individually. What should you do?",
            "o1": "Create a separate Deployment for each microservice.",
            "o2": "Put all containers in one Pod.",
            "o3": "Use a single large Deployment.",
            "o4": "Use a DaemonSet.",
            "ans": 1
        }
    ]

    for q in questions:
        QuizQuestion.objects.create(
            day=day,
            question_text=q['q'],
            option_1=q['o1'],
            option_2=q['o2'],
            option_3=q['o3'],
            option_4=q['o4'],
            correct_option=q['ans']
        )
    
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 6).")

if __name__ == "__main__":
    populate_quiz_part6()
