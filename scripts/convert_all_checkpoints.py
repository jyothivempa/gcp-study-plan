import sys
import os
import django
import re

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def parse_markdown_checkpoints(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for "## ... Checkpoint Questions" OR "## ... Exam"
    # Added ".*?" after keywords to allow for subtitles like "(Comprehensive)" or emoji
    match = re.search(r'##\s*.*?(?:Checkpoint Questions|Final Exam|Mock Exam|Review).*?\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    
    if not match:
        # print(f"    > Debug: No 'Checkpoint/Exam' section found in {os.path.basename(file_path)}")
        return []

    section_content = match.group(1)

    questions = []

    # Text-Based Question Pattern (Legacy support)
    text_pattern = re.compile(r'\d+\.\s+\*\*(.*?)\*\*\s*\n\s*\*\s+\*Answer:\s*(.*?)\*', re.DOTALL)
    
    # MCQ Pattern (Robust)
    # Fixed greedy tail: content after answer stops at next question "**Q" or End of String "\Z"
    mcq_pattern = re.compile(
        r'\*\*Q\d+\.\s+(.*?)\*\*\s*\n'         # **Q1. Question?**
        r'\s*\*\s+A\.\s+(.*?)\n'               # * A. Option
        r'\s*\*\s+B\.\s+(.*?)\n'               # * B. Option
        r'(?:\s*\*\s+C\.\s+(.*?)\n)?'          # Optional C
        r'(?:\s*\*\s+D\.\s+(.*?)\n)?'          # Optional D
        r'.*?Answer:\s*([A-D])\.\*\*\s*(.*?)(?=\n\*\*Q|\Z)',  # Answer + Explanation
        re.DOTALL
    )
    
    # Parse MCQs first (New format)
    for m_match in mcq_pattern.finditer(section_content):
        questions.append({
            'type': 'mcq',
            'question': m_match.group(1).strip(),
            'options': [m_match.group(2), m_match.group(3), m_match.group(4), m_match.group(5)],
            'correct': m_match.group(6),
            'explanation': m_match.group(7).strip()
        })

    # If no MCQs found, try parsing Text questions (Old format)
    if not questions:
        for q_match in text_pattern.finditer(section_content):
            questions.append({
                'type': 'text',
                'question': q_match.group(1).strip(),
                'answer': q_match.group(2).strip()
            })

    return questions

def populate_all_quizzes():
    base_dir = r"d:\ultimateCode\gcp_study_plan\curriculum\content"
    
    # Map letters to indices
    letter_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

    files = sorted([f for f in os.listdir(base_dir) if f.endswith('.md')])
    
    total_added = 0
    
    for filename in files:
        # Extract Day Number from different naming conventions
        # section_1_... -> Day 1
        # section_2_... -> Day 2
        
        # Try finding the day number from filename first
        day_match = re.search(r'section_(\d+)_', filename)
        if not day_match:
            continue
            
        day_num = int(day_match.group(1))
        
        try:
            day = Day.objects.get(number=day_num)
        except Day.DoesNotExist:
            print(f"⚠️ Day {day_num} not found in DB. Skipping {filename}")
            continue

        file_path = os.path.join(base_dir, filename)
        questions = parse_markdown_checkpoints(file_path)
        
        if not questions:
            print(f"Info: No checkpoints found for Day {day_num}")
            continue

        print(f"Processing Day {day_num} ({len(questions)} questions)...")
        
        # Clear existing to avoid duplicates
        QuizQuestion.objects.filter(day=day).delete()
        
        for q in questions:
            if q['type'] == 'text':
                QuizQuestion.objects.create(
                    day=day,
                    question_type='text',
                    question_text=q['question'],
                    explanation=q['answer']
                )
            elif q['type'] == 'mcq':
                opts = q['options']
                QuizQuestion.objects.create(
                    day=day,
                    question_type='mcq',
                    question_text=q['question'],
                    option_1=opts[0],
                    option_2=opts[1],
                    option_3=opts[2] if opts[2] else None,
                    option_4=opts[3] if opts[3] else None,
                    correct_option=letter_map.get(q['correct'], 1),
                    explanation=q['explanation']
                )
            total_added += 1

    print(f"\nDONE! Added {total_added} questions across all days.")

if __name__ == '__main__':
    populate_all_quizzes()
