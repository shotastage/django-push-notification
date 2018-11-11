from datetime import datetime
from django.db import models
from notification.managers import (
    AppleNotificationDeviceManager,
    AndroidNotificationDeviceManager,
)


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
    registered_at = models.DateTimeField(default=datetime.now)
    is_disabled = models.BooleanField(default=False)

    objects = AppleNotificationDeviceManager()


class AndroidNotificationDevices(models.Model):

    ANDROID_VERSIONS = (
      ('2.3', 'Gingerbread'),
      ('3.0', 'Honeycomb'),
      ('4.0', 'Ice Cream Sandwich'),
      ('4.1', 'Jelly Bean'),
      ('4.4', 'Kit Kat'),
      ('5.0', 'Lollipop'),
      ('6.0', 'Marshmallow'),
      ('7.0', 'Nougat'),
      ('8.0', 'Oreo'),
      ('9.0', 'Pie'),
    )

    token = models.CharField(max_length = 255)
    version = models.CharField(max_length = 10, choices=ANDROID_VERSIONS)
    registered_at = models.DateTimeField(default=datetime.now)
    is_disabled = models.BooleanField(default=False)

    objects = AndroidNotificationDeviceManager()
