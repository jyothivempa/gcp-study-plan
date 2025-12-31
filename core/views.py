from django.shortcuts import render
from curriculum.models import Day, UserProgress

def get_progress(user):
    if user.is_authenticated:
        total = Day.objects.count()
        if total > 0:
            completed = UserProgress.objects.filter(user=user, completed=True).count()
            return int((completed / total) * 100)
    return 0

def home(request):
    return render(request, 'home.html', {'user_progress_percentage': get_progress(request.user)})

def projects(request):
    return render(request, 'projects.html', {'user_progress_percentage': get_progress(request.user)})

def roadmap(request):
    return render(request, 'roadmap.html', {'user_progress_percentage': get_progress(request.user)})
