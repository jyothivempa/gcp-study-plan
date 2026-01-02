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
    3: {
        "file": "section_3_compute_engine.md",
        "outcome": "Deploy & Manage Compute Engine VMs (IaaS)",
        "quizzes": [
            {"text": "Compute Engine is an example of which service model?", "type": "mcq", "options": ["A. PaaS", "B. SaaS", "C. IaaS", "D. FaaS"], "correct": 3},
            {"text": "You need to ensure your application keeps running even if a single data center loses power. What should you do?", "type": "mcq", "options": ["A. Use a bigger VM.", "B. Deploy VMs in multiple Zones.", "C. Use a specific Region.", "D. Backup to a USB drive."], "correct": 2},
            {"text": "Which machine family is best for a general-purpose web server?", "type": "mcq", "options": ["A. M2 (Memory Optimized)", "B. E2 (General Purpose)", "C. A2 (Accelerator/GPU)", "D. C2 (Compute Optimized)"], "correct": 2},
            {"text": "What does 'Allow HTTP Traffic' actually do?", "type": "mcq", "options": ["A. Installs Chrome.", "B. Creates a Firewall Rule to allow port 80.", "C. Gives you a domain name.", "D. Opens port 443"], "correct": 2},
            {"text": "True or False: You pay for a VM even if it is stopped.", "type": "mcq", "options": ["A. True (Full price)", "B. False (You only pay for the attached Disk)", "C. True, but half price", "D. False, it is free"], "correct": 2}
        ]
    },
    4: {
        "file": "section_4_cloud_storage.md",
        "outcome": "Manage Cloud Storage Buckets & Objects",
        "quizzes": [
            {"text": "Which storage class is cheapest for storing data you plan to access only once a year?", "type": "mcq", "options": ["A. Standard", "B. Nearline", "C. Archive", "D. Coldline"], "correct": 3},
            {"text": "What must be unique about a Bucket Name?", "type": "mcq", "options": ["A. Unique within your project.", "B. Globally unique across ALL of Google Cloud.", "C. Just contains your name.", "D. Unique within the Region"], "correct": 2},
            {"text": "Cloud Storage is what type of storage?", "type": "mcq", "options": ["A. Block Storage", "B. File Storage", "C. Object Storage", "D. Cold Storage"], "correct": 3},
            {"text": "How do you make a file downloadable by anyone on the internet?", "type": "mcq", "options": ["A. Send them the password.", "B. Grant the 'Storage Object Viewer' role to 'allUsers'.", "C. You cannot do this.", "D. Use a VPN"], "correct": 2},
            {"text": "Is Cloud Storage used for running an Operating System?", "type": "mcq", "options": ["A. Yes", "B. No (That's Persistent Disk)", "C. Sometimes", "D. Only Linux"], "correct": 2}   
        ]
    },
    5: {
        "file": "section_5_storage_basics.md",
        "outcome": "Understand Block Storage (Persistent Disks & Local SSD)",
        "quizzes": [
            {"text": "Which storage type is \"Ephemeral\" and loses all data if the VM is stopped?", "type": "mcq", "options": ["A. Standard Persistent Disk", "B. Local SSD", "C. Cloud Storage Bucket", "D. Hyperdisk"], "correct": 2},
            {"text": "You have a 100GB disk that is half full. You want to save money by shrinking it to 50GB. How do you do this?", "type": "mcq", "options": ["A. Edit the disk and type 50GB.", "B. You cannot shrink it. You must create a new disk and copy data.", "C. Use the \"Compression\" feature.", "D. Contact Google Support"], "correct": 2},
            {"text": "Which disk type creates a clear separation between IOPS (Performance) and Capacity (Size)?", "type": "mcq", "options": ["A. Standard HDD", "B. SSD Persistent Disk", "C. Hyperdisk", "D. Local SSD"], "correct": 3}
        ]
    },
    6: {
        "file": "section_6_iam_identity.md",
        "outcome": "Manage IAM Principals, Roles & Policies",
        "quizzes": [
            {"text": "Which component represents the 'Who' in IAM?", "type": "mcq", "options": ["A. Role", "B. Principal", "C. Policy", "D. Permission"], "correct": 2},
            {"text": "What is the 'Principle of Least Privilege'?", "type": "mcq", "options": ["A. Give everyone Owner access.", "B. Give only the permissions needed to do the job.", "C. Don't use IAM.", "D. Give access for 1 hour only"], "correct": 2},
            {"text": "Which role type should you generally AVOID in production?", "type": "mcq", "options": ["A. Predefined", "B. Custom", "C. Basic (Primitive)", "D. Service Agent"], "correct": 3},
            {"text": "Bob needs to restart VMs but shouldn't be able to delete them. Which role is best?", "type": "mcq", "options": ["A. Compute Admin", "B. Compute Instance Admin (Careful)", "C. Project Editor", "D. Project Viewer"], "correct": 2},
            {"text": "A 'Service Account' is:", "type": "mcq", "options": ["A. A billing account.", "B. An identity for a machine/application.", "C. An administrator account.", "D. A user group"], "correct": 2}
        ]
    },
    7: {
        "file": "section_7_week_1_review.md",
        "outcome": "Week 1 Review & Exam Readiness",
        "quizzes": [
             {"text": "Which Compute Engine machine family is Memory Optimized?", "type": "mcq", "options": ["A. E2", "B. C2", "C. M2", "D. N1"], "correct": 3},
             {"text": "Which storage class is cheapest for 7-year retention?", "type": "mcq", "options": ["A. Standard", "B. Nearline", "C. Archive", "D. Coldline"], "correct": 3},
             {"text": "Cannot reach web server via External IP. Most likely cause?", "type": "mcq", "options": ["A. Wrong Zone", "B. Missing Firewall Rule (Port 80)", "C. Billing Disabled", "D. No IAM"], "correct": 2},
             {"text": "Which GCP resource is Global?", "type": "mcq", "options": ["A. Subnet", "B. VM Instance", "C. VPC Network", "D. Disk"], "correct": 3},
             {"text": "Best way to give contractor upload-only access to a bucket?", "type": "mcq", "options": ["A. Project Editor", "B. Storage Object Creator on bucket", "C. Share password", "D. Public bucket"], "correct": 2},
             {"text": "Best discount for running a VM 24/7 for 3 years?", "type": "mcq", "options": ["A. Preemptible", "B. Committed Use Discounts", "C. Sustained Use", "D. Free Tier"], "correct": 2},
             {"text": "Can a Project have multiple Billing Accounts?", "type": "mcq", "options": ["A. Yes", "B. False (1 Project -> 1 Billing Account)", "C. Only in Org", "D. Yes with support"], "correct": 2},
             {"text": "Difference between IaaS and PaaS?", "type": "mcq", "options": ["A. IaaS cheaper", "B. IaaS=Infra, PaaS=Code/Runtime", "C. PaaS storage only", "D. No difference"], "correct": 2},
             {"text": "Firewall rule for 'Anywhere'?", "type": "mcq", "options": ["A. 127.0.0.1", "B. 0.0.0.0/0", "C. 192.168.0.0/16", "D. 10.0.0.0/8"], "correct": 2},
             {"text": "What is a Service Account?", "type": "mcq", "options": ["A. Support ticket", "B. Machine Identity", "C. Admin account", "D. Billing entity"], "correct": 2}
        ]
    }
}

def update_week1():
    print("🚀 Updating Week 1 Content (Days 3-7)...")
    
    # Calculate base path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "curriculum", "content")
    
    for day_num, config in DAYS_CONFIG.items():
        print(f"\nProcessing Day {day_num}...")
        file_path = os.path.join(base_path, config["file"])
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            full_content = f.read()
            
        # Flexible Splitting logic
        # Look for "Hands-On Lab" or "Mock Exam" markers
        
        split_marker = None
        if "## 🛠️" in full_content:
            # Find the header line that contains the hammer
            for line in full_content.split('\n'):
                if "## 🛠️" in line:
                    split_marker = line
                    break
        elif "## 🧪" in full_content: # For Day 7 Review
             for line in full_content.split('\n'):
                if "## 🧪" in line:
                    split_marker = line
                    break
        
        concept_content = full_content
        hands_on_content = "" # Default if no split
        
        if split_marker:
            parts = full_content.split(split_marker)
            if len(parts) >= 2:
                concept_content = parts[0].strip()
                hands_on_content = split_marker + parts[1] # Keep the header
                # Optional: Trim Quiz section from hands-on if needed, but keeping it is fine for context.
        
        # Save to DB
        try:
            day, created = Day.objects.get_or_create(number=day_num, defaults={'title': f"Day {day_num}", 'week_id': 1})
            
            # Extract Title from first line
            first_line = full_content.split('\n')[0].replace("# ", "").strip()
            # Remove "Day X: " prefix if present to keep title clean? 
            # Model has separate Title field. Let's keep the full string or parse.
            # Usually users prefer "Compute Engine" over "Day 3: Compute Engine" if the UI adds "Day 3".
            # Let's clean it up.
            clean_title = re.sub(r"^Day \d+: ", "", first_line)
            
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.save()
            print(f"✅ Day {day_num} Updated: {clean_title}")

            # Quizzes
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
                    explanation="Correct answer selected." # Generic for now as logic is hardcoded in dict
                )
            print(f"   - Added {len(config['quizzes'])} quiz questions.")

        except Exception as e:
            print(f"❌ Error updating Day {day_num}: {e}")

if __name__ == "__main__":
    update_week1()
