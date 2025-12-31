from curriculum.models import Course, Week, Day

print("--- Initializing Courses ---")

# 1. Create Courses
gcp_course, created = Course.objects.get_or_create(
    slug='gcp',
    defaults={
        'title': 'GCP Associate Cloud Engineer',
        'description': '30-Day Zero to Hero Study Plan',
        'icon_class': 'fa-brands fa-google'
    }
)
if created:
    print("Created GCP Course")
else:
    print("GCP Course exists")

azure_course, created = Course.objects.get_or_create(
    slug='azure',
    defaults={
        'title': 'Azure Administrator (AZ-104)',
        'description': '45-Day Comprehensive Azure Course',
        'icon_class': 'fa-brands fa-microsoft'
    }
)
if created:
    print("Created Azure Course")
else:
    print("Azure Course exists")

# 2. Migrate Existing Weeks to GCP
# Assumption: All existing weeks without a course belong to GCP
weeks_updated = Week.objects.filter(course__isnull=True).update(course=gcp_course)
print(f"Migrated {weeks_updated} weeks to GCP Course")

# 3. Scaffold Azure Content
if not azure_course.weeks.exists():
    print("Scaffolding Azure Curriculum (45 Days)...")
    # Create 7 Weeks (45 days / 7 = 6.4 weeks)
    for w in range(1, 8):
        week = Week.objects.create(
            course=azure_course,
            number=w,
            description=f"Azure Week {w}"
        )
        # Create Days for this week (up to 45)
        start_day = (w - 1) * 7 + 1
        end_day = min(w * 7, 45)
        
        for d in range(start_day, end_day + 1):
            Day.objects.create(
                week=week,
                number=d,
                title=f"Azure Day {d}: Placeholder",
                description="Coming Soon",
                concept_content="# Coming Soon\n\nThis content is under construction.",
                hands_on_content="# Hands-On\n\nLab pending.",
                outcome="Understand Azure Fundamentals"
            )
    print("Azure 45-Day Scaffolding Complete")
