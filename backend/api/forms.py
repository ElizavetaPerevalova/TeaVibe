from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'problem_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }