from django import forms
from django.db.models.fields import TextField
from django.forms.widgets import Textarea
from .models import Neighborhood, Profile,Business,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','bio','profile_pic','location','neighborhood']
        widgets = {
            'bio': Textarea(attrs={'cols': 30, 'rows': 3}),
        }

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name', 'image','description','area_administrator','location','health_tell','police_tell']
        widgets = {
            'description': Textarea(attrs={'cols' : 20, 'rows' : 3}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','image','neighborhood','email','description']
        widgets = {
            'description': Textarea(attrs={'cols' : 20, 'rows' : 3}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'location')