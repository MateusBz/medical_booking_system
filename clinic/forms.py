from django import forms

from .models import Visit, DoctorSchedule


class VisitCreateForm(forms.ModelForm):
    
    doctor = forms.ModelChoiceField(queryset=DoctorSchedule.objects.filter(occupied=False))

    class Meta:
        model = Visit
        fields = ('doctor',)


class DoctorScheduleCreateForm(forms.ModelForm):
    
    class Meta:
        model = DoctorSchedule 
        fields = ('date', 'time',) 
