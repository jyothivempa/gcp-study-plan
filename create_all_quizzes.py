import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

# Clear all existing quizzes
QuizQuestion.objects.all().delete()
print("[OK] Cleared all existing quizzes")

# Quiz data for all days (Days 1-8 initially, can add more)
QUIZZES = {
    1: [  # Day 1 - 5 quizzes
        {"question_text": "What is cloud computing?", "options": ["A. Remote servers", "B. Physical hardware", "C. Local storage", "D. None"], "correct_answer": 1},
        {"question_text": "Which is a Google Cloud region?", "options": ["A. us-east1", "B. aws-west", "C. azure-central", "D. None"], "correct_answer": 1},
        {"question_text": "What is GCP Console?", "options": ["A. Web UI", "B. Command line", "C. API", "D. SDK"], "correct_answer": 1},
        {"question_text": "Cloud storage benefit?", "options": ["A. Scalability", "B. Fixed cost", "C. Local only", "D. Limited"], "correct_answer": 1},
        {"question_text": "GCP stands for?", "options": ["A. Google Cloud Platform", "B. General Computing", "C. Global CPU", "D. None"], "correct_answer": 1},
    ],
    2: [  # Day 2 - 5 quizzes
        {"question_text": "What is a GCP Project?", "options": ["A. Resource container", "B. VM only", "C. User account", "D. Billing"], "correct_answer": 1},
        {"question_text": "Resource Hierarchy top level?", "options": ["A. Organization", "B. Folder", "C. Project", "D. Resource"], "correct_answer": 1},
        {"question_text": "What is a Zone?", "options": ["A. Datacenter", "B. Region", "C. Project", "D. Folder"], "correct_answer": 1},
        {"question_text": "Multi-region benefit?", "options": ["A. High availability", "B. Low cost", "C. Simple", "D. Local"], "correct_answer": 1},
        {"question_text": "Region contains?", "options": ["A. Multiple zones", "B. One zone", "C. Projects", "D. Users"], "correct_answer": 1},
    ],
    3: [  # Day 3 - 5 quizzes  
        {"question_text": "Compute Engine provides?", "options": ["A. Virtual machines", "B. Containers", "C. Serverless", "D. Desktop"], "correct_answer": 1},
        {"question_text": "Machine type defines?", "options": ["A. CPU & Memory", "B. Storage only", "C. Network", "D. Region"], "correct_answer": 1},
        {"question_text": "Preemptible VM use case?", "options": ["A. Batch processing", "B. Production DB", "C. Critical app", "D. User auth"], "correct_answer": 1},
        {"question_text": "VM can be?", "options": ["A. Started/Stopped", "B. Only running", "C. Never stopped", "D. Deleted auto"], "correct_answer": 1},
        {"question_text": "Custom machine type?", "options": ["A. Custom CPU/RAM", "B. Fixed only", "C. Not possible", "D. Auto-sized"], "correct_answer": 1},
    ],
    4: [  # Day 4 - 5 quizzes
        {"question_text": "Cloud Storage class for archival?", "options": ["A. Standard", "B. Nearline", "C. Coldline", "D. Archive"], "correct_answer": 4},
        {"question_text": "Default storage class?", "options": ["A. Standard", "B. Nearline", "C. Coldline", "D. Archive"], "correct_answer": 1},
        {"question_text": "Lifecycle policy enables?", "options": ["A. Bucket Lock", "B. Auto-delete/transition", "C. Versioning", "D. Retention"], "correct_answer": 2},
        {"question_text": "Nearline minimum duration?", "options": ["A. 0 days", "B. 30 days", "C. 90 days", "D. 365 days"], "correct_answer": 2},
        {"question_text": "Upload large files with?", "options": ["A. gcloud storage", "B. gsutil", "C. Both A and B", "D. bq"], "correct_answer": 3},
    ],
    5: [  # Day 5 - 3 quizzes
        {"question_text": "Persistent Disk types?", "options": ["A. Standard & SSD", "B. HDD only", "C. RAM only", "D. Network"], "correct_answer": 1},
        {"question_text": "Local SSD is?", "options": ["A. Ephemeral", "B. Persistent", "C. Network", "D. Cloud"], "correct_answer": 1},
        {"question_text": "Disk can be?", "options": ["A. Attached to VM", "B. Standalone", "C. Both", "D. Neither"], "correct_answer": 3},
    ],
    6: [  # Day 6 - 5 quizzes
        {"question_text": "IAM stands for?", "options": ["A. Identity & Access Management", "B. Internet Access", "C. Internal Auth", "D. IP Address"], "correct_answer": 1},
        {"question_text": "IAM Role contains?", "options": ["A. Permissions", "B. Users", "C. Resources", "D. Regions"], "correct_answer": 1},
        {"question_text": "Service Account is for?", "options": ["A. Applications", "B. Humans only", "C. VMs only", "D. Networks"], "correct_answer": 1},
        {"question_text": "Principle of least privilege?", "options": ["A. Minimum access needed", "B. Maximum access", "C. No access", "D. Full admin"], "correct_answer": 1},
        {"question_text": "Predefined roles are?", "options": ["A. Google-managed", "B. User-created", "C. Auto-deleted", "D. None"], "correct_answer": 1},
    ],
    7: [  # Day 7 - 10 quizzes (Week 1 exam)
        {"question_text": "Cloud computing delivery model?", "options": ["A. IaaS, PaaS, SaaS", "B. On-premise only", "C. Desktop only", "D. Mobile only"], "correct_answer": 1},
        {"question_text": "GCP global infrastructure includes?", "options": ["A. Regions & Zones", "B. Cities only", "C. Countries", "D. Continents"], "correct_answer": 1},
        {"question_text": "Compute Engine best for?", "options": ["A. VMs & control", "B. Serverless", "C. Mobile apps", "D. Desktop"], "correct_answer": 1},
        {"question_text": "Cloud Storage object storage?", "options": ["A. Scalable files", "B. Block storage", "C. VM disks", "D. Databases"], "correct_answer": 1},
        {"question_text": "Persistent Disk vs Local SSD?", "options": ["A. Network vs Physical", "B. Same thing", "C. Both ephemeral", "D. Both network"], "correct_answer": 1},
        {"question_text": "IAM best practice?", "options": ["A. Regular audits", "B. Never review", "C. One-time setup", "D. Ignore"], "correct_answer": 1},
        {"question_text": "Project ID must be?", "options": ["A. Globally unique", "B. Local only", "C. Reusable", "D. Numeric"], "correct_answer": 1},
        {"question_text": "Preemptible VM can run?", "options": ["A. Up to 24 hours", "B. Forever", "C. 1 hour max", "D. 1 minute"], "correct_answer": 1},
        {"question_text": "Cloud Console is?", "options": ["A. Web-based UI", "B. CLI only", "C. Desktop app", "D. Mobile only"], "correct_answer": 1},
        {"question_text": "Resource hierarchy order?", "options": ["A. Org > Folder > Project > Resource", "B. Resource > Project", "C. Zone > Region", "D. Random"], "correct_answer": 1},
    ],
    8: [  # Day 8 - 5 quizzes
        {"question_text": "Instance Group purpose?", "options": ["A. Manage VM groups", "B. Storage", "C. Networking", "D. IAM"], "correct_answer": 1},
        {"question_text": "MIG stands for?", "options": ["A. Managed Instance Group", "B. Manual Instance", "C. Multiple IP", "D. None"], "correct_answer": 1},
        {"question_text": "Autoscaling based on?", "options": ["A. CPU, Traffic", "B. Time only", "C. Manual", "D. None"], "correct_answer": 1},
        {"question_text": "Health check monitors?", "options": ["A. VM availability", "B. Cost", "C. Region", "D. IAM"], "correct_answer": 1},
        {"question_text": "Auto-healing does?", "options": ["A. Recreates failed VMs", "B. Deletes VMs", "C. Nothing", "D. Stops VMs"], "correct_answer": 1},
    ],
}

# Create quizzes
total_created = 0
for day_number, quizzes in QUIZZES.items():
    try:
        day = Day.objects.get(number=day_number)
        for quiz_data in quizzes:
            QuizQuestion.objects.create(
                day=day,
                question_text=quiz_data["question_text"],
                question_type="mcq",
                option_1=quiz_data["options"][0] if len(quiz_data["options"]) > 0 else None,
                option_2=quiz_data["options"][1] if len(quiz_data["options"]) > 1 else None,
                option_3=quiz_data["options"][2] if len(quiz_data["options"]) > 2 else None,
                option_4=quiz_data["options"][3] if len(quiz_data["options"]) > 3 else None,
                correct_option=quiz_data["correct_answer"]
            )
            total_created += 1
        print(f"[OK] Day {day_number}: {len(quizzes)} quizzes created")
    except Day.DoesNotExist:
       print(f"[ERROR] Day {day_number} not found in database")

print(f"\n[SUCCESS] Total quizzes created: {total_created}")
