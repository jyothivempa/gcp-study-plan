import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

CAPSTONE_QUIZZES = {
    42: [
        {
            "q": "Which tool is best for tracing latency across microservices in a distributed architecture?",
            "o1": "Cloud Trace", "o2": "Cloud Logging", "o3": "Cloud Monitoring", "o4": "VPC Flow Logs",
            "a": 1, "exp": "Cloud Trace provides distributed tracing to identify latency bottlenecks."
        },
        {
            "q": "You see a spike in 502 Bad Gateway errors on your Load Balancer. What is the most likely cause?",
            "o1": "Backend instances are unhealthy or overwhelmed.", "o2": "The Load Balancer is down.", "o3": "Firewall rules blocking traffic.", "o4": "DNS propagation delay.",
            "a": 1, "exp": "502 indicates the LB cannot reach a healthy backend."
        },
        {
            "q": "How can you verify if a Firewall Rule is actually blocking traffic without disrupting production?",
            "o1": "Use Firewall Rules Logging.", "o2": "Delete the rule and see if traffic flows.", "o3": "Use Connectivity Tests in Network Intelligence Center.", "o4": "Check VPC Flow Logs.",
            "a": 3, "exp": "Connectivity Tests simulate packets to verify reachability and identify blocking rules."
        }
    ],
    43: [
        {
            "q": "Which service helps you discover, classify, and protect sensitive data like PII?",
            "o1": "Cloud DLP (Data Loss Prevention)", "o2": "Cloud Armor", "o3": "Security Command Center", "o4": "IAM",
            "a": 1, "exp": "Cloud DLP automatically scans and de-identifies sensitive data."
        },
        {
            "q": "You need to prevent developers from accidentally making Storage Buckets public. What should you use?",
            "o1": "Organization Policy 'Domain Restricted Sharing'.", "o2": "Organization Policy 'Enforce Public Access Prevention'.", "o3": "IAM Owner Role.", "o4": "VPC Service Controls.",
            "a": 2, "exp": "Enforce Public Access Prevention physically blocks public ACLs on buckets."
        },
        {
            "q": "A VM is suspected to be compromised (crypto-mining). What is the FIRST step?",
            "o1": "Isolate the VM (remove network tags / quarantine network).", "o2": "Delete the VM immediately.", "o3": "SSH in to check logs.", "o4": "Reboot the VM.",
            "a": 1, "exp": "Quarantine first to prevent lateral movement and preserve evidence for forensics."
        }
    ],
    44: [
        {
            "q": "In a CI/CD pipeline, where should you store your container images for deployment to GKE?",
            "o1": "Artifact Registry", "o2": "Cloud Storage", "o3": "Container Registry (Deprecated)", "o4": "Git Repository",
            "a": 1, "exp": "Artifact Registry is the evolution of GCR and the standard for storing container images."
        },
        {
            "q": "Which strategy allows you to release a new version to a small % of users first?",
            "o1": "Canary Deployment", "o2": "Blue/Green Deployment", "o3": "Rolling Update", "o4": "Recreate",
            "a": 1, "exp": "Canary releases route a small percentage of traffic to the new version to test stability."
        },
        {
            "q": "What is 'Infrastructure as Code'?",
            "o1": "Managing infrastructure using definition files (like Terraform).", "o2": "Writing infrastructure in Python only.", "o3": "Manually clicking in the console and saving screenshots.", "o4": "Documenting server specs in a Wiki.",
            "a": 1, "exp": "IaC uses declarative files to provision and manage resources reliably."
        }
    ],
    45: [
        {
            "q": " CEO asks for a dashboard showing real-time sales. Data is in 5 different databases. Which tool ingests this for analysis?",
            "o1": "BigQuery", "o2": "Cloud SQL", "o3": "Bigtable", "o4": "Datastore",
            "a": 1, "exp": "BigQuery is the serverless Data Warehouse designed for analytics across massive datasets."
        },
        {
            "q": "Which tool is best for 'ETL' (Extract, Transform, Load) pipelines visually?",
            "o1": "Cloud Data Fusion", "o2": "Dataflow", "o3": "Dataproc", "o4": "Pub/Sub",
            "a": 1, "exp": "Cloud Data Fusion provides a visual, drag-and-drop interface for building data pipelines."
        },
        {
            "q": "You need to process a stream of 1 Million events per second. Which service ingests this stream?",
            "o1": "Pub/Sub", "o2": "Cloud Functions", "o3": "Cloud Storage", "o4": "Cloud Tasks",
            "a": 1, "exp": "Pub/Sub is the global messaging service designed for high-throughput ingestion."
        }
    ]
}

def populate_capstone_quizzes():
    print("Populating Capstone Quizzes...")
    for day_num, questions in CAPSTONE_QUIZZES.items():
        try:
            day = Day.objects.get(number=day_num)
            # clear existing
            QuizQuestion.objects.filter(day=day).delete()
            
            for q_data in questions:
                QuizQuestion.objects.create(
                    day=day,
                    question_type='mcq',
                    question_text=q_data['q'],
                    option_1=q_data['o1'],
                    option_2=q_data['o2'],
                    option_3=q_data['o3'],
                    option_4=q_data['o4'],
                    correct_option=q_data['a'],
                    explanation=q_data['exp']
                )
            print(f"Day {day_num}: Added {len(questions)} questions.")
        except Day.DoesNotExist:
            print(f"Day {day_num} not found in DB.")

if __name__ == "__main__":
    populate_capstone_quizzes()
