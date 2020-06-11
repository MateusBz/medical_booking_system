from django.db import models
from accounts.models import Doctor


class Office(models.Model):
    name = models.CharField(max_length=20)
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
    occupied = models.BooleanField(default=False)


    def __str__(self):
        return self.name + ' ' + self.time + ' ' + self.doctor.surname
        
    
