from django.db.models import TextChoices
from django.core.exceptions import ValidationError
from cafe_api import models


class PaymentType(TextChoices):
    CASHBACK = "CASHBACK", "Cashback"
    CHARGE = "CHARGE", "Charge"


class PaymentStatus(TextChoices):
    REQUESTED = "REQUESTED", "Requested"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"


class Wallet:
    @staticmethod
    def update_balance(customer: models.Customer, payment_type: PaymentType, amount: float) -> None:
        if payment_type == PaymentType.CASHBACK:
            customer.balance += amount
        elif payment_type == PaymentType.CHARGE:
            customer.balance -= amount

        customer.save()
