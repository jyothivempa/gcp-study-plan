import os
import pathlib
from curriculum.models import Day, Week

def update_week1():
    print("--- Force Updating Week 1 Content (Days 1-7) ---")
    
    # Path Setup
    # Go up from scripts/ -> project_root
    base_path = pathlib.Path(__file__).resolve().parent.parent / 'curriculum' / 'content'
    
    files = [
        (1, 'section_1_cloud_foundations.md'),
        (2, 'section_2_gcp_structure.md'),
        (3, 'section_3_gcp_billing.md'),
        (4, 'section_4_compute_engine.md'),
        (5, 'section_5_storage_basics.md'),
        (6, 'section_6_cloud_storage.md'),
        (7, 'section_7_week_1_review.md'),
    ]

    for day_num, filename in files:
        file_path = base_path / filename
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Split Concept vs Quiz
            parts = content.split('## 6️⃣ Checkpoint Questions')
            if len(parts) < 2:
                parts = content.split('## Checkpoint Questions')
                
            concept = parts[0]
            quiz = parts[1] if len(parts) > 1 else "Quiz pending."

            # Update DB
            d = Day.objects.get(number=day_num)
            d.concept_content = concept
            d.interview_questions = quiz
            d.save()
            print(f"✅ Updated Day {day_num} from {filename}")
        else:
            print(f"❌ Missing file: {filename}")

if __name__ == '__main__':
    update_week1()
