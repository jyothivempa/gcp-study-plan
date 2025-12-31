from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add custom fields here if needed in the future
    pass
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_study_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile (Lvl {self.level})"

    def add_xp(self, amount):
        self.xp += amount
        # Simple leveling logic: Level up every 500 XP * current_level
        # e.g., Lvl 1->2 needs 500, Lvl 2->3 needs 1000
        required_xp = self.level * 500 
        if self.xp >= required_xp:
            self.level += 1
            self.xp -= required_xp # Deduct or keep cumulative? Let's keep cumulative logic simple for now
            # Actually, standard is cumulative XP total. Let's recalculate level based on total XP.
            # Lvl = Floor(XP / 500) + 1 roughly.
            self.level = (self.xp // 500) + 1
        self.save()
