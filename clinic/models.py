from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import Doctor, Patient


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=5)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.doctor.surname + ' ' + self.doctor.first_name +' '+ self.date.strftime("%Y-%m-%d") +' '+ self.time


class Visit(models.Model):
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    doctor = models.OneToOneField(DoctorSchedule, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("visit_detail", kwargs={"pk": self.pk})
    
    