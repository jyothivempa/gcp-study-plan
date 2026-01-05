"""
Django REST Framework Serializers for GCP Study Plan API
=========================================================
Provides structured JSON responses for all models.
"""

from rest_framework import serializers
from .models import Course, Week, Day, UserProgress, QuizQuestion, UserNote, QuizScore


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course model"""
    weeks_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'description', 'icon_class', 'weeks_count']
    
    def get_weeks_count(self, obj):
        return obj.weeks.count()


class DayListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for Day listings"""
    week_number = serializers.IntegerField(source='week.number', read_only=True)
    course_slug = serializers.CharField(source='week.course.slug', read_only=True)
    
    class Meta:
        model = Day
        fields = ['id', 'number', 'title', 'description', 'week_number', 'course_slug']


class DayDetailSerializer(serializers.ModelSerializer):
    """Full serializer for Day detail view"""
    week_number = serializers.IntegerField(source='week.number', read_only=True)
    course_slug = serializers.CharField(source='week.course.slug', read_only=True)
    quiz_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Day
        fields = [
            'id', 'number', 'title', 'description',
            'concept_content', 'hands_on_content', 'outcome',
            'interview_questions', 'video_url',
            'week_number', 'course_slug', 'quiz_count',
            'created_at', 'updated_at'
        ]
    
    def get_quiz_count(self, obj):
        return obj.quiz_questions.count()


class WeekSerializer(serializers.ModelSerializer):
    """Serializer for Week with nested days"""
    days = DayListSerializer(many=True, read_only=True)
    course_slug = serializers.CharField(source='course.slug', read_only=True)
    
    class Meta:
        model = Week
        fields = ['id', 'number', 'description', 'course_slug', 'days']


class UserProgressSerializer(serializers.ModelSerializer):
    """Serializer for user progress tracking"""
    day_number = serializers.IntegerField(source='day.number', read_only=True)
    day_title = serializers.CharField(source='day.title', read_only=True)
    
    class Meta:
        model = UserProgress
        fields = ['id', 'day_number', 'day_title', 'completed', 'completed_at']
        read_only_fields = ['completed_at']


class QuizQuestionSerializer(serializers.ModelSerializer):
    """Serializer for quiz questions (excludes correct answer for security)"""
    
    class Meta:
        model = QuizQuestion
        fields = [
            'id', 'question_type', 'question_text',
            'option_1', 'option_2', 'option_3', 'option_4'
        ]
        # Note: correct_option and explanation are intentionally excluded


class QuizAnswerSerializer(serializers.Serializer):
    """Serializer for quiz answer submission"""
    question_id = serializers.IntegerField()
    selected_option = serializers.IntegerField(min_value=1, max_value=4)


class QuizSubmissionSerializer(serializers.Serializer):
    """Serializer for full quiz submission"""
    answers = QuizAnswerSerializer(many=True)


class QuizResultSerializer(serializers.Serializer):
    """Serializer for quiz results"""
    score = serializers.IntegerField()
    total = serializers.IntegerField()
    percentage = serializers.FloatField()
    passed = serializers.BooleanField()
    results = serializers.ListField()


class UserNoteSerializer(serializers.ModelSerializer):
    """Serializer for user notes"""
    day_number = serializers.IntegerField(source='day.number', read_only=True)
    
    class Meta:
        model = UserNote
        fields = ['id', 'day_number', 'content', 'updated_at']
        read_only_fields = ['updated_at']


class QuizScoreSerializer(serializers.ModelSerializer):
    """Serializer for QuizScore model"""
    day_number = serializers.IntegerField(source='day.number', read_only=True)
    
    class Meta:
        model = QuizScore
        fields = [
            'id', 'day_number', 'score', 'total_questions', 
            'percentage', 'passed', 'created_at'
        ]

class ProgressSummarySerializer(serializers.Serializer):
    """Serializer for progress summary dashboard"""
    total_days = serializers.IntegerField()
    completed_days = serializers.IntegerField()
    completion_percentage = serializers.FloatField()
    current_streak = serializers.IntegerField()
    longest_streak = serializers.IntegerField()
    xp = serializers.IntegerField()
    level = serializers.IntegerField()
