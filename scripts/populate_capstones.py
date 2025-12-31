import os
import django
import sys
import textwrap

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, Week, QuizQuestion

def populate_capstones():
    # 1. Create Week 7
    week7, created = Week.objects.get_or_create(
        number=7,
        defaults={"description": "Project Phase: Weeks 7"}
    )
    if created:
        print("Created Week 7.")
    else:
        week7.description = "Capstone Projects & Final Readiness"
        week7.save()
        print("Updated Week 7.")

    # 2. Populate Capstones (Days 42-45)
    # Mapping: Day -> File
    # User's files are named section_42, section_43... which align with Days 42-45
    CAPSTONE_MAPPING = {
        42: "section_42_network_capstone.md",
        43: "section_43_security_capstone.md",
        44: "section_44_devops_capstone.md",
        45: "section_45_data_capstone.md"
    }

    for day_num, filename in CAPSTONE_MAPPING.items():
        path = os.path.join("curriculum", "content", filename)
        if not os.path.exists(path):
            print(f"Skipping Day {day_num}: {filename} not found.")
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract title
        lines = content.split('\n')
        title = lines[0].replace("#", "").strip()
        if ":" in title:
            title = title.split(":", 1)[1].strip()

        day, _ = Day.objects.get_or_create(number=day_num, week=week7)
        day.title = title
        
        # Split logic for Capstones
        if "## Phase 1" in content:
            parts = content.split("## Phase 1")
            day.concept_content = parts[0].strip()
            day.hands_on_content = "## Phase 1" + parts[1].strip()
        elif "## 5. Hands-on Lab" in content:
             parts = content.split("## 5. Hands-on Lab")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 5. Hands-on Lab" + parts[1].strip()
        else:
             day.concept_content = content
             day.hands_on_content = "## Hands-On\n\nFollow the instructions in the concept section."
        
        day.save()
        print(f"Updated Day {day_num}: {day.title}")

if __name__ == "__main__":
    populate_capstones()
