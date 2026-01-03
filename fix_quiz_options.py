"""
Batch Quiz Fixer
Fixes all True/False and 3-option questions by adding proper distractor options.
"""
import os
import sys
import codecs
import django

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import QuizQuestion

print("=" * 70)
print("BATCH QUIZ FIXER - Adding Missing Options")
print("=" * 70)

fixed_count = 0

# Fix all questions with missing options
for q in QuizQuestion.objects.all():
    options = [q.option_1, q.option_2, q.option_3, q.option_4]
    valid_opts = [opt for opt in options if opt and opt.strip()]
    empty_count = 4 - len(valid_opts)
    
    if empty_count == 0:
        continue  # Already has 4 options
    
    # Determine fix strategy
    question_lower = q.question_text.lower()
    
    # True/False questions (2 options)
    if empty_count == 2 and len(valid_opts) == 2:
        if 'true' in valid_opts[0].lower() or 'false' in valid_opts[0].lower():
            # Convert True/False to MCQ
            q.option_3 = "It depends on the use case"
            q.option_4 = "Not applicable to GCP"
        else:
            # Generic 2-option question
            q.option_3 = "Both of the above"
            q.option_4 = "None of the above"
        fixed_count += 1
        q.save()
        print(f"[FIXED 2->4] Day {q.day.number}: {q.question_text[:50]}...")
    
    # 3-option questions (1 missing)
    elif empty_count == 1 and len(valid_opts) == 3:
        q.option_4 = "None of the above"
        fixed_count += 1
        q.save()
        print(f"[FIXED 3->4] Day {q.day.number}: {q.question_text[:50]}...")

print("\n" + "=" * 70)
print(f"COMPLETE: Fixed {fixed_count} questions")
print("=" * 70)
