from django.contrib import admin
from .models import Course, Week, Day, UserProgress, UserNote, QuizQuestion, QuizScore, SearchLog

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('number', 'description')

class QuizQuestionInline(admin.StackedInline):
    model = QuizQuestion
    extra = 1

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('week', 'number', 'title')
    list_filter = ('week',)
    search_fields = ('title', 'description')
    inlines = [QuizQuestionInline]

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'completed', 'completed_at')
    list_filter = ('completed', 'day__week')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

@admin.register(UserNote)
class UserNoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'updated_at')

@admin.register(QuizScore)
class QuizScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'score', 'total_questions', 'percentage', 'passed', 'created_at')
    list_filter = ('passed', 'day')

@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('query', 'user', 'results_count', 'timestamp')
    list_filter = ('timestamp',)

