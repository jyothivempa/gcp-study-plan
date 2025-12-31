import os
import django
import sys

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from django.core.management import call_command
from curriculum.models import Day, Week, Course

def run_script(script_name):
    print(f"\n==========================================")
    print(f"🚀 Running: {script_name}")
    print(f"==========================================")
    try:
        # Use exec to run the script in the current context/process
        with open(script_name, 'r', encoding='utf-8') as file:
            exec(file.read(), globals())
        print(f"✅ {script_name} completed successfully.")
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")

def main():
    print("🌍 Starting Full Curriculum Population...")

    # 1. Base Content (Days 1-30 structure)
    print("\n[Phase 1] Creating Base Days...")
    # We will assume populate_days.py handles basic structure if it exists
    # If not, we can import specific logic. 
    # Let's rely on the known scripts present in the file list.
    
    if os.path.exists('populate_days.py'):
        run_script('populate_days.py')
    
    if os.path.exists('create_missing_content.py'):
        run_script('create_missing_content.py')

    # 2. Flashcards
    print("\n[Phase 2] Syncing Flashcards...")
    if os.path.exists('populate_all_flashcards.py'):
        run_script('populate_all_flashcards.py')
    
    # We also need to sync the flashcards from markdown to DB
    if os.path.exists('scripts/sync_flashcards_db.py'):
        run_script('scripts/sync_flashcards_db.py')

    # 3. Capstones & Advanced Content
    print("\n[Phase 3] Populating Capstones & Advanced Days...")
    capstone_scripts = [
        'populate_day_31.py',
        'populate_day_32.py',
        'populate_day_33.py',
        'populate_day_34.py',
        'populate_day_35.py',
        'populate_day_36.py',
        'populate_day_37.py'
    ]
    
    for script in capstone_scripts:
        if os.path.exists(script):
            run_script(script)

    print("\n🎉 Full Curriculum Population Complete!")

if __name__ == '__main__':
    main()
