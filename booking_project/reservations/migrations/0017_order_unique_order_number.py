# Generated by Django 5.1.4 on 2025-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0016_rename_order_id_order_order_number'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='order',
            constraint=models.UniqueConstraint(fields=('order_number',), name='unique_order_number'),
        ),
    ]