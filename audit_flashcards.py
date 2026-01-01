import os
import django
import sys
import json

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

def check_db_flashcards():
    print("--- Flashcard Database Audit ---")
    days = Day.objects.filter(number__lte=7).order_by('number')
    
    for day in days:
        fc = day.flashcards
        status = "✅ Found" if fc else "❌ Missing"
        count = len(fc) if fc else 0
        print(f"Day {day.number}: {status} ({count} cards)")
        if fc:
            print(f"  Sample: {fc[0].get('term', 'Unknown')} - {fc[0].get('def', 'Unknown')[:30]}...")

if __name__ == "__main__":
    check_db_flashcards()
