import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz_part4():
    try:
        day = Day.objects.get(number=34)
    except Day.DoesNotExist:
        print("Day 34 not found.")
        return

    questions = [
        {
            "q": "You need to verify that a Google Cloud Platform service account was created at a particular time. What should you do?",
            "o1": "Go to the Activity Tab in the IAM & Admin Console.",
            "o2": "Check the Service Account JSON key creation time.",
            "o3": "Look at the Stackdriver Monitoring metrics.",
            "o4": "Run 'gcloud iam service-accounts describe'.",
            "ans": 1
        },
        {
            "q": "You deployed an LDAP server on Compute Engine that is reachable via TLS through port 636 using UDP. You want to make sure it is reachable by clients over that port. What should you do?",
            "o1": "Create a Firewall Rule allowing UDP ingress on port 636.",
            "o2": "Create a Firewall Rule allowing TCP ingress on port 636.",
            "o3": "Add a Route to the VPC.",
            "o4": "Use Cloud Load Balancing.",
            "ans": 1
        },
        {
            "q": "You need to set a budget alert for use of Compute Engine services on one of the three Google Cloud Platform projects that you manage. All three projects are linked to a single billing account. What should you do?",
            "o1": "Create a new Budget for the specific project in the Billing Console and set alerts.",
            "o2": "Set a quota on the project.",
            "o3": "You can only set budgets on the Billing Account level, not project level.",
            "o4": "Use Cloud Functions to monitor costs.",
            "ans": 1
        },
        {
            "q": "You are migrating a production-critical on-premises application that requires 96 vCPUs to perform its task. You want to make sure the application runs in a similar environment on GCP. What should you do?",
            "o1": "Use a Compute Engine custom machine type or n1-standard-96 (if available).",
            "o2": "Use a Shielded VM.",
            "o3": "Split the workload into two n1-standard-64 VMs.",
            "o4": "Use App Engine.",
            "ans": 1
        },
        {
            "q": "You want to configure a solution for archiving data in a Cloud Storage bucket. The solution must be cost-effective. Data with multiple versions should be archived after 30 days. Previous versions are accessed once a month for reporting. This archive data is also occasionally updated at month-end. What should you do?",
            "o1": "Use Object Lifecycle Management to move non-current versions to Nearline Storage.",
            "o2": "Use Coldline Storage.",
            "o3": "Use Archive Storage.",
            "o4": "Keep it in Standard Storage.",
            "ans": 1
        },
        {
            "q": "Your company's infrastructure is on-premises, but all machines are running at maximum capacity. You want to burst to Google Cloud. The workloads on Google Cloud must be able to directly communicate to the workloads on-premises using a private IP range. What should you do?",
            "o1": "Set up Cloud VPN between on-premises and GCP VPC.",
            "o2": "Use Cloud Interconnect (Dedicated).",
            "o3": "Use Public IPs and firewall rules.",
            "o4": "Use VPC Peering.",
            "ans": 1
        },
        {
            "q": "You want to select and configure a solution for storing and archiving data on Google Cloud Platform. You need to support compliance objectives for data from one geographic location. This data is archived after 30 days and needs to be accessed annually. What should you do?",
            "o1": "Use Archive Storage (or Coldline) in a Regional Bucket.",
            "o2": "Use Standard Storage in a Multi-Regional Bucket.",
            "o3": "Use BigQuery.",
            "o4": "Use Persistent Disks.",
            "ans": 1
        },
        {
            "q": "Your company uses BigQuery for data warehousing. Over time, many different business units in your company have created 1000+ datasets across hundreds of projects. Your CIO wants you to examine all datasets to find tables that contain an employee_ssn column. You want to minimize effort in performing this task. What should you do?",
            "o1": "Use Data Catalog to search for the column name across the organization.",
            "o2": "Run a query on every dataset's INFORMATION_SCHEMA.",
            "o3": "Look at the console manually.",
            "o4": "Write a script to iterate all projects.",
            "ans": 1
        },
        {
            "q": "You create a Deployment with 2 replicas in a Google Kubernetes Engine cluster that has a single preemptible node pool. After a few minutes, you use kubectl to examine the status of your Pod and observe that one of them is still in Pending status: What is the most likely cause?",
            "o1": "The preemptible node might have been reclaimed or there are insufficient resources on the single node.",
            "o2": "The Pod image is missing.",
            "o3": "The network is down.",
            "o4": "Pending status is normal for 10 minutes.",
            "ans": 1
        },
        {
            "q": "You want to find out when users were added to Cloud Spanner Identity Access Management (IAM) roles on your Google Cloud Platform (GCP) project. What should you do in the GCP Console?",
            "o1": "Go to the Activity tab (Admin Activity Logs) in IAM.",
            "o2": "Check the Spanner instance monitoring.",
            "o3": "Check Stackdriver Trace.",
            "o4": "Check Billing reports.",
            "ans": 1
        },
        {
            "q": "Your company implemented BigQuery as an enterprise data warehouse. Users from multiple business units run queries on this data warehouse. However, you notice that query costs for BigQuery are very high, and you need to control costs. Which two methods should you use? (Choose two.)",
            "o1": "Set a dry-run limit.",
            "o2": "Set a Custom Quota on daily usage per user/project.",
            "o3": "Change to Flat-Rate pricing (if usage justifies it).",
            "o4": "Delete old data.",
            "ans": 2
        },
        {
            "q": "You are building a product on top of Google Kubernetes Engine (GKE). You have a single GKE cluster. For each of your customers, a Pod is running in that cluster, and your customers can run arbitrary code inside their Pod. You want to maximize the isolation between your customers' Pods. What should you do?",
            "o1": "Use GKE Sandbox (gVisor).",
            "o2": "Use Kubernetes Namespaces.",
            "o3": "Use Network Policies.",
            "o4": "Run each pod on a separate node.",
            "ans": 1
        },
        {
            "q": "Your customer has implemented a solution that uses Cloud Spanner and notices some read latency-related performance issues on one table. This table is accessed only by their users using a primary key. The table schema is shown below. You want to resolve the issue. What should you do?",
            "o1": "Ensure the Primary Key does not cause hotspots (e.g., avoid monotonically increasing keys like timestamps).",
            "o2": "Add a secondary index.",
            "o3": "Increase the node count.",
            "o4": "Use a smaller table name.",
            "ans": 1
        },
        {
            "q": "Your finance team wants to view the billing report for your projects. You want to make sure that the finance team does not get additional permissions to the project. What should you do?",
            "o1": "Grant 'Billing Account Viewer' role on the Billing Account.",
            "o2": "Grant 'Project Viewer' role.",
            "o3": "Grant 'Billing Project Manager'.",
            "o4": "Export the bill to CSV and email it.",
            "ans": 1
        },
        {
            "q": "Your organization has strict requirements to control access to Google Cloud projects. You need to enable your Site Reliability Engineers (SREs) to approve requests from the Google Cloud support team when an SRE opens a support case. You want to follow Google-recommended practices. What should you do?",
            "o1": "Use Access Approval.",
            "o2": "Use VPC Service Controls.",
            "o3": "Use Identity-Aware Proxy.",
            "o4": "Use 2-Step Verification.",
            "ans": 1
        },
        {
            "q": "You need to host an application on a Compute Engine instance in a project shared with other teams. You want to prevent the other teams from accidentally causing downtime on that application. Which feature should you use?",
            "o1": "Enable 'Deletion Protection' on the instance.",
            "o2": "Use a Preemptible instance.",
            "o3": "Use a Shielded VM.",
            "o4": "Monitor the potential downtime.",
            "ans": 1
        },
        {
            "q": "Your organization needs to grant users access to query datasets in BigQuery but prevent them from accidentally deleting the datasets. You want a solution that follows Google-recommended practices. What should you do?",
            "o1": "Grant the 'BigQuery Data Viewer' and 'BigQuery Job User' roles.",
            "o2": "Grant the 'BigQuery Admin' role.",
            "o3": "Grant the 'Project Editor' role.",
            "o4": "Grant the 'BigQuery Data Owner' role.",
            "ans": 1
        },
        {
            "q": "You have a developer laptop with the Cloud SDK installed on Ubuntu. The Cloud SDK was installed from the Google Cloud Ubuntu package repository. You want to test your application locally on your laptop with Cloud Datastore. What should you do?",
            "o1": "Install the 'google-cloud-sdk-datastore-emulator' component and run it.",
            "o2": "Connect directly to the production Datastore.",
            "o3": "Run a Redis container.",
            "o4": "It is not possible to test Datastore locally.",
            "ans": 1
        },
        {
            "q": "Your company set up a complex organizational structure on Google Cloud. The structure includes hundreds of folders and projects. Only a few team members should be able to view the hierarchical structure. You need to assign minimum permissions to these team members, and you want to follow Google-recommended practices. What should you do?",
            "o1": "Grant the 'Organization Viewer' and 'Folder Viewer' roles.",
            "o2": "Grant the 'Organization Admin' role.",
            "o3": "Grant the 'Project Viewer' role on all projects.",
            "o4": "Grant the 'Browser' role on the Organization.",
            "ans": 1
        },
        {
            "q": "Your company has a single sign-on (SSO) identity provider that supports Security Assertion Markup Language (SAML) integration with service providers. Your company has users in Cloud Identity. You would like users to authenticate using your company's SSO provider. What should you do?",
            "o1": "Configure SAML SSO in the Google Admin Console.",
            "o2": "Use Directory Sync.",
            "o3": "Use LDAP Sync.",
            "o4": "Re-create users manually.",
            "ans": 1
        },
        {
            "q": "Your organization has a dedicated person who creates and manages all service accounts for Google Cloud projects. You need to assign this person the minimum role for projects. What should you do?",
            "o1": "Grant the 'Service Account Admin' role.",
            "o2": "Grant the 'Project Owner' role.",
            "o3": "Grant the 'IAM Security Admin' role.",
            "o4": "Grant the 'Service Account User' role.",
            "ans": 1
        },
        {
            "q": "You are building an archival solution for your data warehouse and have selected Cloud Storage to archive your data. Your users need to be able to access this archived data once a quarter for some regulatory requirements. You want to select a cost-efficient option. Which storage option should you use?",
            "o1": "Coldline Storage (accessed less than once a month).",
            "o2": "Nearline Storage (accessed less than once a month).",
            "o3": "Archive Storage (accessed less than once a year).",
            "o4": "Standard Storage.",
            "ans": 1
        },
        {
            "q": "A team of data scientists infrequently needs to use a Google Kubernetes Engine (GKE) cluster that you manage. They require GPUs for some long-running, nonrestartable jobs. You want to minimize cost. What should you do?",
            "o1": "Create a Node Pool with GPUs and enable autoscaling (scale to 0 when not in use).",
            "o2": "Use Preemptible instances with GPUs.",
            "o3": "Use a standard cluster.",
            "o4": "Create a new cluster every time.",
            "ans": 1
        },
        {
            "q": "Your organization has user identities in Active Directory. Your organization wants to use Active Directory as their source of truth for identities. Your organization wants to have full control over the Google accounts used by employees for all Google services, including your Google Cloud Platform (GCP) organization. What should you do?",
            "o1": "Use Google Cloud Directory Sync (GCDS) to sync users from AD to Cloud Identity.",
            "o2": "Use a csv import.",
            "o3": "Manually create users.",
            "o4": "Federate with SAML directly without syncing.",
            "ans": 1
        },
        {
            "q": "You have successfully created a development environment in a project for an application. This application uses Compute Engine and Cloud SQL. Now you need to create a production environment for this application. The security team has forbidden the existence of network routes between these 2 environments and has asked you to follow Google-recommended practices. What should you do?",
            "o1": "Create the production environment in a separate Google Cloud Project (and thus separate VPC).",
            "o2": "Use a separate VPC in the same project.",
            "o3": "Use Firewall rules to block traffic.",
            "o4": "Use different subnets.",
            "ans": 1
        },
        {
            "q": "Your management has asked an external auditor to review all the resources in a specific project. The security team has enabled the Organization Policy called Domain Restricted Sharing on the organization node by specifying only your Cloud Identity domain. You want the auditor to only be able to view, but not modify, the resources in that project. What should you do?",
            "o1": "Temporarily override the Org Policy for that project, or add the auditor to the Cloud Identity domain.",
            "o2": "Disable the Org Policy globally.",
            "o3": "Grant the auditor project ownership.",
            "o4": "Send them screenshots.",
            "ans": 1
        },
        {
            "q": "You have a workload running on Compute Engine that is critical to your business. You want to ensure that the data on the boot disk of this workload is backed up regularly. You need to be able to restore a backup as quickly as possible in case of disaster. You also want older backups to be cleaned automatically to save on cost. You want to follow Google-recommended practices. What should you do?",
            "o1": "Use Scheduled Snapshots (Snapshot Schedule) with a retention policy.",
            "o2": "Use a Cron job to run 'gcloud compute disks snapshot'.",
            "o3": "Back up to Cloud Storage.",
            "o4": "Use Machine Images.",
            "ans": 1
        },
        {
            "q": "You need to assign a Cloud Identity and Access Management (Cloud IAM) role to an external auditor. The auditor needs to have permissions to review your Google Cloud Platform (GCP) Audit Logs and also to review your Data Access logs. What should you do?",
            "o1": "Grant the 'Private Logs Viewer' role.",
            "o2": "Grant the 'Logs Viewer' role.",
            "o3": "Grant the 'Monitoring Viewer' role.",
            "o4": "Grant the 'Project Viewer' role.",
            "ans": 1
        },
        {
            "q": "You are managing several Google Cloud Platform (GCP) projects and need access to all logs for the past 60 days. You want to be able to explore and quickly analyze the log contents. You want to follow Google-recommended practices to obtain the combined logs for all projects. What should you do?",
            "o1": "Configure a Log Sink in each project (or aggregated at Folder/Org level) to export to a central BigQuery dataset.",
            "o2": "Use the Logs Viewer in each project.",
            "o3": "Export to Cloud Storage.",
            "o4": "Export to Pub/Sub.",
            "ans": 1
        },
        {
            "q": "You need to reduce GCP service costs for a division of your company using the fewest possible steps. You need to turn off all configured services in an existing GCP project. What should you do?",
            "o1": "Disable billing on the project.",
            "o2": "Delete all resources manually.",
            "o3": "Delete the project.",
            "o4": "Stop all VM instances.",
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
    
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 4).")

if __name__ == "__main__":
    populate_quiz_part4()
