import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, Week, QuizQuestion

def setup_bonus_days():
    week_num = 5
    week, _ = Week.objects.get_or_create(number=week_num, defaults={'description': 'Advanced Topics'})
    
    # Define the 7 days
    days_config = [
        (31, "Bonus Exam 1: Architecture & Design"),
        (32, "Bonus Exam 2: Compute & Networking"),
        (33, "Bonus Exam 3: Storage & Database"),
        (34, "Bonus Exam 4: Security & Identity"),
        (35, "Bonus Exam 5: Operations & Monitoring"),
        (36, "Bonus Exam 6: Advanced Scenarios"),
        (37, "Bonus Exam 7: Final Sprint"),
    ]

    for day_num, title in days_config:
        day, created = Day.objects.get_or_create(
            number=day_num,
            defaults={
                'week': week,
                'title': title,
                'description': f'Part {day_num - 30} of the Advanced Mock Exam series.',
                'outcome': 'Validation of specific knowledge domains.',
                'concept_content': f'## 🎯 {title}\n\nWelcome to Part {day_num - 30} of the challenge. Focus on the questions below.',
                'hands_on_content': 'Complete the interactive quiz to proceed.',
            }
        )
        
        # Update title if it already existed (e.g. Day 31)
        if not created:
            day.title = title
            day.week = week # Ensure it is in week 5
            day.save()
            print(f"Updated Day {day.number}")
        else:
            print(f"Created Day {day.number}")

        # CLEAR Questions for a clean refill
        count = day.quiz_questions.count()
        if count > 0:
            print(f"Clearing {count} existing questions from Day {day.number}...")
            day.quiz_questions.all().delete()

if __name__ == "__main__":
    setup_bonus_days()
