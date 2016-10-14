from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.utils.timezone import utc

from rest_framework.response import Response
from rest_framework import status


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
            if not created:
                token.delete()
                token = Token.objects.create(user=serializer.validated_data['user'])
                token.save()
            return Response({"token":token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()

