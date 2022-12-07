import uuid
from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models

from core.models import BaseModel

from .utils import CARD_NUMBER_LENGTH, generate_card_number, validate_card_number

# Create your models here.

class Card(BaseModel):
    """
        Model for gift card
    """
    # Explicitly declare status options to avoid typo when accessing choices
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    EXPIRED = 'EXPIRED'

    STATUS_CHOICES = (
        (ACTIVE,'Active'),
        (INACTIVE,'Inactive'),
        (EXPIRED, 'Expired')
    )

    serial = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        auto_created=True,
        unique=True
    )

    number = models.CharField(
        max_length=CARD_NUMBER_LENGTH,
        validators=[validate_card_number],
        default=generate_card_number,
        unique=True
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=100.00,
        validators=[MinValueValidator(0.00, message='Amount must be greater or equal to 0')]
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=ACTIVE)
    last_used = models.DateTimeField(auto_now=True)
    expired_at = models.DateTimeField()


    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.status = self.INACTIVE
            self.save()

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.status = self.ACTIVE
            self.save()


class Generator(BaseModel):
    """
        Model for auto cards generation
    """

    A_MINUTE = timedelta(minutes=1)
    A_MONTH = timedelta(days=30)
    SIX_MONTHS = timedelta(days=30*6)
    A_YEAR = timedelta(days=30*12)

    VALIDITY_CHOICES = (
        (A_MINUTE,'A minute(for testing)'),
        (A_MONTH,'A month'),
        (SIX_MONTHS,'Six months'),
        (A_YEAR,'A year')
    )
    quantity = models.PositiveIntegerField(default=1)
    validity_time = models.DurationField(default=A_MONTH, choices=VALIDITY_CHOICES)
    completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'quantity:{self.quantity}, validity:{self.validity_time}'