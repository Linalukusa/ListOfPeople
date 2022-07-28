from django import forms
from .models import People

class PostForm(forms.ModelForm):
    class Meta:
         model= People
         fields = ('name',)





