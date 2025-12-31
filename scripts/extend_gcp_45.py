import os
import django
from curriculum.models import Course, Week, Day

# Define new content topics
NEW_DAYS = {
    38: ("Anthos & Multi-Cloud", "Managing hybrid and multi-cloud Kubernetes clusters."),
    39: ("Cloud Spanner Deep Dive", "Advanced schema design and query optimization for Spanner."),
    40: ("BigQuery Machine Learning (BQML)", "Training ML models directly inside BigQuery using SQL."),
    41: ("Vertex AI & MLOps", "End-to-end machine learning pipelines on Google Cloud."),
    42: ("SAP on Google Cloud", "Architecture patterns for hosting SAP workloads."),
    43: ("Google Cloud VMWare Engine", "Migrating VMWare workloads to GCP without refactoring."),
    44: ("Professional Architect Exam Prep", "Deep dive into case studies and difficult exam scenarios."),
    45: ("Final Capstone: The Enterprise Migration", "Simulated large-scale migration project planning.")
}

TEMPLATE = """# Day {day}: {title}

## Overview
{desc}

## Core Concepts
This advanced module covers...

## Hands-On Lab
Pending...
"""

def scaffold_extension():
    print("--- Extending GCP to 45 Days ---")
    
    gcp = Course.objects.get(slug='gcp')
    
    # 1. Create Weeks 6 and 7
    week6, _ = Week.objects.get_or_create(course=gcp, number=6, defaults={'description': 'Advanced Hybrid & Multi-Cloud'})
    week7, _ = Week.objects.get_or_create(course=gcp, number=7, defaults={'description': 'Professional Architect & Wrap-up'})
    
    print("✅ Verified Weeks 6 & 7")

    # 2. Create Days
    for day_num, (title, desc) in NEW_DAYS.items():
        w_obj = week6 if day_num <= 42 else week7
        
        # Create DB Entry
        d, created = Day.objects.get_or_create(
            number=day_num,
            defaults={
                'week': w_obj,
                'title': title,
                'description': desc,
                'concept_content': TEMPLATE.format(day=day_num, title=title, desc=desc),
                'hands_on_content': "Lab pending...",
                'outcome': "Master advanced topic."
            }
        )
        
        # Ensure it is linked to GCP if it pre-existed (e.g. from Azure collision)
        if d.week != w_obj:
            d.week = w_obj
            d.save()
            print(f"🔄 Re-linked Day {day_num} to GCP Week {w_obj.number}")
            
        print(f"{'✅ Created' if created else '🆗 Verified'} Day {day_num}: {title}")

if __name__ == '__main__':
    scaffold_extension()
