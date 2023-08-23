from django.contrib import admin

from authorization.models import AuthCode


# Register your models here.
@admin.register(AuthCode)
class AuthCodeAdmin(admin.ModelAdmin):
    """Class for viewing users in admin panel"""

    list_display = ('pk', 'user', 'code', 'created_at')
    ordering = ('created_at',)
    list_per_page = 30
    search_fields = ('pk', 'code')
    list_display_links = ('pk', 'code')