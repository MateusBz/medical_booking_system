from datetime import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    pesel_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
    phone = models.CharField(max_length=20)
    day_of_birth = models.DateField(blank=True, null=True)
    GENDER = (
        ('M', 'Mężczyzna'),
        ('W', 'Kobieta'),
        ('NN', 'Odmowa'),
    )
    gender = models.CharField(max_length=2, choices=GENDER)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.surname

    @property
    def compute_age(self):
        return int((datetime.now().date() - self.day_of_birth).days / 365.25)


class DoctorSpeciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    medical_licence = models.CharField(max_length=7)
    is_active = models.BooleanField(default=False)
    speciality = models.ManyToManyField(DoctorSpeciality)

    def __str__(self):
        return self.first_name + ' ' + self.surname
