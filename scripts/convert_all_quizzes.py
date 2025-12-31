import os
import django
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def convert_quizzes():
    # Fetch all days
    days = Day.objects.all().order_by('number')
    
    mcq_regex = re.compile(
        r"\*\*Q(\d+)\.\s+(.*?)\*\*"  # Capture Q Number and Text
        r"(.*?)"                      # Capture content between Question and Answer
        r">\s+\*\*Correct Answer:\s+([A-D])\.\*\*", # Capture Correct Answer (A, B, C, D)
        re.DOTALL
    )

    option_regex = re.compile(r"\*\s+([A-D])\.\s+(.*)")

    for day in days:
        content = day.concept_content + "\n" + day.hands_on_content
        
        # Check if this day actually has MCQs formatted
        matches = mcq_regex.findall(content)
        
        if not matches:
            # print(f"Day {day.number}: No MCQ pattern found. Skipping.")
            continue
            
        print(f"Day {day.number}: Found {len(matches)} MCQs. Processing...")
        
        # Clear existing
        QuizQuestion.objects.filter(day=day).delete()
        
        count = 0
        for match in matches:
            q_num, q_text, middle_content, correct_letter = match
            
            # Extract Options from middle content
            lines = middle_content.strip().split('\n')
            
            options_map = {}
            for line in lines:
                opt_match = option_regex.search(line.strip())
                if opt_match:
                    letter = opt_match.group(1)
                    text = opt_match.group(2)
                    options_map[letter] = text
            
            # If we don't have at least 2 options, skipping might be safer
            if len(options_map) < 2:
                print(f"  Warning: Question {q_num} has < 2 options. Skipping.")
                continue

            # Map Answer Letter to Integer (1=A, 2=B, etc)
            ans_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
            correct_int = ans_map.get(correct_letter, 1)

            # Create
            try:
                QuizQuestion.objects.create(
                    day=day,
                    question_text=q_text.strip(),
                    option_1=options_map.get('A', "Option A"),
                    option_2=options_map.get('B', "Option B"),
                    option_3=options_map.get('C', None),
                    option_4=options_map.get('D', None),
                    correct_option=correct_int
                )
                count += 1
            except Exception as e:
                print(f"  Error creating Q{q_num}: {e}")
        
        print(f"Day {day.number}: Added {count} interactive questions.")

if __name__ == "__main__":
    convert_quizzes()
