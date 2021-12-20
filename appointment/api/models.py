from django.db import models

class Appointment(models.Model):
    services = models.TextField()
    date_time = models.DateTimeField()
    PENDING = 'PE'
    ACCEPTED = 'AC'
    REJECTED = 'RE'
    DECISION_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
    decision = models.CharField(
        max_length=2,
        choices=DECISION_CHOICES,
        default=PENDING,
    )
