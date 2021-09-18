from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from simple_history.admin import SimpleHistoryAdmin

from .models import CustomUser, Favorites


class UserAdmin(BaseUserAdmin, SimpleHistoryAdmin):
    ordering = ["id"]
    list_display = ["username", "email"]
    fieldsets = (
        (
            None,
            {
                "fields": ("email", "password"),
            },
        ),
        (_("Personal Info"), {"fields": ("username",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Favorites, SimpleHistoryAdmin)

admin.site.site_header = "LoR"
admin.site.site_title = "LoR Official"
admin.site.index_title = "dashboard"
