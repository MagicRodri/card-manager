# Generated by Django 4.1.4 on 2022-12-07 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0, message='Amount must be greater or equal to 0')]),
        ),
    ]