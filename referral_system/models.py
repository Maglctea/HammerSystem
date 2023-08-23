from django.db import models
from django.utils.translation import gettext_lazy as _


class Invite(models.Model):
    """Invite model"""

    invite_code = models.CharField(_("invite code"), max_length=6, null=True)

    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'

    def __str__(self):
        return f'{self.invite_code}'
