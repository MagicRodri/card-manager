import uuid
from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q

from core.models import BaseModel

from .utils import CARD_NUMBER_LENGTH, generate_card_number, validate_card_number

# Create your models here.

class CardQuerySet(models.QuerySet):
    
    def search(self, query):
        """
            In order to be able to search any card queryset 
        """
        lookups = Q(serial__icontains=query) | Q(number__icontains=query) | Q(status__icontains=query) | Q(created_at__icontains=query)
        return self.filter(lookups)

class CardManager(models.Manager):

    def get_queryset(self):
        return CardQuerySet(model=self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query)

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

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        auto_created=True,
        unique=True
    )
    serial = models.CharField(max_length=16, default='ABC')
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

    objects = CardManager()

    def __str__(self) -> str:
        return self.number

    def can_activate(self):

        return self.status in (self.INACTIVE,self.EXPIRED)

    def can_deactivate(self):

        return not self.can_activate()

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

    def make_payment(self, payment):

        self.amount -= payment.price
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
    serial = models.CharField(max_length=16, default='gABC')
    validity_time = models.DurationField(default=A_MONTH, choices=VALIDITY_CHOICES)
    completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'quantity:{self.quantity}, validity:{self.validity_time}'


class Payment(BaseModel):

    price = models.DecimalField(decimal_places=2,max_digits=10, default=9.99 )
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='payments')
    comment = models.CharField(max_length=128, blank=True)

    def __str__(self) -> str:
        return f"{self.card}-{self.price}"