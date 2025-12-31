import os
import django
import sys
import textwrap

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

# Mapping: Day Number -> Markdown Filename
# Day 22: GKE (Already done via update_day22_gke.py, skipping)
# Day 25: Cloud Run (Already done via update_day25_cloudrun.py, skipping)

DAY_MAPPING = {
    23: "section_16_app_engine.md",
    24: "section_23_cloud_spanner_bigtable.md",
    26: "section_24_bigquery_data_warehousing.md",
    27: "section_25_pub_sub_data_pipelines.md",
    28: "section_20_backup_dr.md" 
}
# Note: Day 29 (Architecture) & 30 (Final Review) can be done separately or added if files exist.
# section_21_final_architecture.md exists, let's map it to Day 29.
DAY_MAPPING[29] = "section_21_final_architecture.md"

def read_markdown(filename):
    path = os.path.join("curriculum", "content", filename)
    if not os.path.exists(path):
        print(f"Warning: {filename} not found.")
        return None, None
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split('\n')
    title = lines[0].replace("#", "").strip() if lines else "Untitled"
    if ":" in title:
        title = title.split(":", 1)[1].strip()
        
    return title, content

def populate_week4():
    for day_num, filename in DAY_MAPPING.items():
        title, content = read_markdown(filename)
        if not content:
            continue
            
        day, created = Day.objects.get_or_create(number=day_num)
        
        day.title = title
        day.week_id = 4 # Ensure Week 4
        
        # Split logic
        if "## 6️⃣ Hands-On Lab" in content:
            parts = content.split("## 6️⃣ Hands-On Lab")
            day.concept_content = parts[0].strip()
            day.hands_on_content = "## 6️⃣ Hands-On Lab" + parts[1].strip()
        elif "## 5️⃣ Hands-On Lab" in content:
            parts = content.split("## 5️⃣ Hands-On Lab")
            day.concept_content = parts[0].strip()
            day.hands_on_content = "## 5️⃣ Hands-On Lab" + parts[1].strip()
        elif "## 4️⃣ Hands-On Lab" in content: 
             parts = content.split("## 4️⃣ Hands-On Lab")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 4️⃣ Hands-On Lab" + parts[1].strip()
        elif "## 5️⃣ Console Walkthrough" in content: 
             parts = content.split("## 5️⃣ Console Walkthrough")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 5️⃣ Console Walkthrough" + parts[1].strip()
        elif "## 6️⃣ Console Walkthrough" in content: 
             parts = content.split("## 6️⃣ Console Walkthrough")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 6️⃣ Console Walkthrough" + parts[1].strip()
        elif "## 6️⃣ Hands-On" in content:
             parts = content.split("## 6️⃣ Hands-On") 
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 6️⃣ Hands-On" + parts[1].strip()
        elif "## 5. Hands-on Lab" in content:
             parts = content.split("## 5. Hands-on Lab")
             day.concept_content = parts[0].strip()
             day.hands_on_content = "## 5. Hands-on Lab" + parts[1].strip()
        else:
             day.concept_content = content
             day.hands_on_content = ""
             
        day.save()
        print(f"Updated Day {day_num}: {day.title}")

if __name__ == "__main__":
    populate_week4()
