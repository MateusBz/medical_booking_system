from django import forms

from .models import Visit, DoctorSchedule, DoctorVisitDateTime


class VisitCreateForm(forms.ModelForm):

    doctor = forms.ModelChoiceField(queryset=DoctorSchedule.objects.filter(
        occupied=False), label='Dostępne teminy wizyt')

    class Meta:
        model = Visit
        fields = ('doctor',)


class DoctorScheduleCreateForm(forms.ModelForm):

    date = forms.ModelChoiceField(queryset=DoctorVisitDateTime.objects.filter(
        occupied=False), label='Data')

    class Meta:
        model = DoctorSchedule
        fields = ('date',)
