import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz():
    try:
        day = Day.objects.get(number=31)
    except Day.DoesNotExist:
        print("Day 31 not found.")
        return

    # Question data
    questions = [
        {
            "q": "You significantly changed a complex Deployment Manager template and want to confirm that the dependencies of all defined resources are properly met before committing it to the project. You want the most rapid feedback on your changes. What should you do?",
            "o1": "Use gcloud deployment-manager deployments create --preview",
            "o2": "Commit the change and check the build logs",
            "o3": "Use gcloud deployment-manager resources list",
            "o4": "Run a dry-run in Terraform",
            "ans": 1
        },
        {
            "q": "Your company has a 3-tier solution running on Compute Engine. The configuration of the current infrastructure is shown below. Each tier has a service account that is associated with all instances within it. You need to enable communication on TCP port 8080 between tiers as follows: Instances in tier #1 must communicate with tier #2. Instances in tier #2 must communicate with tier #3. What should you do?",
            "o1": "Create firewall rules based on the Service Accounts of each tier.",
            "o2": "Create firewall rules allowing 0.0.0.0/0 on port 8080.",
            "o3": "Use network tags 'tier-1', 'tier-2', 'tier-3' and allow traffic.",
            "o4": "Use Shared VPC.",
            "ans": 1
        },
        {
            "q": "You are analyzing Google Cloud Platform service costs from three separate projects. You want to use this information to create service cost estimates by service type, daily and monthly, for the next six months using standard query syntax. What should you do?",
            "o1": "Export Billing Data to BigQuery and use SQL.",
            "o2": "Use the Pricing Calculator.",
            "o3": "Download the CSV report from the Billing Console.",
            "o4": "Use Cloud Monitoring metrics.",
            "ans": 1
        },
        {
            "q": "You want to send and consume Cloud Pub/Sub messages from your App Engine application. The Cloud Pub/Sub API is currently disabled. You will use a service account to authenticate your application to the API. You want to make sure your application can use Cloud Pub/Sub. What should you do?",
            "o1": "Enable the Cloud Pub/Sub API in the API Library.",
            "o2": "Grant the App Engine Service Account the Pub/Sub Admin role.",
            "o3": "Create a new Service Account.",
            "o4": "Use API Keys.",
            "ans": 1
        },
        {
            "q": "You have a website hosted on App Engine standard environment. You want 1% of your users to see a new test version of the website. You want to minimize complexity.",
            "o1": "Deploy the new version and use Traffic Splitting to route 1%.",
            "o2": "Use Google Analytics to filter users.",
            "o3": "Create a separate project for the 1% users.",
            "o4": "Use Cloud Load Balancing URL maps.",
            "ans": 1
        },
        {
            "q": "Your organization is a financial company that needs to store audit log files for 3 years. Your organization has hundreds of Google Cloud projects. You need to implement a cost-effective approach for log file retention.",
            "o1": "Create a Sink to export logs to a Coldline/Archive Storage Bucket.",
            "o2": "Store logs in BigQuery.",
            "o3": "Keep logs in Cloud Logging (Stackdriver) with 3-year retention.",
            "o4": "Download logs to an on-premise server.",
            "ans": 1
        },
        {
            "q": "You built an application on Google Cloud that uses Cloud Spanner. Your support team needs to monitor the environment but should not have access to table data. You need a streamlined solution to grant the correct permissions to your support team, and you want to follow Google-recommended practices. What should you do?",
            "o1": "Grant the 'Cloud Spanner Viewer' role.",
            "o2": "Grant the 'Cloud Spanner Database Reader' role.",
            "o3": "Grant the 'Monitoring Viewer' role.",
            "o4": "Create a custom role with 'spanner.databases.list'.",
            "ans": 3
        },
        {
            "q": "You want to run a single caching HTTP reverse proxy on GCP for a latency-sensitive website. This specific reverse proxy consumes almost no CPU. You want to have a 30-GB in-memory cache, and need an additional 2 GB of memory for the rest of the processes. You want to minimize cost. How should you run this reverse proxy?",
            "o1": "Use a custom machine type with high memory and low CPU.",
            "o2": "Use an n1-highmem-4 instance.",
            "o3": "Use Cloud Run with 32GB memory.",
            "o4": "Use App Engine Flexible.",
            "ans": 1
        },
        {
            "q": "You have a single binary application that you want to run on Google Cloud Platform. You decided to automatically scale the application based on underlying infrastructure CPU usage. Your organizational policies require you to use Virtual Machines directly. You need to ensure that the application scaling is operationally efficient and completed as quickly as possible. What should you do?",
            "o1": "Use a Managed Instance Group (MIG) with Autoscaling.",
            "o2": "Use GKE with Horizontal Pod Autoscaler.",
            "o3": "Write a script to create VMs when CPU is high.",
            "o4": "Use App Engine Standard.",
            "ans": 1
        },
        {
            "q": "You need to set up permissions for a set of Compute Engine instances to enable them to write data into a particular Cloud Storage bucket. You want to follow Google-recommended practices. What should you do?",
            "o1": "Create a Service Account with 'Storage Object Creator' role and attach it to the instances.",
            "o2": "Store credentials in a file on the instance.",
            "o3": "Make the bucket public.",
            "o4": "Use the default Compute Engine service account with Editor role.",
            "ans": 1
        },
        {
            "q": "You have an object in a Cloud Storage bucket that you want to share with an external company. The object contains sensitive data. You want access to the content to be removed after four hours. The external company does not have a Google account to which you can grant specific user-based access privileges. You want to use the most secure method that requires the fewest steps. What should you do?",
            "o1": "Create a Signed URL with a 4-hour expiration.",
            "o2": "Make the object public and delete it after 4 hours.",
            "o3": "Create a temporary Google account for them.",
            "o4": "Email the file to them.",
            "ans": 1
        },
        {
            "q": "You need to create an autoscaling Managed Instance Group for an HTTPS web application. You want to make sure that unhealthy VMs are recreated. What should you do?",
            "o1": "Configure a Health Check and attach it to the MIG.",
            "o2": "Use a script to ping the VMs.",
            "o3": "Use Cloud Monitoring alerts.",
            "o4": "Restart the group every hour.",
            "ans": 1
        },
        {
            "q": "You are deploying an application to a Compute Engine VM in a Managed Instance Group. The application must be running at all times, but only a single instance of the VM should run per GCP project. How should you configure the instance group?",
            "o1": "Set the Autoscaling size to min=1, max=1.",
            "o2": "Set the Autoscaling size to min=1, max=10.",
            "o3": "Disable Autoscaling.",
            "o4": "Use a single standalone VM instead of a MIG.",
            "ans": 1
        },
        {
            "q": "You have production and test workloads that you want to deploy on Compute Engine. Production VMs need to be in a different subnet than the test VMs. All the VMs must be able to reach each other over internal IP without creating additional routes. You need to set up VPC and the 2 subnets. Which configuration meets these requirements?",
            "o1": "Create 1 VPC with 2 Subnets in the same region.",
            "o2": "Create 2 VPCs and update routing.",
            "o3": "Create 2 VPCs and use VPC Peering.",
            "o4": "Create 1 VPC and use the same subnet for both.",
            "ans": 1
        },
        {
            "q": "You have an instance group that you want to load balance. You want the load balancer to terminate the client SSL session. The instance group is used to serve a public web application over HTTPS. You want to follow Google-recommended practices. What should you do?",
            "o1": "Use an External Global HTTP(S) Load Balancer.",
            "o2": "Use a Network Load Balancer (TCP/UDP).",
            "o3": "Use an Internal HTTP(S) Load Balancer.",
            "o4": "Use SSL Proxy Load Balancing.",
            "ans": 1
        },
        {
            "q": "You have a web application deployed as a Managed Instance Group. You have a new version of the application to gradually deploy. Your web application is currently receiving live web traffic. You want to ensure that the available capacity does not decrease during the deployment. What should you do?",
            "o1": "Perform a Rolling Update with 'maxUnavailable=0' and 'maxSurge=1'.",
            "o2": "Replace the entire instance group at once.",
            "o3": "Stop the group, update the template, and start it.",
            "o4": "Delete the old instances manually.",
            "ans": 1
        },
        {
            "q": "You need to grant access for three users so that they can view and edit table data on a Cloud Spanner instance. What should you do?",
            "o1": "Grant them the 'Cloud Spanner Database User' role.",
            "o2": "Grant them the 'Cloud Spanner Viewer' role.",
            "o3": "Grant them the 'Owner' role.",
            "o4": "Grant them the 'Cloud Spanner Admin' role.",
            "ans": 1
        },
        {
            "q": "You need to create a new billing account and then link it with an existing Google Cloud Platform project. What should you do?",
            "o1": "Create the Billing Account in the Console, then go to Billing -> Account Management to link the project.",
            "o2": "Link the project first, then create the account.",
            "o3": "You cannot link existing projects to new billing accounts.",
            "o4": "Email Google Support.",
            "ans": 1
        },
        {
            "q": "You have sensitive data stored in three Cloud Storage buckets and have enabled data access logging. You want to verify activities for a particular user for these buckets, using the fewest possible steps. You need to verify the addition of metadata labels and which files have been viewed from those buckets. What should you do?",
            "o1": "Use Cloud Logging and filter by the user's email and resource type.",
            "o2": "Check each bucket manually.",
            "o3": "Ask the user what they accessed.",
            "o4": "Use Cloud Monitoring dashboards.",
            "ans": 1
        },
        {
            "q": "You need to run an important query in BigQuery but expect it to return a lot of records. You want to find out how much it will cost to run the query. You are using on-demand pricing. What should you do?",
            "o1": "Use the '--dry-run' flag with 'bq query' or check the validator in the UI.",
            "o2": "Run the query and check the bill.",
            "o3": "Estimate based on rows count.",
            "o4": "Ask a colleague.",
            "ans": 1
        },
        {
            "q": "You need to monitor resources that are distributed over different projects in Google Cloud Platform. You want to consolidate reporting under the same Stackdriver Monitoring dashboard. What should you do?",
            "o1": "Create a Scoping Project (Workspace) and add the other projects to it.",
            "o2": "Open multiple tabs for each project.",
            "o3": "Use Data Studio.",
            "o4": "Merge the projects into one.",
            "ans": 1
        },
        {
            "q": "You need a dynamic way of provisioning VMs on Compute Engine. The exact specifications will be in a dedicated configuration file. You want to follow Google's recommended practices. Which method should you use?",
            "o1": "Deployment Manager.",
            "o2": "Shell scripts with gcloud commands.",
            "o3": "Clicking in the Console manually.",
            "o4": "Cloud Cloud Startup Scripts only.",
            "ans": 1
        },
        {
            "q": "You created an instance of SQL Server 2017 on Compute Engine to test features in the new version. You want to connect to this instance using the fewest number of steps. What should you do?",
            "o1": "Set a Windows password in the console and use RDP.",
            "o2": "Use SSH keys.",
            "o3": "Use Google Cloud Shell.",
            "o4": "Install TeamViewer.",
            "ans": 1
        },
        {
            "q": "You are the organization and billing administrator for your company. The engineering team has the Project Creator role on the organization. You do not want the engineering team to be able to link projects to the billing account. Only the finance team should be able to link a project to a billing account, but they should not be able to make any other changes to projects. What should you do?",
            "o1": "Grant 'Billing Account User' to Finance only. Revoke it from Engineering.",
            "o2": "Grant 'Project Owner' to Finance.",
            "o3": "Create a separate Organization for Finance.",
            "o4": "Disable billing for Engineering.",
            "ans": 1
        },
        {
            "q": "You are creating a Google Kubernetes Engine (GKE) cluster with a cluster autoscaler feature enabled. You need to make sure that each node of the cluster will run a monitoring pod that sends container metrics to a third-party monitoring solution. What should you do?",
            "o1": "Deploy the monitoring pod as a DaemonSet.",
            "o2": "Deploy the monitoring pod as a Deployment with replicas=1.",
            "o3": "Deploy the monitoring pod as a StatefulSet.",
            "o4": "Run it manually on each node.",
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
    
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 1).")

if __name__ == "__main__":
    populate_quiz()
