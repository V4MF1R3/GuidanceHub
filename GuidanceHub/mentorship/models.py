from django.db import models
from django.contrib.auth.models import User

class MentorshipRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.status})"

class MentorshipConnection(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_mentor')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_mentee')
    established_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentor} mentors {self.mentee}"
