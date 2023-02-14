"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """
    Manager for admin users.
    """

    def create_user(self, phone_number: str, password: str, **extra_fields):
        """
        Creates, saves and returns a new admin user.
        """
        if not phone_number:
            raise ValueError("User must have a phone number.")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number: str, password: str):
        """
        Creates, saves and returns a new super user.
        """
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system.
    """
    phone_number: str = models.CharField(
        verbose_name="phone number",
        max_length=12,
        unique=True,
        help_text="The user's phone number",
        error_messages={
            "unique": "The user with this phone number is already exist."
        }
    )
    email: str = models.EmailField(
        verbose_name="email",
        max_length=150,
        blank=True,
        help_text="The user's email"
    )
    first_name: str = models.CharField(
        verbose_name="first name",
        max_length=150,
        blank=True,
        help_text="The user's first name"
    )
    last_name: str = models.CharField(
        verbose_name="last name",
        max_length=150,
        blank=True,
        help_text="The user's last name"
    )
    is_active: bool = models.BooleanField(
        verbose_name="active",
        default=True,
        help_text="Designates whether this user should be treated as active.",
    )
    is_staff: bool = models.BooleanField(
        verbose_name="staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        verbose_name: str = "admin user"
        verbose_name_plural: str = "admin users"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.phone_number
