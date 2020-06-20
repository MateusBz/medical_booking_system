from django import forms

from .models import Visit, DoctorSchedule


class VisitCreateForm(forms.ModelForm):
    
    doctor = forms.ModelChoiceField(queryset=DoctorSchedule.objects.filter(occupied=False))

    class Meta:
        model = Visit
        fields = ('doctor',)


class DoctorScheduleCreateForm(forms.ModelForm):
    
    DATES = (
        ('2020-06-22', '2020-06-22'),
        ('2020-06-23', '2020-06-23'),
        ('2020-06-24', '2020-06-24'),
    )
    date = forms.ChoiceField(choices=DATES)
    HOURS = (
        ('8:00', '8:00'),
        ('8:30', '8:30'),
        ('9:00', '9:00'),
        ('9:30', '9:30'),
        ('10:30', '10:30'),
    )
    time = forms.ChoiceField(choices=HOURS)

    class Meta:
        model = DoctorSchedule 
        fields = ('date', 'time',) 
