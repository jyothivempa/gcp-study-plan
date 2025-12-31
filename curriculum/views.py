from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Course, Week, Day, UserProgress, UserNote, SearchLog
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from django.db.models import Q, Count
from .verification import verify_capstone_project
from .gamification import award_xp, update_streak, XP_LESSON_COMPLETE, XP_LAB_VERIFIED

def search_lessons(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        results = Day.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(concept_content__icontains=query) |
            Q(hands_on_content__icontains=query)
        ).select_related('week')
        
        # Log Search
        user = request.user if request.user.is_authenticated else None
        SearchLog.objects.create(user=user, query=query, results_count=results.count())
    
    # Analytics
    popular_searches = SearchLog.objects.values('query').annotate(count=Count('query')).order_by('-count')[:5]
    recent_searches = []
    if request.user.is_authenticated:
        recent_searches = SearchLog.objects.filter(user=request.user).order_by('-timestamp')[:5]

    context = {
        'query': query,
        'results': results,
        'popular_searches': popular_searches,
        'recent_searches': recent_searches
    }
    return render(request, 'search_results.html', context)

def curriculum_overview(request):
    # Automatically redirect to the GCP course for a cleaner, single-course experience
    return redirect('course_detail', course_slug='gcp')

def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    weeks = Week.objects.prefetch_related('days').filter(course=course)
    completed_day_ids = []
    progress_percentage = 0
    
    if request.user.is_authenticated:
        # Filter progress for this course ONLY
        completed_day_ids = UserProgress.objects.filter(
            user=request.user, 
            completed=True,
            day__week__course=course
        ).values_list('day_id', flat=True)
        
        # Calculate progress
        total = Day.objects.filter(week__course=course).count()
        if total > 0:
            progress_percentage = int((len(completed_day_ids) / total) * 100)

    context = {
        'course': course,
        'weeks': weeks, 
        'completed_day_ids': completed_day_ids,
        'user_progress_percentage': progress_percentage
    }
    return render(request, 'course_detail.html', context)

def ace_guide(request):
    return render(request, 'ace_guide.html')

def style_guide(request):
    return render(request, 'style_guide.html')

def ace_cheat_sheet(request):
    return render(request, 'ace_cheat_sheet.html')

def lesson_detail(request, course_slug, day_number):
    # Ensure day belongs to course
    day = get_object_or_404(Day, number=day_number, week__course__slug=course_slug)
    course = day.week.course
    
    # Access Control: Day 1 of ANY course is free
    # Note: Logic assumes day.number is unique per course (1, 2, 3...)
    if not request.user.is_authenticated and day.number > 1:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    # Handle Progress Toggle
    is_completed = False
    if request.user.is_authenticated:
        progress, created = UserProgress.objects.get_or_create(user=request.user, day=day)
        if request.method == 'POST' and 'toggle_complete' in request.POST:
            progress.completed = not progress.completed
            if progress.completed:
                progress.completed_at = timezone.now()
                # GAMIFICATION
                award_xp(request.user, XP_LESSON_COMPLETE)
                update_streak(request.user)
            else:
                progress.completed_at = None
            progress.save()
            return redirect('lesson_detail', course_slug=course.slug, day_number=day.number)
        is_completed = progress.completed

    next_day = Day.objects.filter(number=day.number + 1, week__course=course).first()
    prev_day = Day.objects.filter(number=day.number - 1, week__course=course).first()
    
    # Calculate global progress for navbar (Course specific now)
    progress_percentage = 0
    if request.user.is_authenticated:
        total = Day.objects.filter(week__course=course).count()
        if total > 0:
            completed_count = UserProgress.objects.filter(
                user=request.user, 
                completed=True,
                day__week__course=course
            ).count()
            progress_percentage = int((completed_count / total) * 100)

    context = {
        'day': day,
        'course': course,
        'next_day': next_day,
        'prev_day': prev_day,
        'is_completed': is_completed,
        'user_progress_percentage': progress_percentage,
        'user_note': UserNote.objects.filter(user=request.user, day=day).first() if request.user.is_authenticated else None,
        'has_verification': day.number in [4, 6, 8, 12, 13, 18, 19, 42, 43, 44, 45] # Hardcoded logic for now, or import from verification.py
    }
    return render(request, 'lesson_detail.html', context)

@login_required
def dashboard(request):
    # Feature removed per user request: redirect to curriculum overview
    return redirect('curriculum_overview')

@login_required
def certificate_view(request):
    total_days = Day.objects.count()
    completed_count = UserProgress.objects.filter(user=request.user, completed=True).count()
    
    # Check eligibility (100% completion)
    if completed_count < total_days:
        # Redirect to dashboard with message (or handle via template)
        return redirect('dashboard')
        
    completion_date = UserProgress.objects.filter(user=request.user, completed=True).latest('completed_at').completed_at
    
    context = {
        'completion_date': completion_date or datetime.now()
    }
    return render(request, 'certificate.html', context)

@login_required
@require_POST
def ask_ai(request):
    try:
        data = json.loads(request.body)
        question = data.get('question')
        day_number = data.get('day_number')
        
        if not question or not day_number:
            return JsonResponse({'error': 'Missing data'}, status=400)
            
        day = Day.objects.get(number=day_number)
        context = day.content
        answer = get_gemini_response(question, context)
        
        return JsonResponse({'answer': answer})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@require_POST
def save_note(request, day_number):
    try:
        data = json.loads(request.body)
        content = data.get('content')
        
        # Allow empty string (clearing notes) but check for None
        if content is None:
            return JsonResponse({'error': 'Missing content'}, status=400)
            
        day = get_object_or_404(Day, number=day_number)
        
        UserNote.objects.update_or_create(
            user=request.user, 
            day=day,
            defaults={'content': content}
        )
        
        return JsonResponse({'status': 'saved'})
    except Exception as e:
        # Log the error in production
        print(f"Error saving note: {e}")
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@require_POST
def verify_capstone(request):
    try:
        data = json.loads(request.body)
        project_id = data.get('project_id')
        day_number = data.get('day_number')
        
        if not project_id:
            return JsonResponse({'success': False, 'message': 'Project ID is required.'}, status=400)
            
        success, message = verify_capstone_project(day_number, project_id)
        
        # If success, mark day as complete
        if success:
            day = get_object_or_404(Day, number=day_number)
            UserProgress.objects.update_or_create(
                user=request.user, 
                day=day,
                defaults={'completed': True}
            )
            # GAMIFICATION
            award_xp(request.user, XP_LAB_VERIFIED)
            update_streak(request.user)
        
        return JsonResponse({'success': success, 'message': message})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@login_required
def study_flashcards(request, day_number):
    day = get_object_or_404(Day, number=day_number)
    
    # Check if flashcards exist
    if not day.flashcards:
        # Fallback or empty state
        return redirect('lesson_detail', course_slug=day.week.course.slug, day_number=day.number)
        
    flashcards_data = day.flashcards # This is a list of dicts [{'front': '...', 'back': '...'}]
    
    # TODO: In a real app, we would only serve cards due for review based on FlashcardProgress
    # For now, we serve all cards but could sort them by 'box' if we fetched progress.
    
    context = {
        'day': day,
        'cards_json': json.dumps(flashcards_data)
    }
    return render(request, 'flashcard_study.html', context)

@login_required
@require_POST
def submit_flashcard(request):
    try:
        from .models import FlashcardProgress
        data = json.loads(request.body)
        day_number = data.get('day_number')
        card_index = data.get('card_index')
        result = data.get('result') # 'easy' or 'hard'
        
        day = get_object_or_404(Day, number=day_number)
        
        progress, created = FlashcardProgress.objects.get_or_create(
            user=request.user,
            day=day,
            card_index=card_index
        )
        
        # Leitner Logic
        if result == 'easy':
            progress.box = min(progress.box + 1, 5) # Max box 5
        else:
            progress.box = 1 # Reset to daily review
            
        progress.save()
        
        return JsonResponse({'status': 'ok', 'new_box': progress.box})
    except Exception as e:
        print(f"Error submitting flashcard: {e}")
        return JsonResponse({'error': str(e)}, status=500)

from .ai_utils import get_flashcard_explanation

@login_required
@require_POST
def explain_flashcard(request):
    """
    API endpoint to get an AI explanation for a flashcard.
    Expects JSON: { "question": "...", "answer": "...", "context": "..." }
    """
    try:
        data = json.loads(request.body)
        question = data.get('question')
        answer = data.get('answer')
        context = data.get('context', '')
        
        if not question or not answer:
            return JsonResponse({'error': 'Missing question or answer'}, status=400)
            
        explanation = get_flashcard_explanation(question, answer, context)
        
        return JsonResponse({'explanation': explanation})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
