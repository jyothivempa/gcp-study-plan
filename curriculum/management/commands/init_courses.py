from django.core.management.base import BaseCommand
from curriculum.models import Course, Week, Day

class Command(BaseCommand):
    help = 'Initialize GCP and Azure courses'

    def handle(self, *args, **kwargs):
        self.stdout.write("--- Initializing Courses ---")
        
        # 1. Create or Update GCP Course
        gcp_course, _ = Course.objects.get_or_create(
            slug='gcp',
            defaults={
                'title': 'GCP Associate Cloud Engineer',
                'description': '30-Day Zero to Hero Study Plan',
                'icon_class': 'fa-brands fa-google'
            }
        )
        self.stdout.write(self.style.SUCCESS(f" Ensured Course: {gcp_course.title}"))

        # 2. Create or Update Azure Course (AZ-104)
        azure_course, created = Course.objects.update_or_create(
            slug='azure',
            defaults={
                'title': 'Azure Administrator (AZ-104)',
                'description': '45-Day Masterclass for Microsoft Certified: Azure Administrator Associate',
                'icon_class': 'fa-brands fa-microsoft'
            }
        )
        self.stdout.write(self.style.SUCCESS(f" Ensured Course: {azure_course.title}"))

        # 3. Migrate Existing Weeks to GCP (Safeguard)
        # Any week without a course is assumed to be GCP
        updated_count = Week.objects.filter(course__isnull=True).update(course=gcp_course)
        if updated_count:
            self.stdout.write(self.style.WARNING(f" Migrated {updated_count} legacy weeks to GCP"))

        # 4. Scaffold Azure Content (45 Days)
        if not azure_course.weeks.exists():
            self.stdout.write(" Scaffolding Azure Curriculum (45 Days)...")
            
            # 45 Days = 6 weeks of 7 days + 3 days (Week 7 partial)
            # Actually simpler: 7 Weeks. Week 1-6 (7 days), Week 7 (3 days)
            days_created = 0
            
            for w in range(1, 8): # Weeks 1 to 7
                week = Week.objects.create(
                    course=azure_course,
                    number=w,
                    description=f"Azure Module {w}: Fundamental Concepts" if w == 1 else f"Azure Module {w}"
                )
                
                start_day = (w - 1) * 7 + 1
                end_day = min(w * 7, 45)
                
                for d in range(start_day, end_day + 1):
                    Day.objects.create(
                        week=week,
                        number=d,
                        title=f"Azure Day {d}: Pending Topic",
                        description="Coming Soon",
                        concept_content="# Coming Soon\n\nContent for AZ-104 is under construction.",
                        hands_on_content="# Hands-On\n\nLab steps pending.",
                        outcome="Learning Objective Pending"
                    )
                    days_created += 1
            
            self.stdout.write(self.style.SUCCESS(f" Created {days_created} Azure days across 7 weeks."))
        else:
            self.stdout.write(" Azure content already exists. Skipping scaffold.")
