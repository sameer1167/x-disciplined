# Generated by Django 5.2 on 2025-04-15 15:25

import timezone_field.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Asia/Kolkata'),
        ),
    ]
