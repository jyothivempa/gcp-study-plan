import os
import django
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

# Mapping of Day Number -> Markdown Filename (Approximate based on naming convention)
DAY_MAPPING = {
    1: "section_1_cloud_foundations.md",
    2: "section_2_gcp_structure.md",
    3: "section_3_gcp_billing.md",
    4: "section_4_compute_engine.md",
    5: "section_5_storage_basics.md",
    6: "section_6_cloud_storage.md",
    7: "section_7_week_1_review.md",
    
    8: "section_8_vpc_basics.md",
    9: "section_9_subnets_ip.md",
    10: "section_10_firewall_rules.md",
    11: "section_11_load_balancing.md",
    12: "section_12_cloud_nat_routes.md",
    13: "section_13_dns_cdn.md",
    14: "section_week_2_review.md" 
}

def read_markdown(filename):
    path = os.path.join("curriculum", "content", filename)
    if not os.path.exists(path):
        print(f"Warning: {filename} not found.")
        return None, None, None
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple extraction logic (Title is usually first line # Title)
    lines = content.split('\n')
    title = lines[0].replace("#", "").strip() if lines else "Untitled"
    if ":" in title:
        title = title.split(":", 1)[1].strip() # Remove "SECTION X:" prefix if present
        
    return title, content, path

def populate_weeks():
    for day_num, filename in DAY_MAPPING.items():
        title, content, path = read_markdown(filename)
        if not content:
            continue
            
        day, created = Day.objects.get_or_create(number=day_num)
        
        # Update fields
        day.title = title
        # Split logic could be added here if files have specific "## Hands-on" markers
        # For now, we put everything in concept_content for safety, or try to split.
        
        # Try to split Concept vs Hands-on
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
        elif "## 5️⃣ GCP Console Walkthrough" in content: 
             parts = content.split("## 5️⃣ GCP Console Walkthrough")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 5️⃣ GCP Console Walkthrough" + parts[1].strip()
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
             
        # Detect Description (often line 3 or 5)
        # We'll just generate a generic one if empty
        if not day.description:
            day.description = f"Mastering {title}"
            
        # Extract Flashcards
        # Robust regex: Allows spaces around <!--, FLASHCARDS, and keys
        
        # EXTRACT QUIZZES (New Feature)
        # We parse the HTML form in the markdown to populate the QuizQuestion model
        # This ensures the DB is in sync with the Markdown content
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            questions = soup.find_all('div', class_='quiz-question')
            
            if questions:
                # WIPE existing quizzes for this day to ensure fresh sync
                QuizQuestion.objects.filter(day=day).delete()
                print(f"  > Found {len(questions)} quiz questions. Syncing...")
                
                for q_div in questions:
                    q_text = q_div.find('p').get_text(strip=True)
                    # Remove "1. ", "2. " prefix if present
                    q_text = re.sub(r'^\d+\.\s*', '', q_text)
                    
                    options = q_div.find_all('label')
                    correct_idx = 1
                    opts_text = []
                    
                    for idx, lbl in enumerate(options, 1):
                        inp = lbl.find('input')
                        opt_text = lbl.get_text(strip=True)
                        opts_text.append(opt_text)
                        if inp and inp.get('value') == 'correct':
                            correct_idx = idx
                            
                    # Feedback/Explanation
                    explanation = ""
                    feedback_div = q_div.find('div', class_='feedback')
                    if feedback_div:
                        explanation = feedback_div.get_text(strip=True)

                    QuizQuestion.objects.create(
                        day=day,
                        question_type='mcq',
                        question_text=q_text,
                        option_1=opts_text[0] if len(opts_text) > 0 else "",
                        option_2=opts_text[1] if len(opts_text) > 1 else "",
                        option_3=opts_text[2] if len(opts_text) > 2 else "",
                        option_4=opts_text[3] if len(opts_text) > 3 else "",
                        correct_option=correct_idx,
                        explanation=explanation
                    )
        except Exception as e:
            print(f"  > Error parsing quizzes for Day {day_num}: {e}")

        day.save()
        print(f"Updated Day {day_num}: {day.title}")

if __name__ == "__main__":
    populate_weeks()
