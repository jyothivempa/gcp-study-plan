#!/usr/bin/env python
"""Quick script to update course description"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Course

# Update course description
try:
    course = Course.objects.get(slug='gcp')
    course.description = 'Master Google Cloud in 45 Days'
    course.save()
    print('Course description updated successfully!')
except Course.DoesNotExist:
    print('Course not found')
except Exception as e:
    print(f'Error: {e}')
