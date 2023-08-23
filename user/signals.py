from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.settings import AUTH_USER_MODEL
from referral_system.models import Invite
from referral_system.utils import create_invite_code
from user.models import User


@receiver(post_save, sender=AUTH_USER_MODEL)
def post_save_user(created, **kwargs):
    """Signal to create a user invite code when creating a user"""

    if created:
        user: User = kwargs.get('instance')
        referral_code = create_invite_code()
        invite = Invite.objects.create(invite_code=referral_code)
        user.invite_code = invite
        user.save()


