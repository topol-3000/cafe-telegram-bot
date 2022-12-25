from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class AdminUserManager(BaseUserManager):
    def _create_user(self, phone_number: str, password: str, **extra_fields) -> AbstractBaseUser:
        if not phone_number:
            raise ValueError("The phone number must be set.")

        user = self.model(phone_number=phone_number, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, phone_number: str, password: str, **extra_fields) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number: str, password: str, **extra_fields) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)
