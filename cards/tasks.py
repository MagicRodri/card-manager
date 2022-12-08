# Create your tasks here
from datetime import datetime

from celery import shared_task

from .models import Card, Generator


@shared_task
def add(x, y):
    return x + y

@shared_task
def set_card_expired(card_pk) -> None:

    card = Card.objects.get(pk=card_pk)
    card.status = card.EXPIRED
    card.is_active = False
    card.save()

@shared_task
def generate_cards(generator_pk) ->None:

    generator = Generator.objects.get(pk=generator_pk)
    for _ in range(generator.quantity):
        Card.objects.create(serial=generator.serial,expired_at = datetime.utcnow() + generator.validity_time )

    generator.completed = True
    generator.save()