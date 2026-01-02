import os
import django
import sys
import codecs
import re

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def update_week7():
    print("🚀 Updating Week 7 Content (Days 43-45)...")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "curriculum", "content")
    
    week_map = {
        43: {"file": "section_43_mock_exam_1.md", "outcome": "Mock Exam 1: Assess Knowledge"},
        44: {"file": "section_44_mock_exam_2.md", "outcome": "Mock Exam 2: Advanced Scenarios"},
        45: {"file": "section_45_exam_strategy.md", "outcome": "Final Strategy & Exam Day Prep"}
    }
    
    for day_num, config in week_map.items():
        print(f"\nProcessing Day {day_num}...")
        file_path = os.path.join(base_path, config["file"])
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            full_content = f.read()

        first_line = full_content.split('\n')[0].strip()
        clean_title = re.sub(r"^(# )?(SECTION \d+: |Day \d+: |# )", "", first_line)

        # For exams, usually mostly content
        split_match = re.search(r'(## \d+.*?(Hands-On|Checklist|Mock Questions|Verification Lab))', full_content)
        
        if split_match:
            split_idx = split_match.start()
            concept_content = full_content[:split_idx].strip()
            hands_on_content = full_content[split_idx:].strip()
        else:
            concept_content = full_content
            hands_on_content = "Final Exam Preparation. No separate lab."

        try:
            day, created = Day.objects.get_or_create(number=day_num, defaults={'week_id': 7})
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.week_id = 7
            day.save()
            print(f"✅ Day {day_num} Updated: {clean_title}")

            # No auto-quizzes for Day 43/44 usually as the content IS the quiz
            # unless formatted identically. Let's try parsing anyway.
            day.quiz_questions.all().delete()
            
            # (Standard parser included just in case they have checkpoint questions)
            quiz_pattern = re.compile(r'\*\*Q(\d+)\.\s+(.*?)\*\*\n(.*?)(?=> \*\*Answer:)', re.DOTALL)
            answer_pattern = re.compile(r'> \*\*Answer: ([A-D])\.\*\*')
            
            matches = quiz_pattern.finditer(full_content)
            count = 0
            for match in matches:
                q_text = match.group(2).strip()
                options_text = match.group(3).strip()
                opts = {'A': '', 'B': '', 'C': '', 'D': ''}
                for line in options_text.split('\n'):
                    line = line.strip()
                    if line.startswith('*   A.'): opts['A'] = line[6:].strip()
                    elif line.startswith('*   B.'): opts['B'] = line[6:].strip()
                    elif line.startswith('*   C.'): opts['C'] = line[6:].strip()
                    elif line.startswith('*   D.'): opts['D'] = line[6:].strip()
                
                snippet_start = match.end()
                snippet = full_content[snippet_start:snippet_start+200]
                ans_match = answer_pattern.search(snippet)
                correct = ans_match.group(1) if ans_match else 'A'
                correct_idx = {'A': 1, 'B': 2, 'C': 3, 'D': 4}.get(correct, 1)

                if q_text and opts['A']:
                    QuizQuestion.objects.create(
                        day=day,
                        question_type='mcq',
                        question_text=q_text,
                        option_1=opts['A'],
                        option_2=opts['B'],
                        option_3=opts['C'],
                        option_4=opts['D'],
                        correct_option=correct_idx,
                        explanation=f"Correct Option: {correct}"
                    )
                    count += 1
            if count > 0:
                print(f"   - Added {count} quiz questions.")
                
            # Note: Real mock exams might need specific parsing if they deviate from **Q1** format.
            # But the content is loaded, so the user can read it.

        except Exception as e:
            print(f"❌ Error updating Day {day_num}: {e}")

if __name__ == "__main__":
    update_week7()
