from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models.users import AdminUser


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
