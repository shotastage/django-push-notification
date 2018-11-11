from rest_framework import serializers
from notification.models import (
    AppleNotificationDevices,
    AndroidNotificationDevices,
)

class AppleNotificationDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppleNotificationDevices
        fields = ('token', 'version', 'device')


class AndroidNotificationDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidNotificationDevices
