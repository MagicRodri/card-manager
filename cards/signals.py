from django.db.models.signals import post_save

from .models import Card, Generator
from .tasks import generate_cards, set_card_expired


def card_post_save(instance, sender, created,*args, **kwargs):

    if created:
    
        set_card_expired.apply_async((instance.pk,), eta = instance.expired_at)


post_save.connect(card_post_save, sender=Card)


def generator_post_save(instance,created,*args, **kwargs):

    if created:
        generate_cards.delay(instance.pk)

post_save.connect(generator_post_save,sender=Generator)
