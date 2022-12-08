from django.contrib import admin

from .models import Card, Generator, Payment

# Register your models here.


admin.site.register(Card)
admin.site.register(Generator)
admin.site.register(Payment)