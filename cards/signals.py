from django.db.models.signals import post_save

from .models import Card
from .tasks import set_card_expired


def card_post_save(instance, sender, created,*args, **kwargs):

    if created:
    
        set_card_expired.apply_async((instance.pk,), eta = instance.expired_at)


post_save.connect(card_post_save, sender=Card)
