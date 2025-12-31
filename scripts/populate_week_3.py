import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

# Mapping: Day Number -> Markdown Filename
# Logic:
# Day 15: IAM Core (Sec 12)
# Day 16: Service Accounts (Sec 13)
# Day 17: Logging & Monitoring (Sec 14)
# Day 18: Cloud Shell (Sec 15) - wait, this file content seems to be about shell.
# Day 19: App Engine (Sec 16) - wait, App Engine is usually compute/serverless (Week 4?). 
# Let's check the files again.
# The user's task.md listed:
# - Day 15: IAM Core (Sec 12)
# - Day 16: Service Accounts (Sec 13)
# - Day 17: Logging/Ops (Sec 14)
# - Day 18: Cloud Shell (Sec 15 in task.md, but Sec 21 in file list? Let's use sec_15_cloud_shell.md if exists)
# - Day 19: Advanced IAM / Security Operations (Sec 17 Advanced IAM?)
# - Day 20: Security Ops / Backup DR? (Sec 20 Security Ops)
# - Day 21: Week 3 Review

DAY_MAPPING = {
    15: "section_12_iam_core.md",
    16: "section_13_service_accounts.md",
    17: "section_14_logging_monitoring.md",
    18: "section_15_cloud_shell.md", 
    19: "section_17_advanced_iam.md", # Advanced IAM fitting for late week 3
    20: "section_20_security_operations.md", # Sec Ops fitting for week 3
    21: "section_week_3_review.md"
}

def read_markdown(filename):
    path = os.path.join("curriculum", "content", filename)
    if not os.path.exists(path):
        print(f"Warning: {filename} not found.")
        return None, None
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract Title from first line "# Title"
    lines = content.split('\n')
    title = lines[0].replace("#", "").strip() if lines else "Untitled"
    if ":" in title:
        title = title.split(":", 1)[1].strip()
        
    return title, content

def populate_week3():
    for day_num, filename in DAY_MAPPING.items():
        title, content = read_markdown(filename)
        if not content:
            continue
            
        day, created = Day.objects.get_or_create(number=day_num)
        
        day.title = title
        
        # Split logic
        if "## 6️⃣ Hands-On Lab" in content:
            parts = content.split("## 6️⃣ Hands-On Lab")
            day.concept_content = parts[0].strip()
            day.hands_on_content = "## 6️⃣ Hands-On Lab" + parts[1].strip()
        elif "## 5️⃣ Hands-On Lab" in content:
            parts = content.split("## 5️⃣ Hands-On Lab")
            day.concept_content = parts[0].strip()
            day.hands_on_content = "## 5️⃣ Hands-On Lab" + parts[1].strip()
        elif "## 4️⃣ Hands-On Lab" in content: 
             parts = content.split("## 4️⃣ Hands-On Lab")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 4️⃣ Hands-On Lab" + parts[1].strip()
        elif "## 5️⃣ Console Walkthrough" in content: 
             parts = content.split("## 5️⃣ Console Walkthrough")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 5️⃣ Console Walkthrough" + parts[1].strip()
        elif "## 6️⃣ Console Walkthrough" in content: 
             parts = content.split("## 6️⃣ Console Walkthrough")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 6️⃣ Console Walkthrough" + parts[1].strip()
        elif "## 6️⃣ Hands-On" in content:
             parts = content.split("## 6️⃣ Hands-On") 
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 6️⃣ Hands-On" + parts[1].strip()
        elif "## 5. Hands-on Lab" in content:
             parts = content.split("## 5. Hands-on Lab")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 5. Hands-on Lab" + parts[1].strip()
        else:
             day.concept_content = content
             day.hands_on_content = ""
             
        day.week_id = 3 # Ensure it's in Week 3
        day.save()
        print(f"Updated Day {day_num}: {day.title}")

if __name__ == "__main__":
    populate_week3()
