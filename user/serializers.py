from rest_framework.serializers import ModelSerializer

from referral_system.models import Invite
from referral_system.serializers import InviteSerializer, InviterSerializer
from user.models import User


class UserSerializer(ModelSerializer):
    invite_code = InviteSerializer()
    inviter_code = InviterSerializer()

    class Meta:
        model = User
        fields = ('pk', 'phone_number', 'invite_code', 'inviter_code')
