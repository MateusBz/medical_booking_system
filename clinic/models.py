from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import Doctor, Patient


class DoctorVisitDate(models.Model):
    date = models.DateField()
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")


class DoctorVisitTime(models.Model):
    HOURS = (
        ('8:00', '8:00'),
        ('8:30', '8:30'),
        ('9:00', '9:00'),
        ('9:30', '9:30'),
        ('10:30', '10:30'),
    )
    time = models.CharField(max_length=5, choices=HOURS)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.time


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.ForeignKey(DoctorVisitDate, on_delete=models.CASCADE)
    time = models.ForeignKey(DoctorVisitTime, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        speciality = ''
        for sp in self.doctor.speciality.all():
            speciality = speciality + str(sp) + ', '
        return speciality + ' ' + self.doctor.first_name + ' ' + self.doctor.surname +' '+ self.date.date.strftime("%d/%m/%Y")+' '+ self.time.time

    def get_absolute_url(self):
        return reverse("doctor_schedule_detail", kwargs={"pk": self.pk})


class Visit(models.Model):
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    doctor = models.OneToOneField(DoctorSchedule, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("visit_detail", kwargs={"pk": self.pk})
    
    