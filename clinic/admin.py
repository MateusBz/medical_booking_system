from django.contrib import admin
from .models import Visit, DoctorSchedule, DoctorVisitDateTime


admin.site.register(Visit)
admin.site.register(DoctorSchedule)
admin.site.register(DoctorVisitDateTime)

