# Generated by Django 5.1.4 on 2024-12-30 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_remove_booth_reserved_by_alter_booth_booth_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibitors', to='reservations.contact')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibitors', to='reservations.event')),
            ],
            options={
                'verbose_name': 'Exhibitor',
                'verbose_name_plural': 'Exhibitors',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['event', 'company'], name='reservation_event_i_f08520_idx')],
                'unique_together': {('event', 'company', 'name')},
            },
        ),
    ]