import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import QuizQuestion

print("=== Checking for whitespace in empty options ===\n")
for q in QuizQuestion.objects.filter(day__number=1):
    print(f"\nQ: {q.question_text[:60]}...")
    for i, opt in enumerate([q.option_1, q.option_2, q.option_3, q.option_4], 1):
        if opt == '':
            print(f"  Opt{i}: (empty string)")
        elif opt is None:
            print(f"  Opt{i}: (NULL)")
        elif opt and not opt.strip():
            print(f"  Opt{i}: (whitespace only: {repr(opt)})")
        elif opt:
            print(f"  Opt{i}: '{opt[:40]}'")
