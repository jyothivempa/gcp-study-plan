import os
import django
import sys
import codecs

# Force utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def update_day_2():
    print("🚀 Updating Day 2 Content (Projects & Billing)...")
    
    # Calculate base path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Calculate base path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "curriculum", "content")
    file_path = os.path.join(base_path, "section_2_gcp_projects_billing.md")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Split into Concept vs Hands-On
    # Based on the marker used in the markdown file
    split_marker = "## 🛠️ 7. Hands-On Lab"
    parts = full_content.split(split_marker)
    
    if len(parts) < 2:
        print("⚠️ Warning: Could not split content cleanly. using full content for concept.")
        concept_content = full_content
        hands_on_content = "## 🛠️ Hands-On Lab\n\n*(See Concept Tab for details)*"
    else:
        concept_content = parts[0].strip()
        hands_on_content = split_marker + parts[1]

    try:
        # Get Day 2
        day = Day.objects.get(number=2)
        
        # Update Contents
        day.concept_content = concept_content
        day.hands_on_content = hands_on_content
        day.outcome = "Manage GCP Projects & Configure Billing/Budgets"
        day.save()
        print("✅ Day 2 Text Content Updated!")
        print(f"   - Concept Length: {len(concept_content)}")
        print(f"   - Hands-On Length: {len(hands_on_content)}")

        # Update Questions
        print("🔄 Refreshing Day 2 Quizzes...")
        day.quiz_questions.all().delete()
        
        questions = [
            {
                "text": "Every GCP resource must belong to a:",
                "type": "mcq",
                "options": ["A. Folder", "B. Project", "C. Billing Account", "D. Organization"],
                "correct": 2, 
                "explanation": "Projects are the fundamental container for all resources."
            },
            {
                "text": "Can one Billing Account pay for multiple Projects?",
                "type": "mcq",
                "options": ["A. Yes", "B. No", "C. Only in Free Tier", "D. Only for Enterprise"],
                "correct": 1,
                "explanation": "Yes, a single billing account can be linked to many projects."
            },
            {
                "text": "What happens if you disable the Billing Account?",
                "type": "mcq",
                "options": ["A. Resources run for free", "B. All paid resources stop working", "C. Nothing happens", "D. Your account is deleted"],
                "correct": 2,
                "explanation": "Disabling billing stops all services that require payment."
            },
            {
                "text": "What is the best way to prevent surprise bills?",
                "type": "mcq",
                "options": ["A. Check the console every hour", "B. Set up Budgets & Alerts", "C. Only use the Free Tier", "D. Delete account daily"],
                "correct": 2,
                "explanation": "Budgets & alerts notify you when spending hits a certain threshold."
            },
            {
                "text": "True or False: The Free Tier allows unlimited usage of all services.",
                "type": "mcq",
                "options": ["A. True", "B. False", "C. True, but only for 1 year", "D. False, only for students"],
                "correct": 2,
                "explanation": "False. Free Tier has specific limits (e.g. time, storage size)."
            }
        ]

        for q_data in questions:
            QuizQuestion.objects.create(
                day=day,
                question_type=q_data["type"],
                question_text=q_data["text"],
                option_1=q_data["options"][0],
                option_2=q_data["options"][1],
                option_3=q_data["options"][2],
                option_4=q_data["options"][3],
                correct_option=q_data["correct"],
                explanation=q_data["explanation"]
            )
        
        print(f"✅ Created {len(questions)} Quiz Questions for Day 2!")

    except Day.DoesNotExist:
        print("❌ Day 2 not found in database! (Do you need to run populate_full_curriculum first?)")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_day_2()
