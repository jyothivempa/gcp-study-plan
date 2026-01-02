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

def update_week6():
    print("🚀 Updating Week 6 Content (Days 36-42)...")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "curriculum", "content")
    
    week_map = {
        36: {"file": "section_36_sre_ops.md", "outcome": "Apply SRE Principles & Error Budgets"},
        37: {"file": "section_37_finops.md", "outcome": "Optimize Costs & Manage Budgets"},
        38: {"file": "section_38_network_capstone.md", "outcome": "Capstone: Troubleshoot VPC Connectivity"},
        39: {"file": "section_39_security_capstone.md", "outcome": "Capstone: Audit IAM & Security Vulnerabilities"},
        40: {"file": "section_40_devops_capstone.md", "outcome": "Capstone: Build & Secure a CI/CD Pipeline"},
        41: {"file": "section_41_data_capstone.md", "outcome": "Capstone: Build a Big Data Pipeline"},
        42: {"file": "section_42_week_6_review.md", "outcome": "Week 6 Review: Reliability & Capstones"}
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

        split_match = re.search(r'(## \d+.*?(Hands-On|Checklist|Mock Questions|The Objectives))', full_content)
        
        if split_match:
            split_idx = split_match.start()
            concept_content = full_content[:split_idx].strip()
            hands_on_content = full_content[split_idx:].strip()
        else:
            concept_content = full_content
            hands_on_content = "Capstone Project Instructions included above."

        try:
            day, created = Day.objects.get_or_create(number=day_num, defaults={'week_id': 6})
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.week_id = 6
            day.save()
            print(f"✅ Day {day_num} Updated: {clean_title}")

            day.quiz_questions.all().delete()
            
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

        except Exception as e:
            print(f"❌ Error updating Day {day_num}: {e}")

if __name__ == "__main__":
    update_week6()
