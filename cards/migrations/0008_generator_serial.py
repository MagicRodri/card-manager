# Generated by Django 4.1.4 on 2022-12-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_card_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generator',
            name='serial',
            field=models.CharField(default='gABC', max_length=16),
        ),
    ]
