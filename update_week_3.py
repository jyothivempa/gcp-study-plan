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
    15: {
        "file": "section_15_containers.md",
        "outcome": "Build & Run Docker Containers",
        "quizzes": [
            {"text": "Best description of a Container?", "type": "mcq", "options": ["A. Physical Server", "B. Lightweight package sharing Host OS", "C. Heavy Virtual Machine", "D. Database"], "correct": 2},
            {"text": "Recipe file to build an image?", "type": "mcq", "options": ["A. Makefile", "B. Dockerfile", "C. Imagefile", "D. Build.xml"], "correct": 2},
            {"text": "Main benefit vs VM?", "type": "mcq", "options": ["A. Larger size", "B. Faster start & less resources", "C. GUI", "D. More expensive"], "correct": 2},
            {"text": "Command to run a container?", "type": "mcq", "options": ["A. docker build", "B. docker run", "C. docker push", "D. docker pull"], "correct": 2},
            {"text": "Where can containers run?", "type": "mcq", "options": ["A. GKE only", "B. Anywhere with runtime (Laptop/Cloud)", "C. Only Linux", "D. Only Windows"], "correct": 2}
        ]
    },
    16: {
        "file": "section_16_kubernetes_arch.md",
        "outcome": "Understand Kubernetes Architecture",
        "quizzes": [
            {"text": "The 'Brain' of the cluster?", "type": "mcq", "options": ["A. Worker Node", "B. Control Plane", "C. Kubelet", "D. Pod"], "correct": 2},
            {"text": "Where do containers run?", "type": "mcq", "options": ["A. ETCD", "B. Worker Nodes", "C. Master", "D. Cloud SQL"], "correct": 2},
            {"text": "Who manages Control Plane in GKE?", "type": "mcq", "options": ["A. You", "B. Google (Fully Managed)", "C. AWS", "D. Your ISP"], "correct": 2},
            {"text": "Database storing cluster state?", "type": "mcq", "options": ["A. Redis", "B. etcd", "C. MySQL", "D. Mongo"], "correct": 2},
            {"text": "Agent on Worker Node?", "type": "mcq", "options": ["A. Docker", "B. Kubelet", "C. Scheduler", "D. API Server"], "correct": 2}
        ]
    },
    17: {
        "file": "section_17_gke_modes.md",
        "outcome": "Choose between GKE Standard & Autopilot",
        "quizzes": [
            {"text": "Who upgrades Node OS in Standard?", "type": "mcq", "options": ["A. Google", "B. You (Responsible for config)", "C. Nobody", "D. Auto"], "correct": 2},
            {"text": "What do you pay for in Autopilot?", "type": "mcq", "options": ["A. Nodes", "B. Pods (CPU/RAM request)", "C. Cluster fee", "D. Traffic"], "correct": 2},
            {"text": "Mode with best security defaults (No root)?", "type": "mcq", "options": ["A. Standard", "B. Autopilot", "C. Both", "D. None"], "correct": 2},
            {"text": "Mode for custom drivers/OS mods?", "type": "mcq", "options": ["A. Autopilot", "B. Standard", "C. Cloud Run", "D. App Engine"], "correct": 2},
            {"text": "Recommended for K8s beginners/Prod?", "type": "mcq", "options": ["A. Autopilot", "B. Standard", "C. Unmanaged", "D. Manual"], "correct": 1}
        ]
    },
    18: {
        "file": "section_18_workloads.md",
        "outcome": "Deploy Pods & Deployments",
        "quizzes": [
            {"text": "Smallest unit in K8s?", "type": "mcq", "options": ["A. Container", "B. Pod", "C. Node", "D. Cluster"], "correct": 2},
            {"text": "Why use Deployment vs Pod?", "type": "mcq", "options": ["A. Speed", "B. Self-healing & Scaling", "C. Cheaper", "D. Simpler"], "correct": 2},
            {"text": "What do containers in a Pod share?", "type": "mcq", "options": ["A. Nothing", "B. IP Address & Storage", "C. Image", "D. Memory"], "correct": 2},
            {"text": "To run 5 copies, configure:", "type": "mcq", "options": ["A. replicas: 5", "B. copies: 5", "C. run 5", "D. scale 5"], "correct": 1},
            {"text": "Object ensuring N healthy pods run?", "type": "mcq", "options": ["A. Scheduler", "B. ReplicaSet", "C. Kubelet", "D. API"], "correct": 2}
        ]
    },
    19: {
        "file": "section_19_services.md",
        "outcome": "Expose Applications with Services",
        "quizzes": [
            {"text": "Why not use Pod IP?", "type": "mcq", "options": ["A. Slow", "B. Ephemeral (Changes on restart)", "C. Private", "D. Static"], "correct": 2},
            {"text": "Service type for Public Internet access?", "type": "mcq", "options": ["A. ClusterIP", "B. LoadBalancer", "C. NodePort", "D. Internal"], "correct": 2},
            {"text": "Default internal-only service?", "type": "mcq", "options": ["A. ClusterIP", "B. NodePort", "C. LB", "D. Gateway"], "correct": 1},
            {"text": "Smart router for paths (/api vs /web)?", "type": "mcq", "options": ["A. Service", "B. Ingress", "C. Router", "D. Firewall"], "correct": 2},
            {"text": "How Service finds Pods?", "type": "mcq", "options": ["A. Magic", "B. Labels & Selectors", "C. Names", "D. IPs"], "correct": 2}
        ]
    },
    20: {
        "file": "section_20_config_secrets.md",
        "outcome": "Manage ConfigMaps & Secrets",
        "quizzes": [
            {"text": "Object for Database Password?", "type": "mcq", "options": ["A. ConfigMap", "B. Secret", "C. Pod", "D. Env"], "correct": 2},
            {"text": "Object for CSS Theme (Public)?", "type": "mcq", "options": ["A. ConfigMap", "B. Secret", "C. Volume", "D. Disk"], "correct": 1},
            {"text": "Why not hardcode config?", "type": "mcq", "options": ["A. Performance", "B. Portability (Dev vs Prod)", "C. Syntax", "D. Space"], "correct": 2},
            {"text": "Are Secrets encrypted in GKE?", "type": "mcq", "options": ["A. No", "B. Yes (At rest by default)", "C. Only Enterprise", "D. Never"], "correct": 2},
            {"text": "How to consume ConfigMap?", "type": "mcq", "options": ["A. Env Var", "B. Volume", "C. Both A and B", "D. Network"], "correct": 3}
        ]
    },
    21: {
        "file": "section_21_week_3_review.md",
        "outcome": "Week 3 Review & Exam Readiness",
        "quizzes": [
            {"text": "Minimize ops, no node mgmt?", "type": "mcq", "options": ["A. Standard", "B. Autopilot", "C. Compute", "D. Run"], "correct": 2},
            {"text": "Ensures 3 copies always run?", "type": "mcq", "options": ["A. Pod", "B. Deployment", "C. Service", "D. Secret"], "correct": 2},
            {"text": "Expose HTTP to public?", "type": "mcq", "options": ["A. LoadBalancer Service", "B. ClusterIP", "C. Deployment", "D. Secret"], "correct": 1},
            {"text": "Store Private API Key?", "type": "mcq", "options": ["A. Dockerfile", "B. Secret", "C. ConfigMap", "D. Label"], "correct": 2},
            {"text": "Kubelet role?", "type": "mcq", "options": ["A. Schedule", "B. Database", "C. Node Agent (Starts containers)", "D. API"], "correct": 3},
            {"text": "Pod to Pod comms?", "type": "mcq", "options": ["A. Pod IP", "B. Service Name (Stable)", "C. Node IP", "D. MAC"], "correct": 2},
            {"text": "Build image definition?", "type": "mcq", "options": ["A. yaml", "B. Dockerfile", "C. json", "D. xml"], "correct": 2},
            {"text": "Route based on path (/video)?", "type": "mcq", "options": ["A. Service", "B. Ingress", "C. NodePort", "D. VPC"], "correct": 2},
            {"text": "Who patches Node OS in Standard?", "type": "mcq", "options": ["A. Google", "B. You (Config required)", "C. Magic", "D. None"], "correct": 2},
            {"text": "Stateless app?", "type": "mcq", "options": ["A. Saves to disk", "B. Saves to external DB (Ephemeral pods)", "C. No restart", "D. No IP"], "correct": 2}
        ]
    }
}

def update_week3():
    print("🚀 Updating Week 3 Content (Days 15-21)...")
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
            # Week 3
            day, created = Day.objects.get_or_create(number=day_num, defaults={'title': f"Day {day_num}", 'week_id': 3})
            
            first_line = full_content.split('\n')[0].replace("# ", "").strip()
            clean_title = re.sub(r"^Day \d+: ", "", first_line)
            
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.week_id = 3 # Ensure week assignment
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
    update_week3()
