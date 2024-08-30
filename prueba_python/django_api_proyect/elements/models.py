
from django.db import models
from django.utils import timezone

class MedicalImageResult(models.Model):
    device_name = models.CharField(max_length=100, default="Unknown Device")
    average_before_normalization = models.FloatField(default=0.0)
    average_after_normalization = models.FloatField(default=0.0)
    data_size = models.IntegerField(default=0)
    raw_data = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)  # Cambia auto_now_add=True a default=timezone.now
    updated_at = models.DateTimeField(default=timezone.now)  # Cambia auto_now=True a default=timezone.now

    def __str__(self):
        return self.device_name
