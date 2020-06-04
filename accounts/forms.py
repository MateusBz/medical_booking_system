from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Patient, Doctor, DoctorSpeciality, CustomUser


class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Imię')
    surname = forms.CharField(max_length=100, label='Nazwisko')
    pesel_number = forms.IntegerField(label='Numer PESEL')
    phone = forms.IntegerField(label='Telefon')
    age = forms.IntegerField(label='Wiek')
    day_of_birth = forms.DateField(label='Data Urodzenia')
    GENDER = (
        ('M', 'Mężczyzna'),
        ('W', 'Kobieta'),
        ('NN', 'Odmowa'),
    )
    gender = forms.ChoiceField(choices=GENDER, label='Þłeć')
    street = forms.CharField(label='Ulica')
    house_number = forms.CharField(label='Numer domu')
    flat_number = forms.CharField(label='Numer mieszkania')
    zip_code = forms.CharField(label='Kod pocztowy')
    city = forms.CharField(label='Miasto')

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.first_name = self.cleaned_data.get('first_name')
        patient.surname = self.cleaned_data.get('surname')
        patient.pesel_number = self.cleaned_data.get('pesel_number')
        patient.phone = self.cleaned_data.get('phone')
        patient.age = self.cleaned_data.get('age')
        patient.day_of_birth = self.cleaned_data.get('day_of_birth')
        patient.gender = self.cleaned_data.get('gender')
        patient.street = self.cleaned_data.get('street')
        patient.house_number = self.cleaned_data.get('house_number')
        patient.flat_number = self.cleaned_data.get('flat_number')
        patient.zip_code = self.cleaned_data.get('zip_code')
        patient.city = self.cleaned_data.get('city')
        patient.save()
        return user


class DoctorSpecialityForm(forms.Form):
    speciality = forms.CharField(max_length=150)

    class Meta:
        model = DoctorSpeciality


class DoctorCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Imię')
    surname = forms.CharField(max_length=150, label='Nazwisko')
    phone = forms.IntegerField(label='Telefon')
    speciality = forms.ModelMultipleChoiceField(
        queryset=DoctorSpeciality.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True, label='Specjalizacja'
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.first_name = self.cleaned_data.get('first_name')
        doctor.surname = self.cleaned_data.get('surname')
        doctor.phone = self.cleaned_data.get('phone')
        doctor.speciality.add(*self.cleaned_data.get('speciality'))
        return user

