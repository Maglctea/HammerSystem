from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status


from authorization.models import AuthCode
from referral_system.models import Invite
from referral_system.serializers import InviteCodeSerializer
from user.models import User
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserProfile(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return UserSerializer
    #     # elif self.request.method == 'POST':
    #     return InviteCodeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.serializer_class = UserSerializer
        elif self.request.method == 'POST':
            self.serializer_class = InviteCodeSerializer

    def get(self, request, *args, **kwargs):
        self.get_serializer_class()
        # self.serializer_class = UserSerializer
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        self.get_serializer_class()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            invite_code = serializer.data.get('invite_code')
            invite = Invite.objects.filter(invite_code=invite_code).first()
            if invite:
                if user.inviter_code is None:
                    user.inviter_code = invite
                    user.save()
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(data={'detail': 'The activation code already exists'}, status=status.HTTP_403_FORBIDDEN)
            return Response(data={'detail': 'Invite code not found'}, status=status.HTTP_403_FORBIDDEN)
        return Response(data={'detail': 'invalid data'}, status=status.HTTP_403_FORBIDDEN)
