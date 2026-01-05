from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Course, Week, Day, UserProgress, UserNote, SearchLog
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from django.views.decorators.cache import cache_page
from django.db.models import Q, Count, Prefetch
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

@cache_page(60 * 15)
def curriculum_overview(request):
    # Automatically redirect to the GCP course for a cleaner, single-course experience
    return redirect('course_detail', course_slug='gcp')

def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    
    # Optimized query with prefetch_related
    weeks = Week.objects.prefetch_related(
        Prefetch('days', queryset=Day.objects.only('id', 'number', 'title', 'description', 'week_id'))
    ).filter(course=course).order_by('number')
    
    completed_day_ids = []
    progress_percentage = 0
    
    if request.user.is_authenticated:
        # Optimized progress fetching
        progress_qs = UserProgress.objects.filter(
            user=request.user, 
            completed=True,
            day__week__course=course
        ).values_list('day_id', flat=True)
        completed_day_ids = list(progress_qs)
        
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

@cache_page(60 * 60)
def ace_guide(request):
    return render(request, 'ace_guide.html')

@cache_page(60 * 60)
def style_guide(request):
    return render(request, 'style_guide.html')

@cache_page(60 * 60)
def ace_cheat_sheet(request):
    return render(request, 'ace_cheat_sheet.html')

def lesson_detail(request, course_slug, day_number):
    # Highly optimized query with select_related and prefetch_related
    day = get_object_or_404(
        Day.objects.select_related('week__course').prefetch_related('quiz_questions'), 
        number=day_number, 
        week__course__slug=course_slug
    )
    course = day.week.course
    
    # Access Control: Day 1 of ANY course is free
    if not request.user.is_authenticated and day.number > 1:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    # Handle Progress Toggle
    is_completed = False
    if request.user.is_authenticated:
        # Optimization: Use filter().first() to avoid automatic DB writes on basic reads
        progress = UserProgress.objects.filter(user=request.user, day=day).first()
        
        if request.method == 'POST' and 'toggle_complete' in request.POST:
            if not progress:
                progress = UserProgress.objects.create(user=request.user, day=day)
                
            progress.completed = not progress.completed
            if progress.completed:
                progress.completed_at = timezone.now()
                award_xp(request.user, XP_LESSON_COMPLETE)
                update_streak(request.user)
            else:
                progress.completed_at = None
            progress.save()
            # Cache Invalidation: Clear the progress percentage cache for the user
            from django.core.cache import cache
            cache.delete(f"user_progress_{request.user.id}")
            
            return redirect('lesson_detail', course_slug=course.slug, day_number=day.number)
            
        if progress:
            is_completed = progress.completed

    # Use single query for navigation if possible, or simple filters
    next_day = Day.objects.filter(number=day.number + 1, week__course=course).only('number').first()
    prev_day = Day.objects.filter(number=day.number - 1, week__course=course).only('number').first()
    
    # Context data
    context = {
        'course': course,
        'day': day,
        'next_day': next_day,
        'prev_day': prev_day,
        'is_completed': is_completed,
        'has_verification': day.number in [4, 6, 8, 12, 13, 18, 19, 42, 43, 44, 45],
        'week_title': f"Week {day.week.number}"
    }
    return render(request, 'lesson_detail.html', context)

@cache_page(60 * 15)
def get_sidebar_data(request, course_slug, day_number):
    """
    API Endpoint to fetch sidebar data as JSON.
    Separates UI rendering from Data Logic.
    Cached for 15 minutes to reduce DB load on navigation.
    """
    day = get_object_or_404(Day, number=day_number, week__course__slug=course_slug)
    
    sidebar_data = []
    week_days = day.week.days.all().order_by('number')
    
    for d in week_days:
        is_active = (d.number == day.number)
        is_past = (d.number < day.number)
        
        # Determine CSS classes in Python (Backend Logic)
        row_class = "group relative flex items-center gap-3 p-3 rounded-xl transition-all duration-200 border "
        if is_active:
            row_class += "bg-brand-50/80 dark:bg-brand-900/20 border-brand-200 dark:border-brand-500/30 shadow-sm"
        else:
            row_class += "hover:bg-slate-100 dark:hover:bg-white/5 border-transparent"
            
        icon_class = "w-8 h-8 rounded-lg flex items-center justify-center text-xs font-bold transition-colors shrink-0 "
        if is_active:
            icon_class += "bg-brand-600 text-white shadow-lg shadow-brand-500/30"
        elif is_past:
             icon_class += "bg-green-100 text-green-600 dark:bg-green-900/30 dark:text-green-400"
        else:
             icon_class += "bg-slate-100 text-slate-400 dark:bg-slate-800 dark:text-slate-600"
             
        text_class = "text-sm font-bold truncate "
        if is_active:
            text_class += "text-brand-900 dark:text-brand-100"
        else:
            text_class += "text-slate-600 dark:text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white"

        sidebar_data.append({
            'number': d.number,
            'title': d.title,
            'is_active': is_active,
            'is_past': is_past,
            'row_class': row_class,
            'icon_class': icon_class,
            'text_class': text_class,
            'url': f"/curriculum/course/{course_slug}/day/{d.number}/" # Pre-calculate URL
        })
        
    return JsonResponse({
        'week_number': day.week.number,
        'items': sidebar_data
    })

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
            
            # Cache Invalidation: Clear the progress percentage cache for the user
            from django.core.cache import cache
            cache.delete(f"user_progress_{request.user.id}")
        
        return JsonResponse({'success': success, 'message': message})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@cache_page(60 * 60 * 24)
def faq(request):
    """FAQ page view"""
    return render(request, 'faq.html')
