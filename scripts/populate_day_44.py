import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

def populate_day_44():
    day_num = 44
    filename = "section_44_exam_strategy.md"
    
    path = os.path.join("curriculum", "content", filename)
    if not os.path.exists(path):
        print(f"Error: {filename} not found.")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract Title
    lines = content.split('\n')
    title = lines[0].replace("#", "").strip()
    if ":" in title:
        title = title.split(":", 1)[1].strip()

    day, created = Day.objects.get_or_create(number=day_num)
    day.title = title
    day.concept_content = content
    day.week_id = 6 # Final Week
    day.description = "Strategies to pass the ACE Exam."
    day.save()
    print(f"Successfully populated Day {day_num}: {day.title.encode('ascii', 'ignore').decode('ascii')}")

if __name__ == "__main__":
    populate_day_44()
