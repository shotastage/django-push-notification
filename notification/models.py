from django.db import models
from notification.managers import (
    AppleNotificationDeviceManager
)
# Create your models here.


class NotificationQueue(models.Model):
    device_token = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    message = models.CharField(max_length = 255)


class AppleNotificationDevices(models.Model):
    
    IOS_VERSIONS = (
      (9, 'iOS9'),
      (10, 'iOS10'),
      (11, 'iOS11'),
      (12, 'iOS12'),
    )

    IOS_DEVICES = (
      ('se', 'iPhone SE'),
      ('6', 'iPhone 6'),
      ('6plus', 'iPhone 6 Plus'),
      ('7', 'iPhone 7'),
      ('7plus', 'iPhone 7 Plus'),
      ('8', 'iPhone 8'),
      ('8plus', 'iPhone 8 Plus'),
      ('x', 'iPhone X'),
      ('xr', 'iPhone XR'),
      ('xs', 'iPhone Xs'),
      ('xsm', 'iPhone Xs Max'),
    )

    token = models.CharField(max_length = 255)
    version = models.IntegerField(choices=IOS_VERSIONS)
    device = models.CharField(max_length = 10, choices=IOS_DEVICES)
    registered_at = models.DateTimeField()
    is_disabled = models.BooleanField(default=False)

    objects = AppleNotificationDeviceManager()


class AndroidNotificationDevices(models.Model):
    token = models.CharField(max_length = 255)
    version = models.CharField(max_length = 255)
    device = models.CharField(max_length = 255)
    registered_at = models.DateTimeField()
    is_disabled = models.BooleanField(default=False)
