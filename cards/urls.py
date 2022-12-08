from django.urls import path

from .views import card_history, card_list, generator_create, payment_create

app_name = 'cards'
urlpatterns = [
    path('',card_list, name='card-list'),
    path('card/history/<str:pk>',card_history, name='card-history'),
    path('generator/create/',generator_create, name='generator-create'),
    path('payment/create/',payment_create, name='payment-create' ),
]
