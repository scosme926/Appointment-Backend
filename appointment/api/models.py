from django.db import models

class Appointment(models.Model):
    services = models.TextField()
    date_time = models.DateTimeField()
