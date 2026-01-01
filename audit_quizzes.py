import os
import django
import sys

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def audit_quizzes():
    print("--- Quiz Audit (Weeks 1 & 2) ---")
    days = Day.objects.filter(number__lte=14).order_by('number')
    missing_count = 0
    
    for day in days:
        q_count = QuizQuestion.objects.filter(day=day).count()
        status = "[OK]" if q_count > 0 else "[MISSING]"
        print(f"Day {day.number}: {status} - {q_count} Questions ({day.title})")
        
        if q_count == 0:
            missing_count += 1

    print(f"\nTotal Days with Missing Quizzes: {missing_count}")

if __name__ == "__main__":
    audit_quizzes()
