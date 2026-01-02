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

def update_day_1():
    print("🚀 Updating Day 1 Content (Polished Version)...")
    
    file_path = r"d:\ultimateCode\gcp_study_plan\curriculum\content\section_1_cloud_foundations.md"
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Intelligent Split based on Headers
    # We want to separate the Hands-On Lab part
    
    split_marker = "## 🛠️ 6. Hands-On Lab"
    parts = full_content.split(split_marker)
    
    if len(parts) < 2:
        print("⚠️  Warning: Could not split content cleanly. Using full content for concept.")
        concept_content = full_content
        hands_on_content = "## 🛠️ Hands-On Lab\n\n*(See Concept Tab for details)*"
    else:
        concept_content = parts[0].strip()
        
        # We also want to remove the Quiz section from the text, as it's interactive now
        # But keeping it in text is fine for "Notes" or review. 
        # Actually, let's keep it clean.
        
        hands_on_part = split_marker + parts[1]
        
        # Split Hands-On from Quiz/Mistakes if needed, or just keep it all there.
        # The user wanted common mistakes in the content.
        # Let's see... Mistakes were Section 7. Quiz Section 8.
        # Let's put Mistakes in Concept or Hands-on? 
        # Usually mistakes go well with the Lab or right after concepts.
        # Let's keep the split simple:
        # Concept = Sections 1-5
        # Hands-On = Section 6 + 7 + 8 + 9 + 10
        
        hands_on_content = hands_on_part.strip()


    try:
        # Get Day 1
        day = Day.objects.get(number=1)
        
        # Update Contents
        day.concept_content = concept_content
        day.hands_on_content = hands_on_content
        day.outcome = "Analyze Cloud Models (IaaS/PaaS/SaaS) & Navigate Console"
        day.save()
        print("✅ Day 1 Text Content Updated!")
        print(f"   - Concept Length: {len(concept_content)}")
        print(f"   - Hands-On Length: {len(hands_on_content)}")

        # Update Questions (Hardcoded for safety/precision, as regex parsing markdown quizzes is flaky)
        print("🔄 Refreshing Quizzes...")
        day.quiz_questions.all().delete()
        
        questions = [
            {
                "text": "Cloud computing mainly helps with which problem?",
                "type": "mcq",
                "options": ["A. Buying more hardware", "B. Scalability & cost efficiency", "C. Manual maintenance", "D. Increasing CapEx"],
                "correct": 2, 
                "explanation": "Cloud computing offers instant scalability and shifts cost from CapEx to OpEx."
            },
            {
                "text": "Which model requires the LEAST amount of management from you?",
                "type": "mcq",
                "options": ["A. IaaS", "B. PaaS", "C. SaaS", "D. On-Premise"],
                "correct": 3,
                "explanation": "SaaS (Software as a Service) is fully managed by the provider."
            },
            {
                "text": "Compute Engine (Virtual Machines) belongs to which model?",
                "type": "mcq",
                "options": ["A. IaaS", "B. PaaS", "C. SaaS", "D. CaaS"],
                "correct": 1,
                "explanation": "IaaS gives you raw infrastructure like VMs."
            },
            {
                "text": "Who manages the physical hardware in the cloud?",
                "type": "mcq",
                "options": ["A. You", "B. The Cloud Provider (e.g., Google)", "C. The ISP", "D. No one"],
                "correct": 2,
                "explanation": "The provider handles all physical data centers and hardware."
            },
            {
                "text": "True or False: Cloud implies 'Free Usage' for everyone.",
                "type": "mcq",
                "options": ["A. True", "B. False", "C. Maybe", "D. Only for students"],
                "correct": 2,
                "explanation": "Cloud is pay-as-you-go. Free tiers exist but have limits."
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
        
        print(f"✅ Created {len(questions)} Quiz Questions!")

    except Day.DoesNotExist:
        print("❌ Day 1 not found via number=1")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_day_1()
