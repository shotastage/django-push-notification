from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


from notification.models import (
    AppleNotificationDevices,
    AndroidNotificationDevices
)


class RegisterDeviceView(APIView):
    """
    View to register device to send notification or manage device session.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, format = None) -> Response:
        """
        Return a status message or registering a new device.
        """
        pass
