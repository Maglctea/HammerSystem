from django.apps import AppConfig


class ReferralSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'referral_system'
    verbose_name = "Приглашения"

    def ready(self):
        import user.signals