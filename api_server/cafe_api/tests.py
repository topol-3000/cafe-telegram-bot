from django.contrib.auth import get_user_model
from django.test import TestCase

from .models.users import AdminUser


class UsersManagersTests(TestCase):
    test_user_phone: str = '1234567890'
    test_user_password: str = 'p@ssWord!'

    def test_create_user(self):
        AdminUserModel = get_user_model()
        user: AdminUser = AdminUserModel.objects.create_user(
            phone_number=self.test_user_phone,
            password=self.test_user_password
        )

        self.assertEqual(user.phone_number, self.test_user_phone)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        AdminUserModel = get_user_model()
        admin_user: AdminUser = AdminUserModel.objects.create_superuser(
            phone_number=self.test_user_phone,
            password=self.test_user_password
        )

        self.assertEqual(admin_user.phone_number, self.test_user_phone)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            AdminUserModel.objects.create_superuser(
                phone_number=self.test_user_phone,
                password=self.test_user_password,
                is_superuser=False,
            )
