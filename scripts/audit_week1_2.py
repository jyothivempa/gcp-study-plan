import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

def check_structure():
    print(f"{'Day':<5} | {'DB Title':<40} | {'Content Length':<10} | {'Start of Content'}")
    print("-" * 80)
    for i in range(1, 15):
        try:
            d = Day.objects.get(number=i)
            # Get first line of content
            first_line = d.concept_content.split('\n')[0] if d.concept_content else "EMPTY"
            print(f"{d.number:<5} | {d.title[:38]:<40} | {len(d.concept_content):<10} | {first_line[:20]}...")
        except Day.DoesNotExist:
            print(f"{i:<5} | MISSING")

if __name__ == "__main__":
    check_structure()
