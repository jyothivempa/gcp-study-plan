import os
import django
import sys
import codecs
import re

# Force utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

DAYS_CONFIG = {
    22: {
        "file": "section_22_cloud_ops.md",
        "outcome": "Monitor & Log Applications",
        "quizzes": [
            {"text": "Service for Metrics (CPU/RAM)?", "type": "mcq", "options": ["A. Logging", "B. Monitoring", "C. Trace", "D. Debugger"], "correct": 2},
            {"text": "How to get Email on High CPU?", "type": "mcq", "options": ["A. Uptime Check", "B. Alerting Policy", "C. Dashboard", "D. Log"], "correct": 2},
            {"text": "Why apply Ops Agent?", "type": "mcq", "options": ["A. For fun", "B. To see Memory/Disk (Internals)", "C. For CPU", "D. For Network"], "correct": 2},
            {"text": "Check web server availability globally?", "type": "mcq", "options": ["A. Uptime Check", "B. Ping", "C. SSH", "D. Trace"], "correct": 1},
            {"text": "Service for searching Error text?", "type": "mcq", "options": ["A. Monitoring", "B. Logging", "C. Billing", "D. IAM"], "correct": 2}
        ]
    },
    23: {
        "file": "section_23_iam_advanced.md",
        "outcome": "Manage Service Accounts",
        "quizzes": [
            {"text": "Account for a machine?", "type": "mcq", "options": ["A. User", "B. Service Account", "C. Group", "D. Domain"], "correct": 2},
            {"text": "Best way to auth a VM?", "type": "mcq", "options": ["A. JSON Key", "B. Attached Service Account", "C. Password", "D. SSH Key"], "correct": 2},
            {"text": "Action if Key is leaked?", "type": "mcq", "options": ["A. Hide it", "B. Revoke immediately", "C. Nothing", "D. Email Google"], "correct": 2},
            {"text": "Tool to debug Permission Denied?", "type": "mcq", "options": ["A. Logs", "B. Policy Troubleshooter", "C. Monitor", "D. Shell"], "correct": 2},
            {"text": "Default Compute SA role?", "type": "mcq", "options": ["A. Viewer", "B. Editor", "C. None", "D. Owner"], "correct": 2}
        ]
    },
    24: {
        "file": "section_24_network_security.md",
        "outcome": "Secure Networks with Firewall & IAP",
        "quizzes": [
            {"text": "How to SSH with No Public IP?", "type": "mcq", "options": ["A. Impossible", "B. IAP", "C. VPN only", "D. Magic"], "correct": 2},
            {"text": "Default Ingress rule?", "type": "mcq", "options": ["A. Allow All", "B. Deny All", "C. Allow Internal", "D. Allow HTTP"], "correct": 2},
            {"text": "Target specific VMs in Firewall?", "type": "mcq", "options": ["A. Network Tags", "B. Name", "C. IP", "D. Size"], "correct": 1},
            {"text": "Service for DDoS protection?", "type": "mcq", "options": ["A. NAT", "B. Cloud Armor", "C. DNS", "D. CDN"], "correct": 2},
            {"text": "Priority logic?", "type": "mcq", "options": ["A. Higher wins", "B. Lower number wins (1 overrides 1000)", "C. Last rule wins", "D. First rule wins"], "correct": 2}
        ]
    },
    25: {
        "file": "section_25_data_security.md",
        "outcome": "Implement Encryption Keys",
        "quizzes": [
            {"text": "Default GCP Encryption state?", "type": "mcq", "options": ["A. None", "B. Encrypted at Rest & Transit", "C. Paid", "D. Transit only"], "correct": 2},
            {"text": "Key managed by You (Revocable)?", "type": "mcq", "options": ["A. Default", "B. CMEK (KMS)", "C. HTTPS", "D. SSL"], "correct": 2},
            {"text": "Risk of destroying CMEK key?", "type": "mcq", "options": ["A. None", "B. Data lost forever", "C. Google restores", "D. Key rotates"], "correct": 2},
            {"text": "Service CMEK works with?", "type": "mcq", "options": ["A. Storage", "B. SQL", "C. Compute", "D. All of above"], "correct": 4},
            {"text": "Service to find Sensitive Data (DLP)?", "type": "mcq", "options": ["A. Armor", "B. Cloud DLP", "C. KMS", "D. IAM"], "correct": 2}
        ]
    },
    26: {
        "file": "section_26_billing_management.md",
        "outcome": "Manage Cost & Billing",
        "quizzes": [
            {"text": "Does Budget stop services?", "type": "mcq", "options": ["A. Yes", "B. No (Alerts only)", "C. Only VMs", "D. Only SQL"], "correct": 2},
            {"text": "Hard limit on resource count?", "type": "mcq", "options": ["A. Budget", "B. Quota", "C. Firewall", "D. IAM"], "correct": 2},
            {"text": "Analyze spending via SQL?", "type": "mcq", "options": ["A. Report", "B. Billing Export to BigQuery", "C. Monitor", "D. Logs"], "correct": 2},
            {"text": "Who links Project to Billing?", "type": "mcq", "options": ["A. Editor", "B. Billing Account User", "C. Viewer", "D. Owner"], "correct": 2},
            {"text": "Best way to categorize cost (Dev/Prod)?", "type": "mcq", "options": ["A. Cards", "B. Labels", "C. Quotas", "D. Names"], "correct": 2}
        ]
    },
    27: {
        "file": "section_27_iac.md",
        "outcome": "Understand Infrastructure as Code",
        "quizzes": [
            {"text": "Benefit of IaC?", "type": "mcq", "options": ["A. Speed", "B. Reproducibility/Git", "C. GUI", "D. Fun"], "correct": 2},
            {"text": "GCP Native IaC tool?", "type": "mcq", "options": ["A. Build", "B. Deployment Manager", "C. Spanner", "D. Run"], "correct": 2},
            {"text": "Terraform style?", "type": "mcq", "options": ["A. Imperative", "B. Declarative", "C. Script", "D. Manual"], "correct": 2},
            {"text": "Result of applying Terraform twice?", "type": "mcq", "options": ["A. Error", "B. Idempotent (Nothing changes)", "C. Duplicate", "D. Delete"], "correct": 2},
            {"text": "Where to store Terraform?", "type": "mcq", "options": ["A. Bucket", "B. Git Repo", "C. Disk", "D. Email"], "correct": 2}
        ]
    },
    28: {
        "file": "section_28_week_4_review.md",
        "outcome": "Week 4 Review & Exam Readiness",
        "quizzes": [
            {"text": "Prevent expensive GPU spinup?", "type": "mcq", "options": ["A. Budget", "B. Quota", "C. IAM", "D. Firewall"], "correct": 2},
            {"text": "Cannot see Memory in Monitor?", "type": "mcq", "options": ["A. Delay", "B. No Ops Agent", "C. Bug", "D. Setting"], "correct": 2},
            {"text": "SSH private VM safely?", "type": "mcq", "options": ["A. Public IP", "B. IAP", "C. VPN", "D. Open Port"], "correct": 2},
            {"text": "Who holds Default keys?", "type": "mcq", "options": ["A. You", "B. Google", "C. KMS", "D. NSA"], "correct": 2},
            {"text": "Budget threshold met?", "type": "mcq", "options": ["A. Stop", "B. Alert only", "C. Delete", "D. Throttle"], "correct": 2},
            {"text": "App to Bucket auth?", "type": "mcq", "options": ["A. Key", "B. Service Account", "C. User", "D. Public"], "correct": 2},
            {"text": "Firewall priority winner?", "type": "mcq", "options": ["A. 1000", "B. 100", "C. 65000", "D. Last"], "correct": 2},
            {"text": "Benefit of Declarative?", "type": "mcq", "options": ["A. Step by step", "B. Idempotent/State", "C. Python", "D. Fast"], "correct": 2},
            {"text": "SQL Billing Analysis?", "type": "mcq", "options": ["A. CSV", "B. BigQuery Export", "C. Logs", "D. Trace"], "correct": 2},
            {"text": "Cloud Armor purpose?", "type": "mcq", "options": ["A. Encrypt", "B. DDoS/Web Protection", "C. Firewall", "D. IAM"], "correct": 2}
        ]
    }
}

def update_week4():
    print("🚀 Updating Week 4 Content (Days 22-28)...")
    base_path = r"d:\ultimateCode\gcp_study_plan\curriculum\content"
    
    for day_num, config in DAYS_CONFIG.items():
        print(f"\nProcessing Day {day_num}...")
        file_path = os.path.join(base_path, config["file"])
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            full_content = f.read()
            
        split_marker = None
        if "## 🛠️" in full_content:
             for line in full_content.split('\n'):
                if "## 🛠️" in line:
                    split_marker = line
                    break
        elif "## 🧪" in full_content:
             for line in full_content.split('\n'):
                if "## 🧪" in line:
                    split_marker = line
                    break
        
        concept_content = full_content
        hands_on_content = ""
        
        if split_marker:
            parts = full_content.split(split_marker)
            if len(parts) >= 2:
                concept_content = parts[0].strip()
                hands_on_content = split_marker + parts[1]
        
        try:
            # Week 4
            day, created = Day.objects.get_or_create(number=day_num, defaults={'title': f"Day {day_num}", 'week_id': 4})
            
            first_line = full_content.split('\n')[0].replace("# ", "").strip()
            clean_title = re.sub(r"^Day \d+: ", "", first_line)
            
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.week_id = 4 # Ensure week assignment
            day.save()
            print(f"✅ Day {day_num} Updated: {clean_title}")

            day.quiz_questions.all().delete()
            for q in config["quizzes"]:
                QuizQuestion.objects.create(
                    day=day,
                    question_type=q["type"],
                    question_text=q["text"],
                    option_1=q["options"][0],
                    option_2=q["options"][1],
                    option_3=q["options"][2],
                    option_4=q["options"][3],
                    correct_option=q["correct"],
                    explanation="Correct answer selected."
                )
            print(f"   - Added {len(config['quizzes'])} quiz questions.")

        except Exception as e:
            print(f"❌ Error updating Day {day_num}: {e}")

if __name__ == "__main__":
    update_week4()
