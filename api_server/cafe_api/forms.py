from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models.users import AdminUser, Customer


class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = AdminUser
        fields = (
            "first_name",
            "last_name",
            "password",
            "email",
        )


class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = AdminUser
        fields = (
            "first_name",
            "last_name",
            "password",
            "email",
        )


class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "phone_number",
        )


class CustomerChangeForm(ModelForm):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "phone_number",
        )
