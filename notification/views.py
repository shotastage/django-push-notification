from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from mirageframework.views import CURDView, CREATE
from rest_framework.response import Response
from django.contrib.auth.models import User

from notification.models import (
    AppleNotificationDevices,
    AndroidNotificationDevices
)

from notification.serializers import (
    AppleNotificationDevicesSerializer,
    AndroidNotificationDevicesSerializer,
)


class RegisterDeviceView(CURDView):
    """
    View to register device to send notification or manage device session.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    def post(self, request, format = None) -> Response:
        """
        Return a status message or registering a new device.
        """

        return CREATE(request, AppleNotificationDevicesSerializer)
