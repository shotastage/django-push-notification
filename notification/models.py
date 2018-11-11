from django.db import models

# Create your models here.


class NotificationQueue(models.Model):
  device_token = models.CharField(max_length = 255)
  title = models.CharField(max_length = 255)
  message = models.CharField(max_length = 255)


class AppleNotificationDevices(models.Model):
  token = models.CharField(max_length = 255)
  version = models.CharField(max_length = 255)
  device = models.CharField(max_length = 255)
  registered_at = models.DateTimeField()
  is_disabled = models.BooleanField()


class AndroidNotificationDevices(models.Model):
  token = models.CharField(max_length = 255)
  version = models.CharField(max_length = 255)
  device = models.CharField(max_length = 255)
  registered_at = models.DateTimeField()
  is_disabled = models.BooleanField()
