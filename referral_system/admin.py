from django.contrib import admin
from referral_system.models import Invite


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    """Class for viewing invitations in admin panel"""

    list_display = ('pk', 'invite_code')
    list_filter = ('invite_code',)
    ordering = ('pk', 'invite_code')
    list_per_page = 30
    search_fields = ('pk', 'invite_code')
    list_display_links = ('pk', 'invite_code')