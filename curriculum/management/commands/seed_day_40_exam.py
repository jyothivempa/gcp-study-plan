from django.core.management.base import BaseCommand
from curriculum.models import Day, QuizQuestion

class Command(BaseCommand):
    help = 'Seeds Day 40 with 15 Hard Exam Questions'

    def handle(self, *args, **kwargs):
        day_num = 40
        try:
            day = Day.objects.get(number=day_num)
        except Day.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Day {day_num} does not exist.'))
            return

        # Update Title if needed, or keep as is.
        # day.title = "Final Exam Readiness" 
        # day.save()

        # Clear existing questions for Day 40 to avoid duplicates if run multiple times
        # Or should I append? The user said "Add these". 
        # But usually exam days are standalone. I will overwrite to ensure a clean state of these 15 hard ones 
        # plus maybe I should keep previous ones if they exist?
        # The prompt says "Add these to day 40 quiz".
        # I'll check if there are existing ones. If so, I'll append. 
        # But for now, to be safe and ensure these specific ones are prominent, I'll just add them.
        # Actually, `populate_full_curriculum` might have added some from markdown.
        # I'll chose to DELETE existing and replace with these high quality ones, 
        # OR just append. 
        # Let's append them. Removing `.delete()` call.
        
        self.stdout.write(f'Adding 15 Hard Questions to Day {day_num}...')

        questions_data = [
            {
                "text": "Scenario: A production app on Compute Engine suddenly becomes unreachable. The VM is running, CPU is normal, but users cannot connect on port 443. What is the MOST LIKELY cause?",
                "options": ["Route table misconfiguration", "Firewall rule blocking ingress", "IAM permission issue", "Disk quota exceeded"],
                "correct": 2
            },
            {
                "text": "Scenario: A team uses a service account key stored in source code for API access. Security flags this as a critical risk. What is the BEST remediation?",
                "options": ["Encrypt the key", "Rotate the key monthly", "Use service account impersonation", "Store the key in Secret Manager"],
                "correct": 3
            },
            {
                "text": "Scenario: You need to expose an internal microservice to other services in the same VPC only. Which load balancer should you use?",
                "options": ["External HTTP(S) Load Balancer", "Network Load Balancer", "Internal HTTP(S) Load Balancer", "External TCP Load Balancer"],
                "correct": 3
            },
            {
                "text": "Scenario: An application needs to scale globally and must guarantee read-after-write consistency. Which service meets this requirement?",
                "options": ["Firestore Native", "Bigtable", "Cloud SQL", "Cloud Storage"],
                "correct": 1
            },
            {
                "text": "Scenario: A VM must never receive a public IP, but must still download patches from the internet. What is REQUIRED?",
                "options": ["Private Google Access", "Cloud NAT", "VPN", "Shared VPC"],
                "correct": 2
            },
            {
                "text": "Scenario: A company wants to prevent developers from creating external IPs on any VM. What is the BEST control?",
                "options": ["Firewall rule", "IAM role restriction", "Organization Policy constraint", "Quota"],
                "correct": 3
            },
            {
                "text": "Scenario: Your batch workload runs nightly and can tolerate interruptions but must be extremely cheap. Which compute option is optimal?",
                "options": ["GKE Autopilot", "Cloud Run", "Preemptible VMs", "Committed-use VMs"],
                "correct": 3
            },
            {
                "text": "Scenario: A Kubernetes workload needs zero node management and enforced best practices. Which mode should you choose?",
                "options": ["GKE Standard", "GKE Autopilot", "Compute Engine", "Cloud Run"],
                "correct": 2
            },
            {
                "text": "Scenario: You want to ensure logs are available even if a project is deleted. Where should logs be routed?",
                "options": ["Local logging", "Same project bucket", "Centralized logging project", "Error Reporting"],
                "correct": 3
            },
            {
                "text": "Scenario: Your service must authenticate to Cloud SQL securely without credentials in code. What should you use?",
                "options": ["Database user/password", "API key", "Service account with Cloud SQL Client role", "SSH tunneling"],
                "correct": 3
            },
            {
                "text": "Scenario: A sudden spike in traffic causes increased latency, but no errors. What should you check FIRST?",
                "options": ["Disk IOPS", "CPU utilization", "Load balancer backend capacity", "IAM permissions"],
                "correct": 3
            },
            {
                "text": "Scenario: A team wants instant rollback during deployments. Which deployment strategy should be used?",
                "options": ["Rolling", "Canary", "Blue/Green", "Recreate"],
                "correct": 3
            },
            {
                "text": "Scenario: You must enforce least privilege for a CI/CD pipeline. What should you create?",
                "options": ["Editor role", "Owner role", "Custom IAM role", "Project Viewer"],
                "correct": 3
            },
            {
                "text": "Scenario: You want to expose Cloud Run only to authenticated users. What should you enable?",
                "options": ["Firewall rule", "Cloud Armor", "IAM-based authentication", "VPC peering"],
                "correct": 3
            },
            {
                "text": "Scenario: A company wants a globally distributed SQL database with 99.999% availability. Which service meets this?",
                "options": ["Cloud SQL", "Bigtable", "Firestore", "Cloud Spanner"],
                "correct": 4
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
        
        self.stdout.write(self.style.SUCCESS(f'Successfully added {count} Hard questions to Day 40.'))
