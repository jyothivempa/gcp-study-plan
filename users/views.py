from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Use custom user model form if needed, but standard UserCreationForm works if User model is simple inheritance
# But since we have a custom user model, we should use a custom form ideally, 
# but UserCreationForm in Django < 4 needs override. In Django 4+ it detects custom user model?
# Let's import UserCreationForm and see. We might need to subclass it if it references auth.User directly.
# Standard practice is to create a CustomUserCreationForm.

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('curriculum_overview')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
