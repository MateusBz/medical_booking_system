from django import forms

from .models import Visit


class VisitCreateForm(forms.ModelForm):
    
    class Meta:
        model = Visit
        fields = ['doctor', 'date', 'time']
