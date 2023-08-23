from rest_framework.serializers import ModelSerializer
from referral_system.models import Invite
from user.models import User


class InvitesUsers(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'phone_number')


class InviteSerializer(ModelSerializer):
    """Serializer for view transactions"""
    invited_users = InvitesUsers(many=True)

    class Meta:
        model = Invite
        fields = ('pk', 'invite_code', 'invited_users')


class InviterSerializer(ModelSerializer):
    """Serializer for view transactions"""

    class Meta:
        model = Invite
        fields = ('pk', 'invite_code')


class InviteCodeSerializer(ModelSerializer):
    """Serializer for view transactions"""

    class Meta:
        model = Invite
        fields = ('invite_code',)
