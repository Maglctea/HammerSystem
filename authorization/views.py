from datetime import timedelta

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
import time
import random

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import rest_framework.status
from authorization.models import AuthCode
from authorization.serializers import PhoneAuthSerializer, CodeAuthSerializer
from backend.settings import CODE_LIVE_HOURS
from user.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token



class SendPhone(CreateAPIView):
    """Class for viewing and creating users"""
    serializer_class = PhoneAuthSerializer
    queryset = AuthCode.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user, _ = User.objects.get_or_create(
                phone_number=serializer.data.get('phone_number')
            )

            time.sleep(4)
            code = random.randint(1000, 10000)
            AuthCode.objects.filter(user=user).delete()
            AuthCode.objects.create(user=user, code=code)

            return Response(data={'auth_code': code}, status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)


class SendCode(CreateAPIView):
    """Class for viewing and creating users"""
    serializer_class = CodeAuthSerializer
    queryset = AuthCode.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.data.get('phone_number')
            code = serializer.data.get('code')
            code_auth = AuthCode.objects.filter(user__phone_number=phone_number, code=code)
            if code_auth.exists():
                code_auth = code_auth.first()
                user = code_auth.user
                date = code_auth.created_at
                code_auth.delete()
                if date + timedelta(hours=CODE_LIVE_HOURS) > timezone.now():
                    token = Token.objects.get_or_create(user=user)

                    return Response(data={'token': token.key}, status=HTTP_200_OK)
                else:
                    return Response(data={'detail': 'Code is not valid'}, status=HTTP_400_BAD_REQUEST)
        return Response(data={'detail': 'incorrect code or phone number'}, status=HTTP_400_BAD_REQUEST)
