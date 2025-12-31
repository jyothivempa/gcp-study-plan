from curriculum.models import Course, Week, Day

def fix_weeks():
    print("--- Fixing Week Collisions ---")
    
    # 1. Get Courses
    gcp = Course.objects.get(slug='gcp')
    azure = Course.objects.get(slug='azure')
    
    print(f"GCP Course ID: {gcp.id}")
    print(f"Azure Course ID: {azure.id}")

    # 2. Fix GCP Weeks (1-5)
    gcp_week_titles = {
        1: 'Cloud Fundamentals & Core Infrastructure',
        2: 'Storage, Databases & Networking Deep Dive',
        3: 'Security, Identity & Monitoring',
        4: 'Containerization, Serverless & Final Prep',
        5: 'Advanced Scenarios & Capstones'
    }

    for num, title in gcp_week_titles.items():
        week, created = Week.objects.get_or_create(
            course=gcp,
            number=num,
            defaults={'description': title}
        )
        if created:
            print(f"✅ Created missing GCP Week {num}")
        else:
            # Enforce title correctness if it exists
            week.description = title
            week.save()
            print(f"🔄 Updated GCP Week {num}")

    # 3. Fix Azure Weeks (1-7)
    for num in range(1, 8):
        week, created = Week.objects.get_or_create(
            course=azure,
            number=num,
            defaults={'description': f'Azure Week {num}'}
        )
        if created:
            print(f"✅ Created missing Azure Week {num}")
        else:
            print(f"🆗 Azure Week {num} exists")

    # 4. Link GCP Days (1-30+)
    # We rely on ranges to assign them to the correct GCP week
    for num in range(1, 38): # Cover up to 37/38 (bonus days)
        try:
            day = Day.objects.get(number=num)
            
            # Determine correct week number
            if 1 <= num <= 7: w_num = 1
            elif 8 <= num <= 14: w_num = 2
            elif 15 <= num <= 21: w_num = 3
            elif 22 <= num <= 30: w_num = 4
            elif num >= 31: w_num = 5
            
            target_week = Week.objects.get(course=gcp, number=w_num)
            
            if day.week != target_week:
                day.week = target_week
                day.save()
                print(f"moved Day {num} to GCP Week {w_num}")
                
        except Day.DoesNotExist:
            pass # Day doesn't exist yet, skip
            
    print("--- Fix Complete ---")

if __name__ == '__main__':
    # Setup Django if run standalone (optional, user works via shell typically)
    pass
