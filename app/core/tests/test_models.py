"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """
    Test models.
    """

    def test_create_user_with_phone_number_successful(self):
        """
        Test creating a user with a phone number is successful.
        """
        phone_number: str = "+1234567890"
        password: str = "testpass123"
        user: models.User = get_user_model().objects.create_user(
            phone_number=phone_number,
            first_name="John",
            last_name="Doe",
            password=password,
        )

        self.assertEqual(user.phone_number, phone_number)
        self.assertEqual(user.full_name, "John Doe")
        self.assertTrue(user.check_password(password))

    def test_new_user_without_phone_number_raises_erro(self):
        """
        Test that creating a user without a phone number raises a ValuesError.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "testpass123")

    def test_create_superuser(self):
        """
        Test creating a superuser.
        """
        user: models.User = get_user_model().objects.create_superuser(
            phone_number="+1234567890",
            password="testpass123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
