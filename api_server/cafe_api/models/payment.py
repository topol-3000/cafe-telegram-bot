from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone

from cafe_api.services import wallet_service


class Payment(models.Model):
    amount: models.FloatField = models.FloatField(
        verbose_name="amount",
        default=0.0,
        validators=[MinValueValidator(0.00)],
        help_text="Specifies the amount of the payment.",
    )
    type: models.CharField = models.CharField(
        verbose_name="type",
        choices=wallet_service.PaymentType.choices,
        default=wallet_service.PaymentType.CASHBACK,
        max_length=10,
        help_text="Specifies the type of the payment.",
    )
    status: models.CharField = models.CharField(
        verbose_name="status",
        choices=wallet_service.PaymentStatus.choices,
        default=wallet_service.PaymentStatus.REQUESTED,
        max_length=10,
        help_text="Specifies the status of the payment.",
    )
    customer: models.ForeignKey = models.ForeignKey(
        to="cafe_api.Customer",
        verbose_name="customer",
        related_name="payments",
        on_delete=models.CASCADE,
    )
    created_at: models.DateTimeField = models.DateTimeField(
        verbose_name="created at",
        default=timezone.now,
        help_text="Specifies when the customer was created."
    )

    def is_payment_amount_valid(self) -> bool:
        if self.type == wallet_service.PaymentType.CASHBACK:
            return True
        elif self.type == wallet_service.PaymentType.CHARGE:
            return self.amount <= self.customer.balance
        else:
            return False

    def clean(self):
        if self.is_payment_amount_valid():
            wallet_service.Wallet.update_balance(self.customer, self.type, self.amount)
        else:
            raise ValidationError("Customer's balance is less than payment amount.")

    def __str__(self) -> str:
        return f"{self.amount} UAH ({self.customer.full_name})"
