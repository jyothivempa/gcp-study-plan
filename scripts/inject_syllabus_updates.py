import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

# MAPPING
# Day 21: Containers Intro (Was Review, but Reviews can happen on weekends. Let's make 21 technical).
# Day 41: Cost Opt
# Day 42: Mock 1
# Day 43: Mock 2
# Day 45: Final Exam (Already exists?)

UPDATES = {
    21: "section_21_containers_intro.md",
    41: "section_41_cost_optimization.md",
    42: "section_42_mock_exam_1.md",
    43: "section_43_mock_exam_2.md"
}

def inject():
    for num, filename in UPDATES.items():
        path = os.path.join("curriculum", "content", filename)
        if not os.path.exists(path):
            print(f"Error: {filename} not found.")
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract Title
        lines = content.split('\n')
        title = lines[0].replace("#", "").strip()
        if ":" in title:
            title = title.split(":", 1)[1].strip()
            
        # Assign Week IDs
        week_num = 3 if num == 21 else 6
        
        # Using defaults to prevent IntegrityError on creation
        day, created = Day.objects.get_or_create(
            number=num,
            defaults={'week_id': week_num} 
        )
        
        day.title = title
        day.concept_content = content
        day.week_id = week_num # Ensure it's set on update too
        
        if num == 21:
            day.description = "Before GKE, you must understand Docker."
        else:
            day.description = "Exam Preparation Module."
            
        day.save()
        print(f"Updated Day {num}: {title.encode('ascii', 'ignore').decode('ascii')}")

if __name__ == "__main__":
    inject()
