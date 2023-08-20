from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    objects = UserManager()
    phone_number = models.CharField(_('phone_number'), max_length=15, unique=True)
    username = models.CharField(_("username"), max_length=150, unique=True)
    invite_code = models.CharField(_("invite code"), max_length=6, unique=True, blank=True, null=True)
    password = models.CharField(_("password"), max_length=128, blank=True, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('phone_number',)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
