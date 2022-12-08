from django.urls import path

from .views import (
    activate_card,
    card_history,
    card_list,
    deactivate_card,
    generator_create,
    payment_create,
)

app_name = 'cards'
urlpatterns = [
    path('',card_list, name='card-list'),
    path('card/activate/<str:pk>',activate_card, name='card-activate'),
    path('card/deactivate/<str:pk>',deactivate_card, name='card-deactivate'),
    path('card/history/<str:pk>',card_history, name='card-history'),
    path('generator/create/',generator_create, name='generator-create'),
    path('payment/create/',payment_create, name='payment-create' ),
]
