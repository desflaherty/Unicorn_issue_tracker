from django import forms
from .models import Bugs


class BugsForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ['name', 'description']
        

