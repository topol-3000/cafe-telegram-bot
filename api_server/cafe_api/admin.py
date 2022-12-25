from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AdminUserCreationForm, AdminUserChangeForm
from .models.users import AdminUser


class CustomUserAdmin(UserAdmin):
    add_form = AdminUserCreationForm
    form = AdminUserChangeForm
    model = AdminUser
    list_display = ("phone_number", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("phone_number", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": (
            "phone_number",
            "first_name",
            "last_name",
            "email",
        )}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            }
        ),
    )
    search_fields = ("phone_number", "first_name", "last_name")
    ordering = ("phone_number", "first_name", "last_name")


admin.site.register(AdminUser, CustomUserAdmin)
