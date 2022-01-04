from django import forms
from django.db.models.fields import TextField
from django.forms.widgets import Textarea
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','bio','profile_pic','location']
        widgets = {
            'bio': Textarea(attrs={'cols': 30, 'rows': 3}),
        }