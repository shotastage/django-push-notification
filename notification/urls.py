from django.urls import path
from notification.views import (
    RegisterDeviceView,
)

urlpatterns = [
    path('device/token/', RegisterDeviceView.as_view(), name='starts'),
]
