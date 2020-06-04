from django.contrib import admin

from .models import Patient, DoctorSpeciality

admin.site.register(Patient)
admin.site.register(DoctorSpeciality)
