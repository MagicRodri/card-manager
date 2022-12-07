# Create your tasks here
from celery import shared_task

from .models import Card


@shared_task
def add(x, y):
    return x + y

@shared_task
def set_card_expired(card_pk) -> None:

    card = Card.objects.get(pk=card_pk)
    card.status = card.EXPIRED
    card.is_active = False
    card.save()
