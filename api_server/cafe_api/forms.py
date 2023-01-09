from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, ValidationError

from .models.users import AdminUser, Customer
from .models.payment import Payment


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


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = (
            "amount",
            "type",
            "status",
            "customer",
        )
