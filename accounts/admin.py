from django.contrib import admin

from .models import Patient, DoctorSpeciality, Doctor

admin.site.register(Patient)
admin.site.register(DoctorSpeciality)
admin.site.register(Doctor)
