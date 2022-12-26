from django.db.models import Model, DateTimeField
from django.utils import timezone


class TimestampMixin(Model):
    created_at: DateTimeField = DateTimeField(
        "created at",
        default=timezone.now,
        help_text="Specifies when the entity was created."
    )
    updated_at: DateTimeField = DateTimeField(
        "updated at",
        default=timezone.now,
        help_text="Specifies when the entity was updated."
    )

    class Meta:
        abstract = True
