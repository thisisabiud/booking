# Generated by Django 5.1.1 on 2024-10-30 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_booking_booking_date_booking_confirmation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
    ]
