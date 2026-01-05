from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL friendly identifier (e.g. 'gcp', 'azure')")
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=50, default="fa-brands fa-google", help_text="FontAwesome class")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Week(models.Model):
    course = models.ForeignKey(Course, related_name='weeks', on_delete=models.CASCADE, null=True, blank=True)
    number = models.PositiveIntegerField(db_index=True, help_text="Week number (1-4)")
    description = models.TextField(help_text="Overview of what is covered this week")

    def __str__(self):
        return f"{self.course.slug.upper() if self.course else '???'} - Week {self.number}"

    class Meta:
        ordering = ['course', 'number']
        unique_together = ['course', 'number']

class Day(models.Model):
    week = models.ForeignKey(Week, related_name='days', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(db_index=True, help_text="Day number (1-45)")
    title = models.CharField(max_length=200, help_text="Title of the day's topic")
    description = models.TextField(blank=True, help_text="Short description for the curriculum card")
    
    # Lesson Content
    concept_content = models.TextField(help_text="Markdown content for 'Concept' section")
    hands_on_content = models.TextField(help_text="Markdown content for 'Hands-on' section")
    outcome = models.CharField(max_length=255, help_text="What the learner will achieve")
    interview_questions = models.TextField(help_text="Markdown for interview questions", blank=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube URL for the lesson video")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Day {self.number}: {self.title}"

    class Meta:
        ordering = ['number']

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='progress', on_delete=models.CASCADE)
    day = models.ForeignKey(Day, related_name='user_progress', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'day']
        verbose_name_plural = "User Progress"

    def __str__(self):
        return f"{self.user.username} - Day {self.day.number} ({'Done' if self.completed else 'Pending'})"

class UserNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notes', on_delete=models.CASCADE)
    day = models.ForeignKey(Day, related_name='user_notes', on_delete=models.CASCADE)
    content = models.TextField(blank=True, help_text="User's private notes for this day")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'day']

    def __str__(self):
        return f"Note by {self.user.username} for Day {self.day.number}"

class QuizQuestion(models.Model):
    TYPE_CHOICES = [
        ('mcq', 'Multiple Choice'),
        ('text', 'Self Check (Text)'),
    ]
    
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='quiz_questions')
    question_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='mcq')
    question_text = models.TextField()
    
    # Options (Required for MCQ, Optional for Text)
    option_1 = models.CharField(max_length=255, blank=True, null=True)
    option_2 = models.CharField(max_length=255, blank=True, null=True)
    option_3 = models.CharField(max_length=255, blank=True, null=True)
    option_4 = models.CharField(max_length=255, blank=True, null=True)
    
    # Answers
    correct_option = models.IntegerField(help_text="1-4 for MCQ. Ignored for Text.", blank=True, null=True)
    explanation = models.TextField(help_text="Explanation/Answer for Self-Check questions", blank=True)

    def __str__(self):
        return f"[{self.get_question_type_display()}] {self.question_text}"

class QuizScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='quiz_scores', on_delete=models.CASCADE)
    day = models.ForeignKey(Day, related_name='quiz_scores', on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.FloatField()
    passed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Quiz Scores"

    def __str__(self):
        return f"{self.user.username} - Day {self.day.number} Score: {self.score}/{self.total_questions}"

class SearchLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    results_count = models.IntegerField(default=0)

    def __str__(self):
        return f"'{self.query}' ({self.results_count} results)"



