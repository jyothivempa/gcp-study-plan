import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, Week

def create_day_31():
    # Ensure Week 5 exists (Day 29-30 might be in Week 4 or 5)
    # 30 days usually means 4 weeks + 2 days.
    # Let's verify week of Day 30.
    day30 = Day.objects.filter(number=30).first()
    week_num = 5
    if day30:
        week_num = day30.week.number
        if day30.week.days.count() >= 7:
            week_num += 1
    
    week, _ = Week.objects.get_or_create(number=week_num, defaults={'description': 'Advanced Topics'})
    
    day, created = Day.objects.get_or_create(
        number=31,
        defaults={
            'week': week,
            'title': 'Bonus: Advanced Exam Scenarios',
            'description': 'A massive collection of scenario-based questions to test your architectural knowledge.',
            'outcome': 'Mastery of complex GCP scenarios.',
            'concept_content': '## 🚀 The Gauntlet\n\nYou have unlocked the hidden level! This day contains a massive question bank.\n\n### Strategy\n*   These questions are scenario-heavy.\n*   Look for keywords: "Minimize Cost", "Google-Recommended", "Fewest Steps".',
            'hands_on_content': 'Taking this massive quiz is the hands-on!',
        }
    )
    if created:
        print("created Day 31")
    else:
        print("Day 31 already exists")

if __name__ == "__main__":
    create_day_31()
