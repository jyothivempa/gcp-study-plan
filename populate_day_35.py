import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz_part5():
    try:
        day = Day.objects.get(number=35)
    except Day.DoesNotExist:
        print("Day 35 not found.")
        return

    questions = [
        {
            "q": "You are configuring service accounts for an application that spans multiple projects. Virtual Machines (VMs) running in the web-applications project need access to BigQuery datasets in crm-databases-proj. You want to follow Google-recommended practices to give access to the service account in the web-applications project. What should you do?",
            "o1": "In crm-databases-proj, grant the 'BigQuery Data Viewer' role to the Service Account email of the web-applications VMs.",
            "o2": "Create a service account in crm-databases-proj and download the key.",
            "o3": "Peer the VPCs.",
            "o4": "Make the dataset public.",
            "ans": 1
        },
        {
            "q": "An employee was terminated, but their access to Google Cloud Platform (GCP) was not removed until 2 weeks later. You need to find out this employee accessed any sensitive customer information after their termination. What should you do?",
            "o1": "Search Data Access logs in Cloud Logging for the user's email.",
            "o2": "Search Admin Activity logs.",
            "o3": "Check the IAM policy.",
            "o4": "Ask the employee.",
            "ans": 1
        },
        {
            "q": "You need to create a custom IAM role for use with a GCP service. All permissions in the role must be suitable for production use. You also want to clearly share with your organization the status of the custom role. This will be the first version of the custom role. What should you do?",
            "o1": "Create the role with stage 'ALPHA' or 'BETA' first, then move to 'GA'.",
            "o2": "Use the description field to state the status.",
            "o3": "Email the organization.",
            "o4": "It is not possible to set status on roles.",
            "ans": 1
        },
        {
            "q": "Your company has a large quantity of unstructured data in different file formats. You want to perform ETL transformations on the data. You need to make the data accessible on Google Cloud so it can be processed by a Dataflow job. What should you do?",
            "o1": "Upload the data to Cloud Storage.",
            "o2": "Upload the data to BigQuery.",
            "o3": "Upload the data to Cloud SQL.",
            "o4": "Upload the data to Firestore.",
            "ans": 1
        },
        {
            "q": "You need to manage multiple Google Cloud projects in the fewest steps possible. You want to configure the Google Cloud SDK command line interface (CLI) so that you can easily manage multiple projects. What should you do?",
            "o1": "Create a configuration for each project using 'gcloud config configurations create'.",
            "o2": "Use 'gcloud init' every time.",
            "o3": "Use multiple terminals.",
            "o4": "Use the '--project' flag for every command.",
            "ans": 1
        },
        {
            "q": "Your Managed Instance Group raised an alert stating that new instance creation has failed to create new instances. You need to maintain the number of running instances specified by the template to be able to process expected application traffic. What should you do?",
            "o1": "Check the MIG errors in the Console, verify Quota limits, or check Image availability.",
            "o2": "Delete the MIG and recreate it.",
            "o3": "Create manual instances.",
            "o4": "Ignore the alert.",
            "ans": 1
        },
        {
            "q": "Your company is moving from an on-premises environment to Google Cloud. You have multiple development teams that use Cassandra environments as backend databases. They all need a development environment that is isolated from other Cassandra instances. You want to move to Google Cloud quickly and with minimal support effort. What should you do?",
            "o1": "Use Google Cloud Marketplace to launch Cassandra clusters for each team.",
            "o2": "Install Cassandra manually on VMs.",
            "o3": "Use Cloud Bigtable.",
            "o4": "Use Cloud Spanner.",
            "ans": 1
        },
        {
            "q": "You have a Compute Engine instance hosting a production application. You want to receive an email if the instance consumes more than 90% of its CPU resources for more than 15 minutes. You want to use Google services. What should you do?",
            "o1": "Create an Alerting Policy in Cloud Monitoring.",
            "o2": "Write a script on the VM to send emails.",
            "o3": "Use a third-party monitoring tool.",
            "o4": "Check the dashboard manually.",
            "ans": 1
        },
        {
            "q": "You have an application that uses Cloud Spanner as a backend database. The application has a very predictable traffic pattern. You want to automatically scale up or down the number of Spanner nodes depending on traffic. What should you do?",
            "o1": "Use a Cloud Autoscaler (Community tool) or Cloud Functions triggered by Monitoring metrics to adjust node count.",
            "o2": "Enable Autoscaling on Spanner settings (not native).",
            "o3": "Use a Managed Instance Group.",
            "o4": "Spanner autoscales nodes automatically by default (False).",
            "ans": 1
        },
        {
            "q": "Your company publishes large files on an Apache web server that runs on a Compute Engine instance. The Apache web server is not the only application running in the project. You want to receive an email when the egress network costs for the server exceed 100 dollars for the current month as measured by Google Cloud. What should you do?",
            "o1": "Export Billing usage to BigQuery and use Data Studio/Cloud Functions to alert.",
            "o2": "Set a specific budget for the project.",
            "o3": "You cannot trigger alerts on specific instances' egress cost directly in Budgets.",
            "o4": "Use Cloud Monitoring metric 'network/sent_bytes_count' and multiply by cost.",
            "ans": 1
        },
        {
            "q": "You have designed a solution on Google Cloud that uses multiple Google Cloud products. Your company has asked you to estimate the costs of the solution. You need to provide estimates for the monthly total cost. What should you do?",
            "o1": "Use the Google Cloud Pricing Calculator.",
            "o2": "Check the SKU list.",
            "o3": "Create the resources and check the bill.",
            "o4": "Ask Sales.",
            "ans": 1
        },
        {
            "q": "You have an application that receives SSL-encrypted TCP traffic on port 443. Clients for this application are located all over the world. You want to minimize latency for the clients. Which load balancing option should you use?",
            "o1": "External SSL Proxy Load Balancing.",
            "o2": "External TCP Proxy Load Balancing.",
            "o3": "External HTTP(S) Load Balancing.",
            "o4": "Network Load Balancing.",
            "ans": 1
        },
        {
            "q": "You have an application on a general-purpose Compute Engine instance that is experiencing excessive disk read throttling on its Zonal SSD Persistent Disk. The application primarily reads large files from disk. The disk size is currently 350 GB. You want to provide the maximum amount of throughput while minimizing costs. What should you do?",
            "o1": "Increase the disk size to increase IOPS/Throughput.",
            "o2": "Switch to Local SSD.",
            "o3": "Add more vCPUs.",
            "o4": "Use a Regional PD.",
            "ans": 1
        },
        {
            "q": "Your Dataproc cluster runs in a single Virtual Private Cloud (VPC) network in a single subnet with range 172.16.20.128/25. There are no private IP addresses available in the VPC network. You want to add new VMs to communicate with your cluster using the minimum number of steps. What should you do?",
            "o1": "Expand the subnet range if possible, or create a new subnet in a new secondary ip range.",
            "o2": "Create a new VPC and peer it.",
            "o3": "Delete existing VMs.",
            "o4": "Use Public IPs.",
            "ans": 1
        },
        {
            "q": "You manage an App Engine Service that aggregates and visualizes data from BigQuery. The application is deployed with the default App Engine Service account. The data that needs to be visualized resides in a different project managed by another team. You do not have access to this project, but you want your application to be able to read data from the BigQuery dataset. What should you do?",
            "o1": "Ask the other team to grant 'BigQuery Data Viewer' to your App Engine Service Account.",
            "o2": "Ask for the owner role.",
            "o3": "Create a Service Account in their project and download the key.",
            "o4": "Make the dataset public.",
            "ans": 1
        },
        {
            "q": "You need to create a copy of a custom Compute Engine Virtual Machine (VM) to facilitate an expected increase in application traffic due to a business acquisition. What should you do?",
            "o1": "Create a Machine Image from the VM and create new instances from it.",
            "o2": "Snapshot the disk and create a new VM.",
            "o3": "Copy the files manually.",
            "o4": "Use Deployment Manager.",
            "ans": 1
        },
        {
            "q": "You have deployed an application on a single Compute Engine instance. The application writes logs to disk. Users start reporting errors with the application. You want to diagnose the problem. What should you do?",
            "o1": "Install the Cloud Logging Agent to stream logs to Cloud Logging, then analyze there.",
            "o2": "SSH into the VM and check logs.",
            "o3": "Reboot the VM.",
            "o4": "Check the Serial Port Console.",
            "ans": 1
        },
        {
            "q": "An application generates daily reports in a Compute Engine Virtual Machine (VM). The VM is in the project corp-iot-insights. Your team operates only in the project corp-aggregate-reports and needs a copy of the daily exports in the bucket corp-aggregate-reports-storage. You want to configure access so that the daily reports from the VM are available in the bucket corp-aggregate-reports-storage and use as few steps as possible while following Google-recommended practices. What should you do?",
            "o1": "Grant the VM's Service Account 'Storage Object Creator' on the destination bucket in corp-aggregate-reports.",
            "o2": "Make the bucket public.",
            "o3": "Copy files via the console.",
            "o4": "Use a VPN.",
            "ans": 1
        },
        {
            "q": "You built an application on your development laptop that uses Google Cloud services. Your application uses Application Default Credentials for authentication and works fine on your development laptop. You want to migrate this application to a Compute Engine Virtual Machine (VM) and set up authentication using Google-recommended practices and minimal changes. What should you do?",
            "o1": "Run the application; it will use the VM's attached Service Account automatically.",
            "o2": "Copy your JSON key to the VM.",
            "o3": "Run 'gcloud auth login' on the VM.",
            "o4": "Hardcode credentials.",
            "ans": 1
        },
        {
            "q": "You need to create a Compute Engine instance in a new project that doesn't exist yet. What should you do?",
            "o1": "Create the project first, enable billing, enable Compute Engine API, then create the instance.",
            "o2": "Run 'gcloud compute instances create --project=new-project'.",
            "o3": "It creates automatically.",
            "o4": "Use Cloud Shell.",
            "ans": 1
        },
        {
            "q": "Your company runs one batch process in an on-premises server that takes around 30 hours to complete. The task runs monthly, can be performed offline, and must be restarted if interrupted. You want to migrate this workload to the cloud while minimizing cost. What should you do?",
            "o1": "Use Preemptible VMs (since it can restart).",
            "o2": "Use a Standard VM.",
            "o3": "Use App Engine.",
            "o4": "Use Cloud Functions.",
            "ans": 1
        },
        {
            "q": "You are developing a new application and are looking for a Jenkins installation to build and deploy your source code. You want to automate the installation as quickly and easily as possible. What should you do?",
            "o1": "Use Google Cloud Marketplace.",
            "o2": "Install on a VM manually.",
            "o3": "Use GKE.",
            "o4": "Use Cloud Build (it replaces Jenkins).",
            "ans": 1
        },
        {
            "q": "You have downloaded and installed the gcloud command line interface (CLI) and have authenticated with your Google Account. Most of your Compute Engine instances in your project run in the europe-west1-d zone. You want to avoid having to specify this zone with each CLI command when managing these instances. What should you do?",
            "o1": "Run 'gcloud config set compute/zone europe-west1-d'.",
            "o2": "Use an alias in your shell.",
            "o3": "Modify the .bashrc file.",
            "o4": "It is not possible.",
            "ans": 1
        },
        {
            "q": "The core business of your company is to rent out construction equipment at large scale. All the equipment that is being rented out has been equipped with multiple sensors that send event information every few seconds. These signals can vary from engine status, distance traveled, fuel level, and more. Customers are billed based on the consumption monitored by these sensors. You expect high throughput - up to thousands of events per hour per device - and need to retrieve consistent data based on the time of the event. Storing and retrieving individual signals should be atomic. What should you do?",
            "o1": "Use Cloud Bigtable.",
            "o2": "Use Cloud Pub/Sub.",
            "o3": "Use Firestore.",
            "o4": "Use Cloud Spanner.",
            "ans": 1
        },
        {
            "q": "You are asked to set up application performance monitoring on Google Cloud projects A, B, and C as a single pane of glass. You want to monitor CPU, memory, and disk. What should you do?",
            "o1": "Create a Metrics Scope (Workspace) in Project A and add B and C to it.",
            "o2": "Open 3 tabs.",
            "o3": "Use Data Studio.",
            "o4": "Export metrics to BigQuery.",
            "ans": 1
        },
        {
            "q": "You created several resources in multiple Google Cloud projects. All projects are linked to different billing accounts. To better estimate future charges, you want to have a single visual representation of all costs incurred. You want to include new cost data as soon as possible. What should you do?",
            "o1": "Export billing data from all billing accounts to the *same* BigQuery dataset, then visualize with Data Studio.",
            "o2": "Check the reports manually.",
            "o3": "Merge the billing accounts.",
            "o4": "Use a 3rd party tool.",
            "ans": 1
        },
        {
            "q": "Your company has workloads running on Compute Engine and on-premises. The Google Cloud Virtual Private Cloud (VPC) is connected to your WAN over a Virtual Private Network (VPN). You need to deploy a new Compute Engine instance and ensure that no public Internet traffic can be routed to it. What should you do?",
            "o1": "Create the instance without an External IP address.",
            "o2": "Configure the firewall to deny port 80.",
            "o3": "Use a Private Service Connect.",
            "o4": "Enable Private Google Access.",
            "ans": 1
        },
        {
            "q": "Your team maintains the infrastructure for your organization. The current infrastructure requires changes. You need to share your proposed changes with the rest of the team. You want to follow Google's recommended best practices. What should you do?",
            "o1": "Use Terraform (Infrastructure as Code) and store the state/code in Git.",
            "o2": "Share screenshots of the console.",
            "o3": "Write a document describing the changes.",
            "o4": "Use Deployment Manager blueprints.",
            "ans": 1
        },
        {
            "q": "You have a Compute Engine instance hosting an application used between 9 AM and 6 PM on weekdays. You want to back up this instance daily for disaster recovery purposes. You want to keep the backups for 30 days. You want the Google-recommended solution with the least management overhead and the least number of services. What should you do?",
            "o1": "Configuring a Scheduled Snapshot policy.",
            "o2": "Use a cron job.",
            "o3": "Use Cloud Functions.",
            "o4": "Manually snapshot every day.",
            "ans": 1
        },
        {
            "q": "Your existing application running in Google Kubernetes Engine (GKE) consists of multiple pods running on four GKE n1-standard-2 nodes. You need to deploy additional pods requiring n2-highmem-16 nodes without any downtime. What should you do?",
            "o1": "Create a new Node Pool with n2-highmem-16 nodes and deploy the pods there (using nodeSelector or affinity).",
            "o2": "Resize the existing node pool.",
            "o3": "Create a new cluster.",
            "o4": "Upgrade the master.",
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
    
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 5).")

if __name__ == "__main__":
    populate_quiz_part5()
