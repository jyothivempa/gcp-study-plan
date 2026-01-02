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
    """Extract quiz questions from markdown content using regex
    
    Searches both regular content and HTML comments (<!-- -->)
    """
    # First, extract content from HTML comments
    comment_pattern = r'<!--(.*?)-->'
    comment_matches = re.findall(comment_pattern, content, re.DOTALL)
    all_content = content + '\n'.join(comment_matches)
    
    quizzes = []
    matches = re.finditer(QUIZ_PATTERN, all_content, re.DOTALL)
    
    for match in matches:
        question_num = match.group(1)
        question_text = match.group(2).strip()
        options_block = match.group(3).strip()
        
        # Parse options and answer
        options_lines = [line.strip() for line in options_block.split('\n') if line.strip()]
        options = []
        correct_index = None
        
        for line in options_lines:
            if line.startswith('> **Answer:'):
                # Extract correct answer letter
                answer_match = re.search(r'\*\*Answer:\s*(\w)', line)
                if answer_match:
                    answer_letter = answer_match.group(1)
                    correct_index = ord(answer_letter.upper()) - ord('A') + 1
            elif re.match(r'^[A-D]\.', line):
                options.append(line)
        
        if len(options) >= 2 and correct_index:
            quizzes.append({
                "text": question_text,
                "type": "mcq",
                "options": options,
                "correct": correct_index
            })
    
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
    
    # Extract quizzes from markdown
    quizzes = extract_quizzes_from_markdown(content)
    
    if dry_run:
        print(f"  📄 Day {day_num}: {day_config['title']}")
        print(f"     File: {day_config['file']}")
        print(f"     Quizzes found: {len(quizzes)}")
        return True
    
    # Get or create course
    course, _ = Course.objects.get_or_create(
        slug='gcp',
        defaults={'name': 'GCP Associate Cloud Engineer'}
    )
    
    # Get or create week
    week_num = day_config['week']
    week, _ = Week.objects.get_or_create(
        number=week_num,
        course=course,
        defaults={'title': f'Week {week_num}'}
    )
    
    # Update day
    day, created = Day.objects.update_or_create(
        number=day_num,
        defaults={
            'title': day_config['title'],
            'outcome': day_config['outcome'],
            'content_file': day_config['file'],
            'week': week
        }
    )
    
    # Clear existing quizzes for this day
    QuizQuestion.objects.filter(day=day).delete()
    
    # Add new quizzes
    for quiz_data in quizzes:
        QuizQuestion.objects.create(
            day=day,
            question_text=quiz_data['text'],
            question_type=quiz_data['type'],
            options=quiz_data['options'],
            correct_answer=quiz_data['correct']
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
    total_quizzes = 0
    
    for day_num in sorted(days_to_update.keys()):
        day_config = days_to_update[day_num]
        if update_day(day_num, day_config, content_base_path, args.dry_run):
            success_count += 1
    
    print(f"\n{'✅' if not args.dry_run else '📋'} Complete: {success_count}/{len(days_to_update)} days processed")
    
    if args.dry_run:
        print("\n💡 Run without --dry-run to apply changes to the database")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
