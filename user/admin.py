from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Class for viewing users in admin panel"""

    list_display = ('pk', 'phone_number', 'invite_code', 'inviter_code', 'is_superuser', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    ordering = ('phone_number',)
    list_per_page = 30
    search_fields = ('pk', 'phone_number')
    list_display_links = ('phone_number',)
