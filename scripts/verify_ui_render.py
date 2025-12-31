import sys
import os
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import django
from django.conf import settings
from django.template.loader import render_to_string
from django.test import RequestFactory

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from users.models import User

def verify_render():
    try:
        # Get the user
        user = User.objects.get(username='jyothi')
        print(f"User found: {user.username} (Level: {user.profile.level}, Streak: {user.profile.current_streak})")
        
        # Create a mock request
        factory = RequestFactory()
        request = factory.get('/')
        request.user = user
        
        # Render the template
        # We render a simple string allowing base to be extended or just render base directly?
        # Rendering base directly might fail if it expects blocks, but usually it works fine for checking header.
        # Let's render 'base.html' directly.
        rendered = render_to_string('base.html', request=request)
        
        # Check for specific strings
        print("\n--- Verification Results ---")
        
        # Check Streak
        expected_streak = f'>{user.profile.current_streak}</span>'
        # The template has: <span ...>\n     {{ user.profile.current_streak }}\n </span>
        # So we look for the number.
        
        if str(user.profile.level) in rendered and "Level " + str(user.profile.level) in rendered: # Rough check
             pass
        
        # Let's explicitly check for the FAIL case
        fail_patterns = [
            "{{ user.profile.current_streak }}",
            "{{ user.profile.level }}",
            "{{ user.profile.xp }}",
            "%}" 
        ]
        
        failed = False
        for pat in fail_patterns:
            if pat in rendered:
                print(f"❌ FAIL: Found raw template tag: {pat}")
                failed = True
                
        if not failed:
            print("✅ SUCCES: No raw template tags found.")
            
            # Check for actual values
            # We look for substrings that indicate success roughly, ignoring whitespace
            if f"Level {user.profile.level}" in " ".join(rendered.split()):
                 print(f"✅ FOUND: 'Level {user.profile.level}'")
            else:
                 print(f"⚠️ WARNING: Could not find exact string 'Level {user.profile.level}' (might be whitespace related), but raw tags are gone.")
                 
            # print snippet
            print("\nSnippet of Rendered Output (Header):")
            # Find the index of "Level"
            idx = rendered.find("Level")
            if idx != -1:
                print(rendered[idx-50:idx+100])
                
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    verify_render()
