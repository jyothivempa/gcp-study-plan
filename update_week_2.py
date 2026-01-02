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
    8: {
        "file": "section_8_instance_groups.md",
        "outcome": "Manage Instance Groups & Auto-scaling",
        "quizzes": [
            {"text": "Which type of Instance Group contains identical VMs created from a template?", "type": "mcq", "options": ["A. Unmanaged", "B. Managed (MIG)", "C. Zonal", "D. Regional"], "correct": 2},
            {"text": "What happens if you manually delete a VM that belongs to a MIG?", "type": "mcq", "options": ["A. Permanent shrink", "B. MIG auto-heals (Recreates it)", "C. Nothing", "D. Error"], "correct": 2},
            {"text": "For Auto-scaling to work, your application should ideally be:", "type": "mcq", "options": ["A. Stateful", "B. Stateless", "C. Massive", "D. Monolithic"], "correct": 2},
            {"text": "Where do you define the Startup Script for a MIG?", "type": "mcq", "options": ["A. Group settings", "B. Instance Template", "C. VPC", "D. IAM"], "correct": 2},
            {"text": "Updating all VMs in a MIG without downtime is called:", "type": "mcq", "options": ["A. Hard Reset", "B. Rolling Update", "C. Hot Patch", "D. Cold Boot"], "correct": 2}
        ]
    },
    9: {
        "file": "section_9_load_balancing.md",
        "outcome": "Configure HTTP/S Load Balancing",
        "quizzes": [
            {"text": "Which Load Balancer is Global and operates at Layer 7?", "type": "mcq", "options": ["A. Network TCP", "B. External HTTP(S)", "C. UDP Passthrough", "D. Internal TCP"], "correct": 2},
            {"text": "What does a 'Health Check' do?", "type": "mcq", "options": ["A. Virus scan", "B. Checks if VM is responsive to route traffic", "C. Checks user latency", "D. Checks billing"], "correct": 2},
            {"text": "Solution for single IP traffic distribution to Asia, Europe, US?", "type": "mcq", "options": ["A. DNS LB", "B. Global HTTP LB (Anycast)", "C. VPN", "D. Router"], "correct": 2},
            {"text": "Can a Load Balancer distribute traffic to instances in different regions?", "type": "mcq", "options": ["A. Yes (Global LBs)", "B. No", "C. Only if same zone", "D. Only UDP"], "correct": 1},
            {"text": "Layer 4 Load Balancing handles:", "type": "mcq", "options": ["A. URL Paths", "B. TCP/UDP (IP/Ports)", "C. Cookies", "D. Headers"], "correct": 2}
        ]
    },
    10: {
        "file": "section_10_cloud_sql.md",
        "outcome": "Deploy & Manage Cloud SQL Databases",
        "quizzes": [
            {"text": "Which database engine is NOT supported by Cloud SQL?", "type": "mcq", "options": ["A. MySQL", "B. PostgreSQL", "C. Oracle", "D. SQL Server"], "correct": 3},
            {"text": "Relational DB that scales horizontally globally?", "type": "mcq", "options": ["A. Cloud SQL", "B. Cloud Spanner", "C. BigQuery", "D. Firestore"], "correct": 2},
            {"text": "Main benefit of Managed Cloud SQL over VM?", "type": "mcq", "options": ["A. Cheaper", "B. Google handles patching/backups", "C. Root access", "D. Faster CPU"], "correct": 2},
            {"text": "Feature to increase Read performance?", "type": "mcq", "options": ["A. HA", "B. Read Replicas", "C. SSD", "D. Failover"], "correct": 2},
            {"text": "When to use BigQuery over Cloud SQL?", "type": "mcq", "options": ["A. OLTP", "B. OLAP (Analytics on massive data)", "C. Wordpress", "D. Mobile App"], "correct": 2}
        ]
    },
    11: {
        "file": "section_11_storage_advanced.md",
        "outcome": "Configure storage Lifecycle & Security",
        "quizzes": [
            {"text": "Purpose of Lifecycle Management?", "type": "mcq", "options": ["A. Faster speed", "B. Automate cost optimization (moving classes)", "C. Encryption", "D. Backups"], "correct": 2},
            {"text": "Cost impact of overwriting a file 5 times with Versioning on?", "type": "mcq", "options": ["A. None", "B. You pay for all 5 versions", "C. Pay for 1 version", "D. Pay double"], "correct": 2},
            {"text": "Feature to let non-users upload files securely?", "type": "mcq", "options": ["A. Public bucket", "B. Signed URL", "C. IAM", "D. Password"], "correct": 2},
            {"text": "Lifecycle condition to clean up old versions?", "type": "mcq", "options": ["A. Age", "B. Number of newer versions", "C. Storage Class", "D. Size"], "correct": 2},
            {"text": "How to verify file integrity?", "type": "mcq", "options": ["A. CRC32c / MD5 Hash", "B. File size", "C. Name", "D. Date"], "correct": 1}
        ]
    },
    12: {
        "file": "section_12_app_engine.md",
        "outcome": "Deploy Apps on App Engine (PaaS)",
        "quizzes": [
            {"text": "App Engine is an example of:", "type": "mcq", "options": ["A. IaaS", "B. PaaS", "C. SaaS", "D. FaaS"], "correct": 2},
            {"text": "Which environment scales to zero?", "type": "mcq", "options": ["A. Standard", "B. Flexible", "C. Both", "D. None"], "correct": 1},
            {"text": "Environment for custom Docker containers?", "type": "mcq", "options": ["A. Standard", "B. Flexible", "C. Basic", "D. Pro"], "correct": 2},
            {"text": "Feature to test new version on 1% of traffic?", "type": "mcq", "options": ["A. A/B Check", "B. Traffic Splitting", "C. Load Balancer", "D. Router"], "correct": 2},
            {"text": "Do you need manual firewall rules for App Engine HTTP?", "type": "mcq", "options": ["A. Yes", "B. No (Auto handled)", "C. Only in Flex", "D. Only in Standard"], "correct": 2}
        ]
    },
    13: {
        "file": "section_13_cloud_run.md",
        "outcome": "Deploy Serverless Containers with Cloud Run",
        "quizzes": [
            {"text": "Deployment unit for Cloud Run?", "type": "mcq", "options": ["A. ZIP file", "B. Container Image", "C. VM", "D. JAR"], "correct": 2},
            {"text": "Can Cloud Run scale to zero?", "type": "mcq", "options": ["A. Yes", "B. No", "C. Only on weekends", "D. With extra cost"], "correct": 1},
            {"text": "Meaning of 'Stateless'?", "type": "mcq", "options": ["A. No memory", "B. No local persistence between requests", "C. No database", "D. No IP"], "correct": 2},
            {"text": "Service for Docker container on Port 8080 serverless?", "type": "mcq", "options": ["A. GKE", "B. Cloud Run", "C. Compute Engine", "D. Dataproc"], "correct": 2},
            {"text": "Cloud Run is based on which open source?", "type": "mcq", "options": ["A. Swarm", "B. Knative", "C. Terraform", "D. Ansible"], "correct": 2}
        ]
    },
    14: {
        "file": "section_14_week_2_review.md",
        "outcome": "Week 2 Review & Exam Readiness",
        "quizzes": [
            {"text": "MIG auto-healing triggers when:", "type": "mcq", "options": ["A. CPU is high", "B. Health check fails", "C. User logs out", "D. Night time"], "correct": 2},
            {"text": "Global DB with horizontal scale?", "type": "mcq", "options": ["A. Cloud SQL", "B. Cloud Spanner", "C. Bigtable", "D. Firestore"], "correct": 2},
            {"text": "App Engine Env for legacy apps requiring OS mods?", "type": "mcq", "options": ["A. Standard", "B. Flexible", "C. Cloud Functions", "D. Cloud Run"], "correct": 2},
            {"text": "LB preserving Client IP (Passthrough)?", "type": "mcq", "options": ["A. HTTP LB", "B. Network TCP/UDP LB", "C. Internal LB", "D. Proxy LB"], "correct": 2},
            {"text": "Feature to prevent deletion for legal hold?", "type": "mcq", "options": ["A. Lifecycle", "B. Retention Policy (Bucket Lock)", "C. Versioning", "D. Signed URL"], "correct": 2},
            {"text": "Cloud Run scales based on:", "type": "mcq", "options": ["A. CPU", "B. Concurrency (Requests)", "C. RAM", "D. Nodes"], "correct": 2},
            {"text": "Fastest rollback for App Engine?", "type": "mcq", "options": ["A. Re-deploy", "B. Traffic Splitting", "C. Delete", "D. Restart"], "correct": 2},
            {"text": "Fix for slow Read-heavy Cloud SQL?", "type": "mcq", "options": ["A. More CPU", "B. Read Replicas", "C. SSD", "D. Index"], "correct": 2},
            {"text": "Storage class with instant access but retrieval fees?", "type": "mcq", "options": ["A. Standard", "B. Nearline/Coldline", "C. RAM", "D. Disk"], "correct": 2},
            {"text": "Two serverless container options?", "type": "mcq", "options": ["A. Compute & GKE", "B. App Engine Flex & Cloud Run", "C. SQL & Spanner", "D. VPC & IAM"], "correct": 2}
        ]
    }
}

def update_week2():
    print("🚀 Updating Week 2 Content (Days 8-14)...")
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
        elif "## 🧪" in full_content: # For Review Days
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
            # NoteWeek ID is 2 for these days
            day, created = Day.objects.get_or_create(number=day_num, defaults={'title': f"Day {day_num}", 'week_id': 2})
            
            first_line = full_content.split('\n')[0].replace("# ", "").strip()
            clean_title = re.sub(r"^Day \d+: ", "", first_line)
            
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.week_id = 2 # Ensure week assignment
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
    update_week2()
