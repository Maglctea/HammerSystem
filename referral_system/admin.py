from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Class for viewing users in admin panel"""

    list_display = ('pk', 'username', 'invite_code', 'is_superuser', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    ordering = ('username',)
    list_per_page = 30
    search_fields = ('user', 'username')
    list_display_links = ('username',)