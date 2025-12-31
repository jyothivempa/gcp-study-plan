import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz_part3():
    try:
        day = Day.objects.get(number=33)
    except Day.DoesNotExist:
        print("Day 33 not found.")
        return

    questions = [
        {
            "q": "You are running an application on multiple Virtual Machines within a Managed Instance Group and have autoscaling enabled. The autoscaling policy is configured so that additional instances are added to the group if the CPU utilization of instances goes above 80%. VMs are added until the instance group reaches its maximum limit of five VMs or until CPU utilization of instances lowers to 80%. The initial delay for HTTP health checks against the instances is set to 30 seconds. The Virtual Machine instances take around three minutes to become available for users. You observe that when the instance group autoscales, it adds more instances then necessary to support the levels of end-user traffic. You want to properly maintain instance group sizes when autoscaling. What should you do?",
            "o1": "Increase the 'initialDelaySec' to match the startup time (e.g., 200 seconds).",
            "o2": "Decrease the CPU utilization threshold to 60%.",
            "o3": "Increase the maximum number of instances.",
            "o4": "Use a startup script to signal readiness.",
            "ans": 1
        },
        {
            "q": "You have 32 GB of data in a single file that you need to upload to a Nearline Storage bucket. The WAN connection you are using is rated at 1 Gbps, and you are the only one on the connection. You want to use as much of the rated 1 Gbps as possible to transfer the file rapidly. How should you upload the file?",
            "o1": "Use 'gsutil cp' with parallel composite uploads enabled.",
            "o2": "Use 'gsutil cp -m' (multi-threading).",
            "o3": "Split the file manually effectively.",
            "o4": "Use the Transfer Appliance.",
            "ans": 1
        },
        {
            "q": "You deployed an App Engine application using gcloud app deploy, but it did not deploy to the intended project. You want to find out why this happened and where the application deployed. What should you do?",
            "o1": "Check the output of 'gcloud config list' to see the active project configuration.",
            "o2": "Check the App Engine dashboard in all your projects.",
            "o3": "Deploy again with the --trace flag.",
            "o4": "Check Cloud Logging.",
            "ans": 1
        },
        {
            "q": "You want to verify the IAM users and roles assigned within a GCP project named my-project. What should you do?",
            "o1": "Run 'gcloud projects get-iam-policy my-project'.",
            "o2": "Run 'gcloud iam service-accounts list'.",
            "o3": "Run 'gcloud auth list'.",
            "o4": "Check the Activity log.",
            "ans": 1
        },
        {
            "q": "You need to select and configure compute resources for a set of batch processing jobs. These jobs take around 2 hours to complete and are run nightly. You want to minimize service costs. What should you do?",
            "o1": "Use Preemptible VMs (or Spot VMs).",
            "o2": "Use Shielded VMs.",
            "o3": "Use Sole-tenant nodes.",
            "o4": "Use Compute Engine with Committed Use Discounts.",
            "ans": 1
        },
        {
            "q": "You want to select and configure a cost-effective solution for relational data on Google Cloud Platform. You are working with a small set of operational data in one geographic location. You need to support point-in-time recovery. What should you do?",
            "o1": "Cloud SQL (MySQL or PostgreSQL).",
            "o2": "Cloud Spanner.",
            "o3": "BigQuery.",
            "o4": "Cloud Bigtable.",
            "ans": 1
        },
        {
            "q": "You are hosting an application on bare-metal servers in your own data center. The application needs access to Cloud Storage. However, security policies prevent the servers hosting the application from having public IP addresses or access to the internet. You want to follow Google-recommended practices to provide the application with access to Cloud Storage. What should you do?",
            "o1": "Use Private Google Access for On-Premises (via Cloud VPN/Interconnect).",
            "o2": "Use a NAT Gateway.",
            "o3": "Allow specific public IPs in the firewall.",
            "o4": "Use a Proxy Server.",
            "ans": 1
        },
        {
            "q": "Your company has a Google Cloud Platform project that uses BigQuery for data warehousing. Your data science team changes frequently and has few members. You need to allow members of this team to perform queries. You want to follow Google-recommended practices. What should you do?",
            "o1": "Create a Google Group for the team and grant the 'BigQuery Job User' role to the group.",
            "o2": "Grant the 'BigQuery Job User' role to each user individually.",
            "o3": "Grant the 'Project Editor' role to the group.",
            "o4": "Use a Service Account.",
            "ans": 1
        },
        {
            "q": "You are given a project with a single Virtual Private Cloud (VPC) and a single subnetwork in the us-central1 region. There is a Compute Engine instance hosting an application in this subnetwork. You need to deploy a new instance in the same project in the europe-west1 region. This new instance needs access to the application. You want to follow Google-recommended practices. What should you do?",
            "o1": "Add a new subnet in europe-west1 to the existing VPC. The internal network is global.",
            "o2": "Create a new VPC in Europe and peer them.",
            "o3": "Use Cloud VPN.",
            "o4": "Use External IPs.",
            "ans": 1
        },
        {
            "q": "You are building a pipeline to process time-series data. Which Google Cloud Platform services should you put in boxes 1,2,3, and 4?",
            "o1": "Pub/Sub -> Dataflow -> Bigtable -> BigQuery",
            "o2": "Pub/Sub -> Dataproc -> Cloud Storage -> BigQuery",
            "o3": "Cloud Storage -> Dataflow -> Bigtable -> BigQuery",
            "o4": "Pub/Sub -> Cloud Functions -> Firestore -> BigQuery",
            "ans": 1
        },
        {
            "q": "For analysis purposes, you need to send all the logs from all of your Compute Engine instances to a BigQuery dataset called platform-logs. You have already installed the Cloud Logging agent on all the instances. You want to minimize cost. What should you do?",
            "o1": "Create a Sink in Cloud Logging to export logs to BigQuery.",
            "o2": "Write a script on each VM to stream logs to BigQuery.",
            "o3": "Use Dataflow to read logs and write to BigQuery.",
            "o4": "Use Cloud Pub/Sub as an intermediary.",
            "ans": 1
        },
        {
            "q": "You want to deploy an application on Cloud Run that processes messages from a Cloud Pub/Sub topic. You want to follow Google-recommended practices. What should you do?",
            "o1": "Create a Pub/Sub triggers (Push subscription) to the Cloud Run endpoint.",
            "o2": "Have the Cloud Run service pull messages from Pub/Sub.",
            "o3": "Use Cloud Functions as a wrapper.",
            "o4": "Use App Engine.",
            "ans": 1
        },
        {
            "q": "Your projects incurred more costs than you expected last month. Your research reveals that a development GKE container emitted a huge number of logs, which resulted in higher costs. You want to disable the logs quickly using the minimum number of steps. What should you do?",
            "o1": "Add an exclusion filter in Cloud Logging for the GKE cluster logs.",
            "o2": "Delete the GKE cluster.",
            "o3": "Update the container code to stop logging.",
            "o4": "Disable the Cloud Logging API.",
            "ans": 1
        },
        {
            "q": "You've deployed a microservice called myapp1 to a Google Kubernetes Engine cluster using the YAML file specified below. You need to refactor this configuration so that the database password is not stored in plain text. You want to follow Google-recommended practices. What should you do?",
            "o1": "Use a Kubernetes Secret and reference it in the YAML.",
            "o2": "Use a ConfigMap.",
            "o3": "Use Metadata server.",
            "o4": "Encrypt the file with KMS.",
            "ans": 1
        },
        {
            "q": "You have an application running in Google Kubernetes Engine (GKE) with cluster autoscaling enabled. The application exposes a TCP endpoint. There are several replicas of this application. You have a Compute Engine instance in the same region, but in another Virtual Private Cloud (VPC), called gce-network, that has no overlapping IP ranges with the first VPC. This instance needs to connect to the application on GKE. You want to minimize effort. What should you do?",
            "o1": "Use VPC Network Peering between the two VPCs.",
            "o2": "Use Cloud VPN.",
            "o3": "Expose the GKE service via an External Load Balancer.",
            "o4": "Use Cloud Interconnect.",
            "ans": 1
        },
        {
            "q": "You are using Container Registry to centrally store your company's container images in a separate project. In another project, you want to create a Google Kubernetes Engine (GKE) cluster. You want to ensure that Kubernetes can download images from Container Registry. What should you do?",
            "o1": "Grant the GKE Service Account the 'Storage Object Viewer' role on the GCR bucket in the other project.",
            "o2": "Make the GCR bucket public.",
            "o3": "Copy the images to the local project.",
            "o4": "Use a pull secret.",
            "ans": 1
        },
        {
            "q": "You deployed a new application inside your Google Kubernetes Engine cluster using the YAML file specified below. You check the status of the deployed pods and notice that one of them is still in PENDING status. You want to find out why the pod is stuck in pending status. What should you do?",
            "o1": "Run 'kubectl describe pod <pod-name>'.",
            "o2": "Run 'kubectl logs <pod-name>'.",
            "o3": "Run 'kubectl get pods'.",
            "o4": "Check Cloud Logging.",
            "ans": 1
        },
        {
            "q": "You are setting up a Windows VM on Compute Engine and want to make sure you can log in to the VM via RDP. What should you do?",
            "o1": "Set a Windows Password (which creates a local user) in the Console, then use RDP.",
            "o2": "Use SSH keys.",
            "o3": "Enable OS Login.",
            "o4": "Add a metadata tag 'enable-rdp'.",
            "ans": 1
        },
        {
            "q": "You want to configure an SSH connection to a single Compute Engine instance for users in the dev1 group. This instance is the only resource in this particular Google Cloud Platform project that the dev1 users should be able to connect to. What should you do?",
            "o1": "Add the users' SSH keys to the instance metadata.",
            "o2": "Add the users' SSH keys to the project metadata.",
            "o3": "Grant the 'Compute Instance Admin' role to dev1.",
            "o4": "Grant 'OS Login' to dev1.",
            "ans": 1
        },
        {
            "q": "You need to produce a list of the enabled Google Cloud Platform APIs for a GCP project using the gcloud command line in the Cloud Shell. The project name is my-project. What should you do?",
            "o1": "Run 'gcloud services list --enabled --project=my-project'.",
            "o2": "Run 'gcloud projects describe my-project'.",
            "o3": "Run 'gcloud apis list'.",
            "o4": "Run 'gcloud config list'.",
            "ans": 1
        },
        {
            "q": "You are building a new version of an application hosted in an App Engine environment. You want to test the new version with 1% of users before you completely switch your application over to the new version. What should you do?",
            "o1": "Deploy the new version and use Traffic Splitting to route 1%.",
            "o2": "Use Cloud Load Balancing.",
            "o3": "Use a randomized script in your app code.",
            "o4": "Deploy to a separate project.",
            "ans": 1
        },
        {
            "q": "You need to provide a cost estimate for a Kubernetes cluster using the GCP pricing calculator for Kubernetes. Your workload requires high IOPs, and you will also be using disk snapshots. You start by entering the number of nodes, average hours, and average days. What should you do next?",
            "o1": "Select 'Local SSD' for high IOPS and add 'Persistent Disk' for snapshots storage estimate.",
            "o2": "Select 'Standard Persistent Disk'.",
            "o3": "Select 'Preemptible Nodes'.",
            "o4": "Add a Load Balancer.",
            "ans": 1
        },
        {
            "q": "You are using Google Kubernetes Engine with autoscaling enabled to host a new application. You want to expose this new application to the public, using HTTPS on a public IP address. What should you do?",
            "o1": "Create a Kubernetes Ingress object (which provisions an HTTP(S) Load Balancer).",
            "o2": "Create a Service of type LoadBalancer.",
            "o3": "Use a NodePort.",
            "o4": "Use Cloud DNS.",
            "ans": 1
        },
        {
            "q": "You need to enable traffic between multiple groups of Compute Engine instances that are currently running two different GCP projects. Each group of Compute Engine instances is running in its own VPC. What should you do?",
            "o1": "Use VPC Network Peering.",
            "o2": "Use Cloud VPN.",
            "o3": "Use Shared VPC.",
            "o4": "Use Public IPs.",
            "ans": 1
        },
        {
            "q": "You want to add a new auditor to a Google Cloud Platform project. The auditor should be allowed to read, but not modify, all project items. How should you configure the auditor's permissions?",
            "o1": "Grant the 'Viewer' role (basic role).",
            "o2": "Grant the 'Browser' role.",
            "o3": "Grant the 'Auditor' custom role.",
            "o4": "Grant 'Read-Only' access.",
            "ans": 1
        },
        {
            "q": "You are operating a Google Kubernetes Engine (GKE) cluster for your company where different teams can run non-production workloads. Your Machine Learning (ML) team needs access to Nvidia Tesla P100 GPUs to train their models. You want to minimize effort and cost. What should you do?",
            "o1": "Create a new Node Pool with GPU-enabled nodes.",
            "o2": "Create a new Cluster with GPUs.",
            "o3": "Add GPUs to existing running nodes.",
            "o4": "Run the ML workload on Compute Engine instead.",
            "ans": 1
        },
        {
            "q": "Your VMs are running in a subnet that has a subnet mask of 255.255.255.240. The current subnet has no more free IP addresses and you require an additional 10 IP addresses for new VMs. The existing and new VMs should all be able to reach each other without additional routes. What should you do?",
            "o1": "Expand the CIDR range of the subnet (if possible) or create a new secondary range.",
            "o2": "Create a new subnet in the same region.",
            "o3": "Create a new VPC.",
            "o4": "Use Static IPs.",
            "ans": 1
        },
        {
            "q": "Your organization uses G Suite for communication and collaboration. All users in your organization have a G Suite account. You want to grant some G Suite users access to your Cloud Platform project. What should you do?",
            "o1": "Add the users directly to IAM using their G Suite email addresses.",
            "o2": "Sync G Suite to Cloud Identity.",
            "o3": "Export users to CSV and import.",
            "o4": "Create Gmail accounts for them.",
            "ans": 1
        },
        {
            "q": "You have a Google Cloud Platform account with access to both production and development projects. You need to create an automated process to list all compute instances in development and production projects on a daily basis. What should you do?",
            "o1": "Use Cloud Scheduler to trigger a Cloud Function that runs 'gcloud compute instances list' (via API) for both projects.",
            "o2": "Run a cron job on your laptop.",
            "o3": "Use Stackdriver.",
            "o4": "Use Deployment Manager.",
            "ans": 1
        },
        {
            "q": "You have a large 5-TB AVRO file stored in a Cloud Storage bucket. Your analysts are proficient only in SQL and need access to the data stored in this file. You want to find a cost-effective way to complete their request as soon as possible. What should you do?",
            "o1": "Create a BigQuery External Table pointing to the Cloud Storage file.",
            "o2": "Load the data into BigQuery Native Storage.",
            "o3": "Use Cloud Dataproc.",
            "o4": "Use Cloud Dataflow.",
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
    
    # Manually printing progress
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 3).")

if __name__ == "__main__":
    populate_quiz_part3()
