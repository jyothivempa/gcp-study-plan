"""
REST API Views for GCP Study Plan
==================================
Provides JSON API endpoints for progress tracking, quiz submission, and data retrieval.
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count, Q

from .models import Course, Week, Day, UserProgress, QuizQuestion, UserNote, QuizScore
from .serializers import (
    CourseSerializer, WeekSerializer, DayListSerializer, DayDetailSerializer,
    UserProgressSerializer, QuizQuestionSerializer, QuizSubmissionSerializer,
    QuizResultSerializer, UserNoteSerializer, ProgressSummarySerializer,
    QuizScoreSerializer
)


# =============================================================================
# COURSE & CURRICULUM API
# =============================================================================

@api_view(['GET'])
@permission_classes([AllowAny])
def course_list(request):
    """
    GET /api/courses/
    List all available courses.
    """
    courses = Course.objects.annotate(
        weeks_count=Count('weeks'),
        total_days=Count('weeks__days')
    )
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def course_detail_api(request, course_slug):
    """
    GET /api/courses/<slug>/
    Get course details with all weeks and days.
    """
    course = get_object_or_404(
        Course.objects.prefetch_related('weeks__days'),
        slug=course_slug
    )
    
    weeks = course.weeks.all().prefetch_related('days')
    
    data = {
        'course': CourseSerializer(course).data,
        'weeks': WeekSerializer(weeks, many=True).data
    }
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def day_detail_api(request, course_slug, day_number):
    """
    GET /api/courses/<slug>/days/<number>/
    Get full day/lesson details.
    """
    day = get_object_or_404(
        Day.objects.select_related('week__course'),
        number=day_number,
        week__course__slug=course_slug
    )
    serializer = DayDetailSerializer(day)
    return Response(serializer.data)


# =============================================================================
# PROGRESS API
# =============================================================================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def progress_summary(request):
    """
    GET /api/progress/
    Get user's overall progress summary.
    """
    user = request.user
    
    # Get progress stats
    total_days = Day.objects.count()
    completed_progress = UserProgress.objects.filter(
        user=user, completed=True
    ).count()
    
    # Get profile stats (if exists)
    try:
        profile = user.profile
        xp = profile.xp
        level = profile.level
        current_streak = profile.current_streak
        longest_streak = profile.longest_streak
    except:
        xp = 0
        level = 1
        current_streak = 0
        longest_streak = 0
    
    data = {
        'total_days': total_days,
        'completed_days': completed_progress,
        'completion_percentage': round((completed_progress / total_days) * 100, 1) if total_days > 0 else 0,
        'current_streak': current_streak,
        'longest_streak': longest_streak,
        'xp': xp,
        'level': level
    }
    
    serializer = ProgressSummarySerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def progress_list(request):
    """
    GET /api/progress/days/
    Get user's progress for all days.
    """
    progress = UserProgress.objects.filter(
        user=request.user
    ).select_related('day')
    
    serializer = UserProgressSerializer(progress, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_complete(request, day_number):
    """
    POST /api/progress/<day_number>/complete/
    Mark a day/lesson as complete.
    """
    day = get_object_or_404(Day, number=day_number)
    
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        day=day,
        defaults={'completed': True, 'completed_at': timezone.now()}
    )
    
    if not created and not progress.completed:
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()
    
    # Award XP if available
    try:
        from .gamification import award_xp, update_streak, XP_LESSON_COMPLETE
        award_xp(request.user, XP_LESSON_COMPLETE)
        update_streak(request.user)
    except:
        pass
    
    serializer = UserProgressSerializer(progress)
    return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_incomplete(request, day_number):
    """
    POST /api/progress/<day_number>/incomplete/
    Mark a day/lesson as incomplete.
    """
    day = get_object_or_404(Day, number=day_number)
    
    try:
        progress = UserProgress.objects.get(user=request.user, day=day)
        progress.completed = False
        progress.completed_at = None
        progress.save()
        serializer = UserProgressSerializer(progress)
        return Response(serializer.data)
    except UserProgress.DoesNotExist:
        return Response({'detail': 'No progress found for this day.'}, status=status.HTTP_404_NOT_FOUND)


# =============================================================================
# QUIZ API
# =============================================================================

@api_view(['GET'])
@permission_classes([AllowAny])
def quiz_questions(request, day_number):
    """
    GET /api/quiz/<day_number>/
    Get quiz questions for a day (without correct answers).
    """
    day = get_object_or_404(Day, number=day_number)
    questions = day.quiz_questions.all()
    serializer = QuizQuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_quiz(request, day_number):
    """
    POST /api/quiz/<day_number>/submit/
    Submit quiz answers and get results.
    
    Request body:
    {
        "answers": [
            {"question_id": 1, "selected_option": 2},
            {"question_id": 2, "selected_option": 1}
        ]
    }
    """
    day = get_object_or_404(Day, number=day_number)
    
    submission_serializer = QuizSubmissionSerializer(data=request.data)
    if not submission_serializer.is_valid():
        return Response(submission_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    answers = submission_serializer.validated_data['answers']
    questions = {q.id: q for q in day.quiz_questions.filter(question_type='mcq')}
    
    results = []
    correct_count = 0
    
    for answer in answers:
        question_id = answer['question_id']
        selected = answer['selected_option']
        
        if question_id in questions:
            question = questions[question_id]
            is_correct = question.correct_option == selected
            
            if is_correct:
                correct_count += 1
            
            results.append({
                'question_id': question_id,
                'selected_option': selected,
                'correct_option': question.correct_option,
                'is_correct': is_correct,
                'explanation': question.explanation if not is_correct else None
            })
    
    total = len(questions)
    percentage = round((correct_count / total) * 100, 1) if total > 0 else 0
    passed = percentage >= 70
    
    # Save the score
    QuizScore.objects.create(
        user=request.user,
        day=day,
        score=correct_count,
        total_questions=total,
        percentage=percentage,
        passed=passed
    )
    
    response_data = {
        'score': correct_count,
        'total': total,
        'percentage': percentage,
        'passed': passed,
        'results': results
    }
    
    return Response(response_data)


# =============================================================================
# NOTES API
# =============================================================================

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def user_note(request, day_number):
    """
    GET/POST/PUT /api/notes/<day_number>/
    Get or save user notes for a day.
    """
    day = get_object_or_404(Day, number=day_number)
    
    if request.method == 'GET':
        try:
            note = UserNote.objects.get(user=request.user, day=day)
            serializer = UserNoteSerializer(note)
            return Response(serializer.data)
        except UserNote.DoesNotExist:
            return Response({'content': '', 'day_number': day_number})
    
    # POST or PUT
    note, created = UserNote.objects.get_or_create(
        user=request.user,
        day=day,
        defaults={'content': request.data.get('content', '')}
    )
    
    if not created:
        note.content = request.data.get('content', note.content)
        note.save()
    
    serializer = UserNoteSerializer(note)
    return Response(
        serializer.data, 
        status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
    )


# =============================================================================
# SEARCH API
# =============================================================================

@api_view(['GET'])
@permission_classes([AllowAny])
def search_api(request):
    """
    GET /api/search/?q=query
    Search lessons by title and content.
    """
    query = request.query_params.get('q', '')
    
    if not query:
        return Response({'results': [], 'query': ''})
    
    results = Day.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(concept_content__icontains=query) |
        Q(hands_on_content__icontains=query)
    ).select_related('week__course')[:20]
    
    serializer = DayListSerializer(results, many=True)
    return Response({
        'query': query,
        'count': len(results),
        'results': serializer.data
    })
