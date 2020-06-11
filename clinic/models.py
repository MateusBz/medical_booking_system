from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import Doctor, Patient


class Visit(models.Model):
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    DATE = (
        ('11.06', '11.06'),
        ('12.06', '12.06')
    )
    date = models.CharField(max_length=5, choices=DATE)
    TIMES = (
        ('13:00', '13:00'),
        ('13:30', '13.30'),
        ('14:00', '14:00')
    )
    time = models.CharField(max_length=5, choices=TIMES)

    

    def get_absolute_url(self):
        return reverse("visit_detail", kwargs={"pk": self.pk})
    
    
