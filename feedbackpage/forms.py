from django import forms
from .models import *


class feedback_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    feedback = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = feedbackperson
        fields = ['name', 'email', 'feedback']
