from django.db import models

from core.models import BaseModel

from .utils import CARD_SERIAL_LENGTH, generate_card_serial, validate_card_serial

# Create your models here.

class Card(BaseModel):
    """
        Model for gift card
    """
    # Explicitly declare status options to avoid typo
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    EXPIRED = 'EXPIRED'

    STATUS_CHOICES = (
        (ACTIVE,'Active'),
        (INACTIVE,'Inactive'),
        (EXPIRED, 'Expired')
    )
    serial = models.CharField(max_length=CARD_SERIAL_LENGTH, validators=[validate_card_serial],default=generate_card_serial, unique=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=ACTIVE)
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