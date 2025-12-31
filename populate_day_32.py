import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz_part2():
    try:
        day = Day.objects.get(number=32)
    except Day.DoesNotExist:
        print("Day 32 not found.")
        return

    # Do NOT clear questions here, we are appending!

    questions = [
        {
            "q": "You create a new Google Kubernetes Engine (GKE) cluster and want to make sure that it always runs a supported and stable version of Kubernetes. What should you do?",
            "o1": "Enable Node Auto-Upgrades.",
            "o2": "Enable Node Auto-Repair.",
            "o3": "Select the latest version manually every week.",
            "o4": "Use a Static version.",
            "ans": 1
        },
        {
            "q": "Your company uses Cloud Storage to store application backup files for disaster recovery purposes. You want to follow Google's recommended practices. Which storage option should you use?",
            "o1": "Nearline or Coldline Storage, depending on access frequency.",
            "o2": "Multi-Regional Standard Storage.",
            "o3": "Regional Standard Storage.",
            "o4": "Local SSD.",
            "ans": 1
        },
        {
            "q": "You need to set up a policy so that videos stored in a specific Cloud Storage Regional bucket are moved to Coldline after 90 days, and then deleted after one year from their creation. How should you set up the policy?",
            "o1": "Use Object Lifecycle Management.",
            "o2": "Use a Cloud Function to check dates.",
            "o3": "Use a Cron job on a VM.",
            "o4": "Manually move files.",
            "ans": 1
        },
        {
            "q": "Your company has an existing GCP organization with hundreds of projects and a billing account. Your company recently acquired another company that also has hundreds of projects and its own billing account. You would like to consolidate all GCP costs of both GCP organizations onto a single invoice. You would like to consolidate all costs as of tomorrow. What should you do?",
            "o1": "Link the projects of the acquired company to your existing Billing Account.",
            "o2": "Migrate the projects to your Organization.",
            "o3": "Merge the two Billing Accounts.",
            "o4": "Create a new Organization.",
            "ans": 1
        },
        {
            "q": "You want to configure 10 Compute Engine instances for availability when maintenance occurs. Your requirements state that these instances should attempt to automatically restart if they crash. Also, the instances should be highly available including during system maintenance. What should you do?",
            "o1": "Set 'Automatic Restart' to On and 'On Host Maintenance' to 'Migrate'.",
            "o2": "Set 'Automatic Restart' to Off and 'On Host Maintenance' to 'Terminate'.",
            "o3": "Use Preemptible instances.",
            "o4": "Use a Managed Instance Group with auto-healing only.",
            "ans": 1
        },
        {
            "q": "You have a development project with appropriate IAM roles defined. You are creating a production project and want to have the same IAM roles on the new project, using the fewest possible steps. What should you do?",
            "o1": "Use 'gcloud iam roles copy' to copy custom roles, or re-apply standard roles via script.",
            "o2": "Manually add each user in the console.",
            "o3": "Copy the project.",
            "o4": "Use the IAM Policy Analyzer.",
            "ans": 1
        },
        {
            "q": "You are using multiple configurations for gcloud. You want to review the configured Kubernetes Engine cluster of an inactive configuration using the fewest possible steps. What should you do?",
            "o1": "Use 'kubectl config get-contexts' or inspect the kubeconfig file.",
            "o2": "Activate the configuration first, then check.",
            "o3": "Use 'gcloud config list'.",
            "o4": "Delete the configuration.",
            "ans": 1
        },
        {
            "q": "You need to configure IAM access audit logging in BigQuery for external auditors. You want to follow Google-recommended practices. What should you do?",
            "o1": "Verify Data Access logs are enabled for BigQuery (they are on by default for BigQuery) and grant the auditor Viewer access to the logs.",
            "o2": "Create a custom log sink to Pub/Sub.",
            "o3": "Export logs to Cloud Storage.",
            "o4": "Use Cloud Monitoring.",
            "ans": 1
        },
        {
            "q": "You need to create a custom VPC with a single subnet. The subnet's range must be as large as possible. Which range should you use?",
            "o1": "10.0.0.0/8",
            "o2": "172.16.0.0/12",
            "o3": "192.168.0.0/16",
            "o4": "10.0.0.0/24",
            "ans": 1
        },
        {
            "q": "You recently deployed a new version of an application to App Engine and then discovered a bug in the release. You need to immediately revert to the prior version of the application. What should you do?",
            "o1": "In the App Engine versions page, route 100% traffic to the previous version.",
            "o2": "Delete the new version.",
            "o3": "Redeploy the old code.",
            "o4": "Restore from backup.",
            "ans": 1
        },
        {
            "q": "You want to configure Autohealing for network load balancing for a group of Compute Engine instances that run in multiple zones, using the fewest possible steps. You need to configure re-creation of VMs if they are unresponsive after 3 attempts of 10 seconds each. What should you do?",
            "o1": "Configure a Health Check on the Managed Instance Group.",
            "o2": "Configure a Health Check on the Load Balancer.",
            "o3": "Use a startup script.",
            "o4": "Use Cloud Functions to monitor.",
            "ans": 1
        },
        {
            "q": "You have a Linux VM that must connect to Cloud SQL. You created a service account with the appropriate access rights. You want to make sure that the VM uses this service account instead of the default Compute Engine service account. What should you do?",
            "o1": "Stop the VM, edit the instance settings to assign the new Service Account, and start it.",
            "o2": "SSH into the VM and run 'gcloud auth activate-service-account'.",
            "o3": "It is not possible to change the service account of a VM.",
            "o4": "Delete the VM and recreate it.",
            "ans": 1
        },
        {
            "q": "You have one project called proj-sa where you manage all your service accounts. You want to be able to use a service account from this project to take snapshots of VMs running in another project called proj-vm. What should you do?",
            "o1": "Grant the Service Account from proj-sa the 'Compute Instance Admin' or 'Snapshot Admin' role in proj-vm.",
            "o2": "Create a new Service Account in proj-vm.",
            "o3": "Peering the VPCs.",
            "o4": "Use Shared VPC.",
            "ans": 1
        },
        {
            "q": "You have one GCP account running in your default region and zone and another account running in a non-default region and zone. You want to start a new Compute Engine instance in these two Google Cloud Platform accounts using the command line interface. What should you do?",
            "o1": "Use 'gcloud config configurations create' to manage multiple profiles.",
            "o2": "Use 'gcloud auth login' every time you switch.",
            "o3": "Run commands in two different terminals.",
            "o4": "Use the Google Cloud Console.",
            "ans": 1
        },
        {
            "q": "Every employee of your company has a Google account. Your operational team needs to manage a large number of instances on Compute Engine. Each member of this team needs only administrative access to the servers. Your security team wants to ensure that the deployment of credentials is operationally efficient and must be able to determine who accessed a given instance. What should you do?",
            "o1": "Use OS Login.",
            "o2": "Manage SSH keys manually in metadata.",
            "o3": "Use a shared SSH key.",
            "o4": "Use a bastion host.",
            "ans": 1
        },
        {
            "q": "You need to deploy an application, which is packaged in a container image, in a new project. The application exposes an HTTP endpoint and receives very few requests per day. You want to minimize costs. What should you do?",
            "o1": "Cloud Run (fully managed).",
            "o2": "GKE Standard.",
            "o3": "Compute Engine.",
            "o4": "App Engine Flexible.",
            "ans": 1
        },
        {
            "q": "Your development team needs a new Jenkins server for their project. You need to deploy the server using the fewest steps possible. What should you do?",
            "o1": "Use the Google Cloud Marketplace to launch a Jenkins solution.",
            "o2": "Install Jenkins manually on a VM.",
            "o3": "Use GKE and Helm charts.",
            "o4": "Use Cloud Build.",
            "ans": 1
        },
        {
            "q": "You are building an application that stores relational data from users. Users across the globe will use this application. Your CTO is concerned about the scaling requirements because the size of the user base is unknown. You need to implement a database solution that can scale with your user growth with minimum configuration changes. Which storage solution should you use?",
            "o1": "Cloud Spanner.",
            "o2": "Cloud SQL.",
            "o3": "Bigtable.",
            "o4": "Firestore.",
            "ans": 1
        },
        {
            "q": "You are using Deployment Manager to create a Google Kubernetes Engine cluster. Using the same Deployment Manager deployment, you also want to create a DaemonSet in the kube-system namespace of the cluster. You want a solution that uses the fewest possible services.",
            "o1": "Use a Deployment Manager Type Provider for Kubernetes.",
            "o2": "Run a script after deployment.",
            "o3": "Use Terraform.",
            "o4": "Create a separate deployment.",
            "ans": 1
        },
        {
            "q": "You have a Virtual Machine that is currently configured with 2 vCPUs and 4 GB of memory. It is running out of memory. You want to upgrade the Virtual Machine to have 8 GB of memory. What should you do?",
            "o1": "Stop the instance, change the machine type to n1-standard-2 (or custom), and start it.",
            "o2": "Change the machine type while it is running.",
            "o3": "Add a Local SSD.",
            "o4": "Create a new VM and migrate data.",
            "ans": 1
        },
        {
            "q": "You created a Google Cloud Platform project with an App Engine application inside the project. You initially configured the application to be served from the us-central region. Now you want the application to be served from the asia-northeast1 region. What should you do?",
            "o1": "Create a new Project. App Engine region cannot be changed.",
            "o2": "Change the region in App Engine settings.",
            "o3": "Redeploy with the --region flag.",
            "o4": "Contact Support.",
            "ans": 1
        },
        {
            "q": "Several employees at your company have been creating projects with Cloud Platform and paying for it with their personal credit cards, which the company reimburses. The company wants to centralize all these projects under a single, new billing account. What should you do?",
            "o1": "Create a Corporate Billing Account and change the billing account of each project to the new one.",
            "o2": "Create a new Project and move resources.",
            "o3": "Add the company card to each project.",
            "o4": "Use Resource Manager.",
            "ans": 1
        },
        {
            "q": "You have a Dockerfile that you need to deploy on Kubernetes Engine. What should you do?",
            "o1": "Build the image (Cloud Build), push to Container Registry/Artifact Registry, then deploy to GKE.",
            "o2": "Deploy the Dockerfile directly to GKE.",
            "o3": "Use App Engine.",
            "o4": "Use Cloud Functions.",
            "ans": 1
        },
        {
            "q": "You have a project for your App Engine application that serves a development environment. The required testing has succeeded and you want to create a new project to serve as your production environment. What should you do?",
            "o1": "Create the new project and redeploy the app to it.",
            "o2": "Rename the existing project.",
            "o3": "Clone the project.",
            "o4": "Use Deployment Manager.",
            "ans": 1
        },
        {
            "q": "You are building an application that will run in your data center. The application will use Google Cloud Platform (GCP) services like AutoML. You created a service account that has appropriate access to AutoML. You need to enable authentication to the APIs from your on-premises environment. What should you do?",
            "o1": "Create a JSON key for the Service Account and set GOOGLE_APPLICATION_CREDENTIALS.",
            "o2": "Use gcloud auth login.",
            "o3": "Use an API Key.",
            "o4": "Use Workload Identity Federation (Modern approach) or Keys (Classic).",
            "ans": 1
        },
        {
            "q": "You host a static website on Cloud Storage. Recently, you began to include links to PDF files on this site. Currently, when users click on the links to these PDF files, their browsers prompt them to save the file onto their local system. Instead, you want the clicked PDF files to be displayed within the browser window directly, without prompting the user to save the file locally. What should you do?",
            "o1": "Set the Content-Type metadata to 'application/pdf'.",
            "o2": "Set the Content-Disposition metadata to 'inline'.",
            "o3": "Use Signed URLs.",
            "o4": "Compress the files.",
            "ans": 2
        },
        {
            "q": "You have an application that looks for its licensing server on the IP 10.0.3.21. You need to deploy the licensing server on Compute Engine. You do not want to change the configuration of the application and want the application to be able to reach the licensing server. What should you do?",
            "o1": "Create a VPC with a subnet containing 10.0.3.21 and assign that static internal IP to the VM.",
            "o2": "Use an Alias IP.",
            "o3": "Use a static public IP.",
            "o4": "Use Cloud DNS.",
            "ans": 1
        },
        {
            "q": "You are deploying an application to App Engine. You want the number of instances to scale based on request rate. You need at least 3 unoccupied instances at all times. Which scaling type should you use?",
            "o1": "Automatic Scaling with min_idle_instances set to 3.",
            "o2": "Basic Scaling.",
            "o3": "Manual Scaling with 3 instances.",
            "o4": "Automatic Scaling with max_instances set to 3.",
            "ans": 1
        },
        {
            "q": "You are the project owner of a GCP project and want to delegate control to colleagues to manage buckets and files in Cloud Storage. You want to follow Google-recommended practices. Which IAM roles should you grant your colleagues?",
            "o1": "Storage Admin.",
            "o2": "Project Editor.",
            "o3": "Storage Object Admin.",
            "o4": "Storage Object Creator.",
            "ans": 1
        },
        {
            "q": "You need to update a deployment in Deployment Manager without any resource downtime in the deployment. Which command should you use?",
            "o1": "gcloud deployment-manager deployments update --preview (to check) then update.",
            "o2": "gcloud deployment-manager deployments create.",
            "o3": "gcloud deployment-manager resources update.",
            "o4": "gcloud deployment-manager deployments delete and recreate.",
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
    
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 2).")

if __name__ == "__main__":
    populate_quiz_part2()
