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

def update_week5():
    print("🚀 Updating Week 5 Content (Days 29-35)...")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "curriculum", "content")
    
    # Configuration for Week 5
    week_map = {
        29: {"file": "section_29_architect_case_studies.md", "outcome": "Design Scalable & Reliable Architectures"},
        30: {"file": "section_30_bigquery.md", "outcome": "Design Data Warehousing Solutions with BigQuery"},
        31: {"file": "section_31_pubsub.md", "outcome": "Implement Decoupled Event-Driven Systems"},
        32: {"file": "section_32_dataflow_dataproc.md", "outcome": "Choose Data Pipelines (Beam vs Spark)"},
        33: {"file": "section_33_hybrid_connectivity.md", "outcome": "Connect On-Prem to Cloud (VPN/Interconnect)"},
        34: {"file": "section_34_db_migration.md", "outcome": "Migrate Databases to Cloud SQL/AlloyDB"},
        35: {"file": "section_35_week_5_review.md", "outcome": "Week 5 Review: Architecture & Data"}
    }
    
    for day_num, config in week_map.items():
        print(f"\nProcessing Day {day_num}...")
        file_path = os.path.join(base_path, config["file"])
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            full_content = f.read()

        # Extract Title
        first_line = full_content.split('\n')[0].strip()
        clean_title = re.sub(r"^(# )?(SECTION \d+: |Day \d+: |# )", "", first_line)

        # Split Concept vs Hands-On/Checklist
        # Pattern: find "## \d+.*?Hands-On" or "## \d+.*?Checklist" or "## \d+.*?Mock Exam"
        split_match = re.search(r'(## \d+.*?(Hands-On|Checklist|Mock Questions|Mock Exam|Examination))', full_content)
        
        if split_match:
            split_idx = split_match.start()
            concept_content = full_content[:split_idx].strip()
            # Everything after is hands-on/practice
            hands_on_content = full_content[split_idx:].strip()
        else:
            concept_content = full_content
            hands_on_content = "Check content for details."

        try:
            day, created = Day.objects.get_or_create(number=day_num, defaults={'week_id': 5})
            day.title = clean_title
            day.concept_content = concept_content
            day.hands_on_content = hands_on_content
            day.outcome = config["outcome"]
            day.week_id = 5 # Ensure Week ID is set
            day.save()
            print(f"✅ Day {day_num} Updated: {clean_title}")

            # Parse Quizzes (Regex Parser)
            day.quiz_questions.all().delete()
            
            # Regex to find questions like "**Q1. Question text**"
            # And options like "* A. Option"
            # And answer like "> **Answer: B.**"
            
            # We iterate through the file to find chunks
            quiz_pattern = re.compile(r'\*\*Q(\d+)\.\s+(.*?)\*\*\n(.*?)(?=> \*\*Answer:)', re.DOTALL)
            answer_pattern = re.compile(r'> \*\*Answer: ([A-D])\.\*\*')
            
            matches = quiz_pattern.finditer(full_content)
            count = 0
            for match in matches:
                q_text = match.group(2).strip()
                options_text = match.group(3).strip()
                
                # Parse options
                opts = {'A': '', 'B': '', 'C': '', 'D': ''}
                for line in options_text.split('\n'):
                    line = line.strip()
                    if line.startswith('*   A.'): opts['A'] = line[6:].strip()
                    elif line.startswith('*   B.'): opts['B'] = line[6:].strip()
                    elif line.startswith('*   C.'): opts['C'] = line[6:].strip()
                    elif line.startswith('*   D.'): opts['D'] = line[6:].strip()
                
                # Find answer in the snippet following the match
                snippet_start = match.end()
                snippet = full_content[snippet_start:snippet_start+200]
                ans_match = answer_pattern.search(snippet)
                correct = ans_match.group(1) if ans_match else 'A' # Default fallback
                
                # Map letter to index (1-4)
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
    update_week5()
