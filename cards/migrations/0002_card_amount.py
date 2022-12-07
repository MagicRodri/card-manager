# Generated by Django 4.1.4 on 2022-12-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]
