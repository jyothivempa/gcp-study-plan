import os
import sys
import django
from django.test import Client

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
from django.conf import settings
if not settings.configured:
    django.setup()
settings.ALLOWED_HOSTS += ['testserver', 'localhost', '127.0.0.1']

from curriculum.models import Day

def run_tests():
    c = Client()
    errors = []
    success_count = 0

    print("Starting Site Integrity Check...")

    # 1. Static / Public Pages
    urls = [
        '/',
        '/auth/login/',
        '/auth/register/',  # Assuming users app URLs are under auth/
        '/roadmap/',
        '/curriculum/',
        '/curriculum/search/?q=cloud',
    ]

    for url in urls:
        print(f"Checking {url:<30} ...", end=" ")
        try:
            resp = c.get(url)
            if resp.status_code == 200:
                print("[OK]")
                success_count += 1
            elif resp.status_code == 302:
                print(f"[REDIRECT] -> {resp.url}")
                success_count += 1
            else:
                print(f"[FAILED] ({resp.status_code})")
                errors.append(f"{url} returned {resp.status_code}")
        except Exception as e:
            print(f"[ERROR]: {e}")
            errors.append(f"{url} raised {e}")

    # 2. Lesson Pages
    print("\nChecking Lesson Pages...")
    days = Day.objects.all().order_by('number')
    if not days.exists():
        print("[WARNING] No Days found in database!")
        errors.append("Database is empty (no Day objects).")

    for day in days:
        url = f"/curriculum/day/{day.number}/"
        print(f"Checking Day {day.number:<2} ...", end=" ")
        try:
            resp = c.get(url)
            if resp.status_code == 200:
                print("[OK]", end=" ")
                # Content Checks
                content = resp.content.decode('utf-8')
                checks = []
                if "Flashcards" in content:
                     checks.append("Flashcards")
                if "Quiz" in content or "Checkpoint" in content:
                     checks.append("Quiz")
                
                if checks:
                    print(f"[{', '.join(checks)}]", end="")
                print("")
                success_count += 1
            elif resp.status_code == 302:
                print(f"[REDIRECT] (Auth Required)", end="\n")
                success_count += 1
            else:
                print(f"[FAILED] ({resp.status_code})")
                errors.append(f"Day {day.number} ({url}) returned {resp.status_code}")
        except Exception as e:
            print(f"[ERROR]: {e}")
            errors.append(f"Day {day.number} raised {e}")

    # Summary
    print("-" * 50)
    print(f"Testing Complete. {success_count} pages passed.")
    if errors:
        print(f"\n{len(errors)} Errors Found:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("\nAll systems nominal.")

if __name__ == "__main__":
    run_tests()
