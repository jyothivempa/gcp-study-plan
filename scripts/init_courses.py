from curriculum.models import Course, Week, Day

print("--- Initializing Courses ---")

# 1. Create Courses
gcp_course, created = Course.objects.get_or_create(
    slug='gcp',
    defaults={
        'title': 'GCP Associate Cloud Engineer',
        'description': 'Master GCP in 45 Days (From Zero to Hero)',
        'icon_class': 'fa-brands fa-google'
    }
)
if created:
    print("Created GCP Course")
else:
    print("GCP Course exists")

# Azure creation logic removed per user request.
print("Azure scaffolding skipped.")
