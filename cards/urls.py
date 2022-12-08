from django.urls import path

from .views import card_list, generator_create

app_name = 'cards'
urlpatterns = [
    path('',card_list, name='card-list'),
    path('generator/create/',generator_create, name='generator-create'),
]
