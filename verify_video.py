
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()
from curriculum.models import Day

try:
    day1 = Day.objects.get(number=1)
    print(f"Day 1 Title: {day1.title}")
    print(f"Video URL: '{day1.video_url}'")
    
    if not day1.video_url:
        print("ERROR: Video URL is empty/null.")
    else:
        print("SUCCESS: Video URL is present.")

except Day.DoesNotExist:
    print("Day 1 not found.")
