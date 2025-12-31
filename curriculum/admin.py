from django.contrib import admin
from .models import Week, Day, UserProgress, QuizQuestion

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
