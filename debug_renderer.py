import os
import django
import sys
import json

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from django.test import Client

def debug_view():
    print("=== DEBUG START ===")
    c = Client()
    
    # 1. PAGE VERIFICATION
    print("\n[1] Fetching Lesson Page (Day 1)...")
    try:
        response = c.get('/curriculum/course/gcp/day/1/', HTTP_HOST='127.0.0.1')
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            content = response.content.decode()
            
            # DARK MODE VERIFICATION
            if '<html lang="en" class="dark scroll-smooth">' in content:
                 print("THEME VERIFICATION: PASS (Forced Dark Mode found)")
            else:
                 print("THEME VERIFICATION: FAIL (Did not find forced dark class)")
                 print(f"HTML Tag Context: {content[:100]}")
            
            # Check for API integration
            if "loadSidebar()" in content and "x-data" in content:
                 print("TEMPLATE VERIFICATION: PASS (Found Alpine.js 'loadSidebar')")
            else:
                 print("TEMPLATE VERIFICATION: FAIL (Did not find Alpine.js code)")

            # Check for raw tags cleaning
            if "{{ day.week.number }}" in content:
                 print("CLEANLINESS VERIFICATION: FAIL (Found raw template tag)")
            else:
                 print("CLEANLINESS VERIFICATION: PASS (No raw sidebar tags found)")
        else:
            print("Render Failed (Status != 200)")
            print(response.content.decode()[:500])
            
    except Exception as e:
        print(f"PAGE EXCEPTION: {e}")
        import traceback
        traceback.print_exc()

    # 2. API VERIFICATION
    print("\n[2] Fetching Sidebar API Endpoint...")
    try:
        api_response = c.get('/curriculum/api/sidebar_data/gcp/1/', HTTP_HOST='127.0.0.1')
        print(f"API Status Code: {api_response.status_code}")
        
        if api_response.status_code == 200:
            data = json.loads(api_response.content)
            print("API VERIFICATION: PASS (Valid JSON returned)")
            print(f"API Week Number: {data.get('week_number')}")
            print(f"API Items Count: {len(data.get('items', []))}")
            
            # Verify items structure
            if data.get('items'):
                first = data['items'][0]
                print(f"First Item: {first.get('title')} (Active: {first.get('is_active')})")
        else:
             print("API VERIFICATION: FAIL (Non-200 Status)")
             print(api_response.content.decode()[:500])
             
    except Exception as e:
        print(f"API EXCEPTION: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    debug_view()
