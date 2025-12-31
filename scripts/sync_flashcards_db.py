
import os
import sys
import re
import json
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, Course

CONTENT_DIR = r"d:\ultimateCode\gcp_study_plan\curriculum\content"

def sync_flashcards():
    print("Syncing Flashcards from Markdown to Database...")
    
    # Get GCP Course
    try:
        gcp_course = Course.objects.get(slug='gcp')
    except Course.DoesNotExist:
        print("GCP Course not found!")
        return

    updated_count = 0
    
    for filename in os.listdir(CONTENT_DIR):
        if not filename.endswith(".md") or not filename.startswith("section_"):
            continue
            
        # Parse Day Number from filename: section_5_storage_basics.md -> 5
        match = re.match(r"section_(\d+)_", filename)
        if not match:
            continue
            
        day_num = int(match.group(1))
        
        filepath = os.path.join(CONTENT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract Flashcard Block
        # Looks like: 
        # <!-- FLASHCARDS
        # [ ... json ... ]
        # -->
        
        fc_match = re.search(r"<!-- FLASHCARDS\s*(\[.*?\])\s*-->", content, re.DOTALL)
        if fc_match:
            json_str = fc_match.group(1)
            try:
                raw_cards = json.loads(json_str)
                flashcards = []
                
                # Transform keys to standard front/back
                for card in raw_cards:
                    new_card = {}
                    if 'term' in card:
                        new_card['front'] = card['term']
                        new_card['back'] = card['def']
                    else:
                        new_card['front'] = card.get('front', '')
                        new_card['back'] = card.get('back', '')
                    flashcards.append(new_card)
                
                # Find the Day
                # We assume GCP course for these legacy files
                # We need to filter by course to avoid ambiguity if Azure days share numbers
                days = Day.objects.filter(week__course=gcp_course, number=day_num)
                
                if days.exists():
                    day = days.first()
                    day.flashcards = flashcards
                    day.save()
                    print(f"Updated Day {day_num} ({filename}): {len(flashcards)} cards")
                    updated_count += 1
                else:
                    print(f"Day {day_num} not found in DB (File: {filename})")
                    
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON in {filename}: {e}")
        else:
            # print(f"No flashcards in {filename}")
            pass
            
    print(f"\nSync Complete. Updated {updated_count} Days.")

if __name__ == "__main__":
    sync_flashcards()
