# Generated by Django 4.1.4 on 2022-12-07 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_card_last_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('validity_time', models.DurationField(choices=[(datetime.timedelta(seconds=60), 'A minute(for testing)'), (datetime.timedelta(days=30), 'A month'), (datetime.timedelta(days=180), 'Six months'), (datetime.timedelta(days=360), 'A year')], default=datetime.timedelta(days=30))),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
