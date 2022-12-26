from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, BooleanField, EmailField

from cafe_api.managers import AdminUserManager
from .mixins import TimestampMixin


class AdminUser(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    phone_number: CharField = CharField(
        "phone number",
        max_length=12,
        unique=True,
        help_text="The user's phone number",
        error_messages={
            "unique": "A user with that phone number already exists.",
        },
    )
    first_name = CharField(
        "first name",
        max_length=150,
        blank=True,
        help_text="The user's first name",
    )
    last_name = CharField(
        "last name",
        max_length=150,
        blank=True,
        help_text="The user's last name",
    )
    email = EmailField(
        "email",
        max_length=150,
        blank=True,
        help_text="The user's last email",
    )
    is_staff = BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active.",
    )

    objects = AdminUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "admin user"
        verbose_name_plural = "admin users"

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.phone_number
