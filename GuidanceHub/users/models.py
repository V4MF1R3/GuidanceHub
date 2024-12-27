from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [('mentor', 'Mentor'), ('mentee', 'Mentee')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField()
    interests = models.TextField()

    def __str__(self):
        return self.user.username