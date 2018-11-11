from django.db import models


class AppleNotificationDeviceManager(models.Manager):

    def register(self, token, version, device):
        new = self.create(
            token = token,
            version = version,
            device = device,
        )

        return new


class AndroidNotificationDeviceManager(models.Manager):

    def register(self, token, version):
        new = self.create(
            token = token,
            version = version,
        )

        return new
