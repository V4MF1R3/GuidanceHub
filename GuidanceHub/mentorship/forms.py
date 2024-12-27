from django import forms
from .models import MentorshipRequest

class MentorshipRequestForm(forms.ModelForm):
    class Meta:
        model = MentorshipRequest
        fields = ['receiver']
