from django.contrib import admin

from .models import Patient, DoctorSpeciality, Doctor, CustomUser

admin.site.register(Patient)
admin.site.register(DoctorSpeciality)
admin.site.register(Doctor)
admin.site.register(CustomUser)
