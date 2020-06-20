from django.contrib import admin
from .models import Visit, DoctorSchedule, DoctorVisitDate, DoctorVisitTime


admin.site.register(Visit)
admin.site.register(DoctorSchedule)
admin.site.register(DoctorVisitDate)
admin.site.register(DoctorVisitTime)
