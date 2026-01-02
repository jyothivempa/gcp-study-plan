#!/usr/bin/env python
"""
Unified Curriculum Update Script
Replaces update_week_1.py through update_week_7.py

Usage:
    python update_curriculum.py --all              # Update all days
    python update_curriculum.py --week 1           # Update specific week
    python update_curriculum.py --day 5            # Update specific day
    python update_curriculum.py --week 5 --dry-run # Preview changes
"""
import os
import sys
import django
import codecs
import re
import yaml
import argparse
from pathlib import Path

# Force UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion, Week, Course

# Quiz extraction regex (same as legacy scripts)
QUIZ_PATTERN = r'\*\*Q(\d+)\.\s+(.*?)\*\*\n(.*?)(?=> \*\*Answer:)'


def load_config():
    """Load curriculum configuration from YAML"""
    config_path = Path(__file__).parent / "curriculum_config.yaml"
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def extract_quizzes_from_markdown(content):
    """Extract quiz questions using a state machine for robustness"""
    # Combine content from HTML comments
    comment_pattern = r'<!--(.*?)-->'
    comment_matches = re.findall(comment_pattern, content, re.DOTALL)
    all_content = content + '\n' + '\n'.join(comment_matches)
    
    lines = all_content.split('\n')
    quizzes = []
    
    current_q = None
    
    # regexes
    # matches: "### Q1. text" or "1. **text**" or "**Q1. text**" or "Q1. **text**"
    # Capture starts AFTER the Q1 part
    q_start_re = re.compile(r'^(?:#+\s*)?(?:(?:\*\*?Q\d+[\.:]\*\*?)|(?:\*\*?\d+[\.:]\*\*?)|(?:Q\d+[\.:])|(?:- Q:)|(?:\d+[\.:]))\s*(.*)', re.IGNORECASE)
    # matches: "* A. Option" or "A. Option"
    opt_re = re.compile(r'^[*-]?\s*([A-D][\.\)]\s*.*)', re.IGNORECASE)
    # matches: "> **Answer: B**" or "* B. Option ✅"
    ans_re = re.compile(r'(?:>\s*(?:\*\*)?(?:Answer|Correct|Ans)(?:\*\*)?[:\s]+(?:\*\*)?([A-D])(?:\*\*)?)|(?:([A-D])[\.\)].*?✅)', re.IGNORECASE)
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Start of a new question?
        q_match = q_start_re.match(line_clean)
        if q_match:
            # Save previous if valid
            if current_q and len(current_q['options']) >= 2 and current_q['correct']:
                if not any(q['text'].strip() == current_q['text'].strip() for q in quizzes):
                    quizzes.append(current_q)
            
            # Start new one
            q_initial_text = q_match.group(1).strip()
            current_q = {
                'text': q_initial_text,
                'type': 'mcq',
                'options': [],
                'correct': None,
                'collecting_text': True
            }
            continue
            
        if current_q:
            # Option?
            opt_match = opt_re.match(line_clean)
            if opt_match:
                current_q['collecting_text'] = False
                opt_text = opt_match.group(1).strip()
                # Remove checkmark from option text if present
                clean_opt = re.sub(r'[\s✅]+$', '', opt_text).strip().strip('*').strip()
                current_q['options'].append(clean_opt)
                
            # Answer?
            ans_match = ans_re.search(line_clean)
            if ans_match:
                current_q['collecting_text'] = False
                letter = ans_match.group(1) or ans_match.group(2)
                current_q['correct'] = ord(letter.upper()) - ord('A') + 1
            
            # If we are still collecting text and it's not an option/answer, append it to question text
            if current_q['collecting_text'] and not opt_match and not ans_match:
                # Avoid adding headers or separators to question text
                if not line_clean.startswith('#') and not line_clean.startswith('---'):
                    if current_q['text']:
                        current_q['text'] += " " + line_clean
                    else:
                        current_q['text'] = line_clean

    # Save last one
    if current_q and len(current_q['options']) >= 2 and current_q['correct']:
        if not any(q['text'].strip() == current_q['text'].strip() for q in quizzes):
            quizzes.append(current_q)
            
    # Final cleanup of question text
    for q in quizzes:
        # Strip outer stars and whitespace
        text = q['text'].strip()
        # Handle cases like **Q: text** or **text**
        text = re.sub(r'^\*+', '', text)
        text = re.sub(r'\*+$', '', text)
        q['text'] = text.strip()
        # Remove "Scenario:" prefix if it got doubled up or messy
        q['text'] = re.sub(r'^Scenario:\s*', '', q['text'], flags=re.IGNORECASE)
        q['text'] = q['text'].replace('**', '') # Double check for internal stars
            
    return quizzes


def update_day(day_num, day_config, content_base_path, dry_run=False):
    """Update a single day's content and quizzes"""
    file_path = content_base_path / day_config['file']
    
    if not file_path.exists():
        print(f"  ❌ File not found: {file_path}")
        return False
    
    # Read markdown file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into Concept and Lab parts if possible
    # For now, we'll put most in Concept
    concept_content = ""
    hands_on_content = ""
    
    if "## Hands-on" in content:
        parts = content.split("## Hands-on")
        concept_content = parts[0]
        hands_on_content = parts[1]
    else:
        concept_content = content
    
    # Extract quizzes from markdown
    quizzes = extract_quizzes_from_markdown(content)
    
    if dry_run:
        print(f"  📄 Day {day_num}: {day_config['title']}")
        print(f"     File: {day_config['file']}")
        print(f"     Quizzes found: {len(quizzes)}")
        return True
    
    # Get or create course
    # Use 'gcp' slug as defined in config or default
    course, _ = Course.objects.get_or_create(
        slug='gcp',
        defaults={'title': 'GCP Associate Cloud Engineer'}
    )
    
    # Get or create week
    week_num = day_config['week']
    week, _ = Week.objects.get_or_create(
        number=week_num,
        course=course,
        defaults={'description': f'Week {week_num} topics'}
    )
    
    # Update day
    day, created = Day.objects.update_or_create(
        number=day_num,
        defaults={
            'week': week,
            'title': day_config['title'],
            'outcome': day_config['outcome'],
            'concept_content': concept_content,
            'hands_on_content': hands_on_content,
        }
    )
    
    # Clear existing quizzes for this day
    QuizQuestion.objects.filter(day=day).delete()
    
    # Add new quizzes
    for quiz_data in quizzes:
        opts = quiz_data['options']
        QuizQuestion.objects.create(
            day=day,
            question_text=quiz_data['text'],
            question_type=quiz_data['type'],
            option_1=opts[0] if len(opts) > 0 else "",
            option_2=opts[1] if len(opts) > 1 else "",
            option_3=opts[2] if len(opts) > 2 else "",
            option_4=opts[3] if len(opts) > 3 else "",
            correct_option=quiz_data['correct']
        )
    
    action = "Created" if created else "Updated"
    print(f"  ✅ Day {day_num} {action}: {day_config['title']}")
    print(f"     - Added {len(quizzes)} quiz questions.")
    return True


def main():
    parser = argparse.ArgumentParser(description='Update GCP curriculum database')
    parser.add_argument('--all', action='store_true', help='Update all days')
    parser.add_argument('--week', type=int, help='Update specific week (1-7)')
    parser.add_argument('--day', type=int, help='Update specific day (1-45)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without updating database')
    
    args = parser.parse_args()
    
    # Load configuration
    print("📂 Loading curriculum configuration...")
    config = load_config()
    
    # Determine content base path
    script_dir = Path(__file__).parent
    content_base_path = script_dir / "curriculum" / "content"
    
    # Build days to update
    days_to_update = {}
    for day_config in config['days']:
        day_num = day_config['number']
        days_to_update[day_num] = day_config
    
    # Filter based on arguments
    if args.day:
        if args.day not in days_to_update:
            print(f"❌ Day {args.day} not found in configuration")
            return 1
        days_to_update = {args.day: days_to_update[args.day]}
        print(f"🚀 Updating Day {args.day}...")
    elif args.week:
        week_days = {num: cfg for num, cfg in days_to_update.items() if cfg['week'] == args.week}
        if not week_days:
            print(f"❌ Week {args.week} not found in configuration")
            return 1
        days_to_update = week_days
        print(f"🚀 Updating Week {args.week} (Days {min(week_days.keys())}-{max(week_days.keys())})...")
    elif args.all:
        print(f"🚀 Updating ALL days (1-{max(days_to_update.keys())})...")
    else:
        print("❌ Please specify --all, --week, or --day")
        parser.print_help()
        return 1
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No database changes will be made\n")
    
    # Update days
    success_count = 0
    active_day_numbers = set(days_to_update.keys())
    
    for day_num in sorted(days_to_update.keys()):
        day_config = days_to_update[day_num]
        if update_day(day_num, day_config, content_base_path, args.dry_run):
            success_count += 1
            
    # Cleanup orphaned days and questions (only if updating all or specified days)
    if not args.dry_run and (args.all or len(days_to_update) > 1):
        print("\n🧹 Cleaning up orphaned data...")
        # Get all days currently in the DB
        all_db_days = Day.objects.all()
        for db_day in all_db_days:
            if db_day.number not in active_day_numbers:
                print(f"  🗑️ Removing phantom Day {db_day.number}: {db_day.title}")
                db_day.delete() # This will cascade delete related QuizQuestions
    
    print(f"\n{'✅' if not args.dry_run else '📋'} Complete: {success_count}/{len(days_to_update)} days processed")
    
    if args.dry_run:
        print("\n💡 Run without --dry-run to apply changes to the database")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
