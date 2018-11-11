from django.contrib import admin
from notification.models import (
    NotificationQueue,
    AppleNotificationDevices
)
# Register your models here.

admin.site.register(NotificationQueue)
admin.site.register(AppleNotificationDevices)
