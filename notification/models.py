from django.db import models

# Create your models here.


class NotificationQueue(models.Model):
  device_token = models.CharField(max_length = 255)
  title = models.CharField(max_length = 255)
  message = models.CharField(max_length = 255)
