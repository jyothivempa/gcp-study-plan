from .models import Day, UserProgress

def global_progress(request):
    progress_percentage = 0
    if request.user.is_authenticated:
        total_days = Day.objects.count()
        if total_days > 0:
            completed_count = UserProgress.objects.filter(user=request.user, completed=True).count()
            progress_percentage = int((completed_count / total_days) * 100)
    
    return {'user_progress_percentage': progress_percentage}
