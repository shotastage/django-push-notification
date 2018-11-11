from django.db import models


class AppleNotificationDeviceManager(models.Manager):

    def register(self, token, version, device):
        new = self.create(
            token = token,
            version = version,
            device = device,
        )

        return new
