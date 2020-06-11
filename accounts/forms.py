from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Patient, Doctor, DoctorSpeciality, CustomUser


class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=80, label='Imię')
    surname = forms.CharField(max_length=80, label='Nazwisko')
    email = forms.EmailField(label='Email', max_length=80)
    pesel_number = forms.CharField(label='Numer PESEL', widget= forms.TextInput(attrs={'pattern': '\d*', 'maxlength': 11}))
    phone = PhoneNumberField(label='Telefon', max_length=15)
    day_of_birth = forms.DateField(
        label='Data Urodzenia', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),  error_messages={'invalid': 'Niepoprawna nazwa'})
    GENDER = (
        ('M', 'Mężczyzna'),
        ('W', 'Kobieta'),
        ('NN', 'Odmowa'),
    )
    gender = forms.ChoiceField(choices=GENDER, label='Płeć')
    street = forms.CharField(label='Ulica', max_length=80)
    house_number = forms.CharField(label='Numer domu', max_length=10)
    flat_number = forms.CharField(label='Numer mieszkania', required=False, max_length=10)
    zip_code = forms.CharField(label='Kod pocztowy', max_length=6)
    city=forms.CharField(label = 'Miasto', max_length=80)

    class Meta(UserCreationForm.Meta):
        model=CustomUser

    def __init__(self, *args, **kwargs):
        super(PatientSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text=None
        
        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Potwierdź hasło'

        


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
    speciality = forms.CharField(max_length=100)

    class Meta:
        model = DoctorSpeciality


class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=80, label='Imię')
    surname = forms.CharField(max_length=80, label='Nazwisko')
    email = forms.EmailField(label='Email', max_length=80)
    phone = PhoneNumberField(label='Telefon', max_length=15)
    medical_licence = forms.CharField(label='PWZ', widget=forms.TextInput(
        attrs={'pattern': '\d*', 'maxlength': 7}))
    speciality = forms.ModelMultipleChoiceField(
        queryset=DoctorSpeciality.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True, label='Specjalizacja'
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super(DoctorSignUpForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Potwierdź hasło'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.first_name = self.cleaned_data.get('first_name')
        doctor.surname = self.cleaned_data.get('surname')
        doctor.email = self.cleaned_data.get('email')
        doctor.phone = self.cleaned_data.get('phone')
        doctor.medical_licence = self.cleaned_data.get('medical_licence')
        doctor.speciality.add(*self.cleaned_data.get('speciality'))
        doctor.save()
        return user

