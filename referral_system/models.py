from django.db import models
from user.models import User


class Invite(models.Model):
    """Invite model"""
    user_from = models.ForeignKey(User,
                                  verbose_name='Пригласивший',
                                  on_delete=models.CASCADE,
                                  related_name='invites_from')
    user_to = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   verbose_name='Приглашенный',
                                   related_name='invites_to'
                                   )

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

    def __str__(self):
        return f'{self.user_from.username} - {self.user_to.username}'
