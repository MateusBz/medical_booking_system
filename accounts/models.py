from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    pesel_number = models.CharField(max_length=11)
    phone = PhoneNumberField(max_length=15)
    day_of_birth = models.DateField(blank=True, null=True)
    GENDER = (
        ('M', 'Mężczyzna'),
        ('W', 'Kobieta'),
        ('NN', 'Odmowa'),
    )
    gender = models.CharField(max_length=2, choices=GENDER)
    street = models.CharField(max_length=80)
    house_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=80)

    def __str__(self):
        return self.first_name + ' ' + self.surname

    @property
    def compute_age(self):
        today = date.today()
        return (today.year - self.day_of_birth.year)
        


class DoctorSpeciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = PhoneNumberField(max_length=15)
    medical_licence = models.CharField(max_length=7)
    is_active = models.BooleanField(default=False)
    speciality = models.ManyToManyField(DoctorSpeciality)

    def __str__(self):
        return self.first_name + ' ' + self.surname
