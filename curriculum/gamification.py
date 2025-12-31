from datetime import date, timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import User, UserProfile

# --- XP CONSTANTS ---
XP_LESSON_COMPLETE = 100
XP_QUIZ_COMPLETE = 50
XP_LAB_VERIFIED = 150
XP_DAILY_LOGIN = 10

def award_xp(user, amount):
    """
    Awards XP to the user and handles leveling up.
    """
    profile, created = UserProfile.objects.get_or_create(user=user)
    profile.add_xp(amount)
    return profile

def update_streak(user):
    """
    Updates the user's daily streak.
    Should be called when a significant action (lesson, quiz) is completed.
    """
    profile, _ = UserProfile.objects.get_or_create(user=user)
    today = date.today()
    
    if profile.last_study_date == today:
        # Already studied today, nothing to do
        return profile
    
    if profile.last_study_date == today - timedelta(days=1):
        # Studied yesterday, extend streak
        profile.current_streak += 1
    else:
        # Missed a day (or first day), reset/start streak
        profile.current_streak = 1
        
    # Update longest streak
    if profile.current_streak > profile.longest_streak:
        profile.longest_streak = profile.current_streak
        
    profile.last_study_date = today
    profile.save()
    
    # Bonus XP for streak milestones?
    # award_xp(user, 10 * profile.current_streak) # Optional
    
    return profile

# --- SIGNALS ---
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
