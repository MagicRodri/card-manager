# Generated by Django 4.1.4 on 2022-12-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_card_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='last_used',
            field=models.DateTimeField(auto_now=True),
        ),
    ]