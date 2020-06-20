from django import forms

from .models import Visit, DoctorSchedule, DoctorVisitDate, DoctorVisitTime


class VisitCreateForm(forms.ModelForm):

    doctor = forms.ModelChoiceField(queryset=DoctorSchedule.objects.filter(
        occupied=False))

    class Meta:
        model = Visit
        fields = ('doctor',)


class DoctorScheduleCreateForm(forms.ModelForm):

    date = forms.ModelChoiceField(queryset=DoctorVisitDate.objects.filter(
        occupied=False))

    time = forms.ModelChoiceField(queryset=DoctorVisitTime.objects.filter(
        occupied=False))

    class Meta:
        model = DoctorSchedule
        fields = ('date', 'time',)
