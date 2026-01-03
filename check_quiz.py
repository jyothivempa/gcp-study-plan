import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import QuizQuestion

q = QuizQuestion.objects.filter(day__number=1).first()
print(f"Q: {q.question_text}")
print(f"Opt1: [{repr(q.option_1)}]")
print(f"Opt2: [{repr(q.option_2)}]")
print(f"Opt3: [{repr(q.option_3)}]")
print(f"Opt4: [{repr(q.option_4)}]")
print(f"\nCorrect: {q.correct_option}")

# Check all Day 1 questions
print("\n=== All Day 1 Questions ===")
for q in QuizQuestion.objects.filter(day__number=1):
    opts = [q.option_1, q.option_2, q.option_3, q.option_4]
    non_empty = [o for o in opts if o]
    print(f"\n{q.question_text[:60]}...")
    print(f"  Options: {len(non_empty)} non-empty out of 4")
    for i, opt in enumerate(opts, 1):
        if opt:
            print(f"    {i}: {opt[:50]}")
        else:
            print(f"    {i}: <EMPTY>")
