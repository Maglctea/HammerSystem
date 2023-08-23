from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from authorization.models import AuthCode
from user.models import User
from user.serializers import UserSerializer


class PhoneAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone_number')


class CodeAuthSerializer(Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone_number = serializers.CharField(max_length=12)

    class Meta:
        fields = ('code', 'phone_number')
