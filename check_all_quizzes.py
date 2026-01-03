"""
Comprehensive Quiz Quality Checker
Analyzes all quiz questions across the entire GCP curriculum.
"""
import os
import sys
import codecs
import django

# Force UTF-8 output
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import QuizQuestion, Day

print("=" * 70)
print("GCP CURRICULUM - COMPREHENSIVE QUIZ QUALITY REPORT")
print("=" * 70)

# Statistics
total_questions = 0
questions_with_issues = 0
days_without_quizzes = []
issues_by_day = {}

for day in Day.objects.all().order_by('number'):
    questions = QuizQuestion.objects.filter(day=day)
    day_issues = []
    
    if questions.count() == 0:
        days_without_quizzes.append(day.number)
        continue
    
    for q in questions:
        total_questions += 1
        options = [q.option_1, q.option_2, q.option_3, q.option_4]
        
        # Check for missing/empty options
        empty_count = sum(1 for opt in options if not opt or not opt.strip())
        valid_count = 4 - empty_count
        
        issue = None
        if empty_count > 0:
            if valid_count < 2:
                issue = f"CRITICAL: Only {valid_count} option(s)"
            elif valid_count < 4:
                issue = f"Missing: {empty_count} option(s) empty"
        
        # Check for correct answer validity
        if q.correct_option and q.correct_option > valid_count:
            issue = f"INVALID: Correct answer points to empty option {q.correct_option}"
        
        if issue:
            questions_with_issues += 1
            day_issues.append({
                'text': q.question_text[:60] + "...",
                'issue': issue,
                'options': valid_count
            })
    
    if day_issues:
        issues_by_day[day.number] = {
            'title': day.title,
            'issues': day_issues,
            'total': questions.count()
        }

# Print Report
print(f"\n[SUMMARY]")
print(f"   Total Questions: {total_questions}")
print(f"   Questions with Issues: {questions_with_issues}")
print(f"   Days without Quizzes: {len(days_without_quizzes)}")

if days_without_quizzes:
    print(f"\n[WARNING] DAYS WITHOUT QUIZZES: {days_without_quizzes}")

if issues_by_day:
    print(f"\n[DETAILS] ISSUES BY DAY:")
    print("-" * 70)
    for day_num in sorted(issues_by_day.keys()):
        data = issues_by_day[day_num]
        print(f"\nDay {day_num}: {data['title']} ({len(data['issues'])}/{data['total']} issues)")
        for issue in data['issues']:
            print(f"   * [{issue['options']} opts] {issue['issue']}")
            print(f"     Q: {issue['text']}")
else:
    print("\n[OK] No issues found! All quizzes have proper 4-option format.")

print("\n" + "=" * 70)
