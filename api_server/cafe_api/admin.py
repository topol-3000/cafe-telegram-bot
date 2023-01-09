from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    AdminUserCreationForm,
    AdminUserChangeForm,
    CustomerCreationForm,
    CustomerChangeForm,
    PaymentForm,
)
from .models.users import AdminUser, Customer
from .models.payment import Payment


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


class CustomerAdmin(admin.ModelAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = (
        "phone_number",
        "first_name",
        "last_name",
        "balance",
        "created_at",
        "updated_at",
    )
    list_filter = ("phone_number", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": (
            "phone_number",
            "first_name",
            "last_name",
        )}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    "phone_number",
                    "first_name",
                    "last_name",
                ),
            }
        ),
    )
    search_fields = ("phone_number", "first_name", "last_name")
    ordering = ("phone_number", "first_name", "last_name")


class PaymentAdmin(admin.ModelAdmin):
    add_form = PaymentForm
    form = PaymentForm
    model = Payment
    list_display = (
        "amount",
        "customer",
        "type",
        "status",
        "created_at",
    )
    list_filter = ("type", "status", "customer")
    fieldsets = (
        (None, {"fields": (
            "amount",
            "type",
            "status",
            "customer",
        )}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    "amount",
                    "type",
                    "status",
                    "customer",
                ),
            }
        ),
    )
    search_fields = ("type", "status", "customer")
    ordering = ("amount", "type", "status", "customer")


admin.site.register(AdminUser, CustomUserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
