# Generated by Django 5.2.1 on 2025-05-26 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191011_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 10 digits', regex='^\\d{10}$')]),
        ),
    ]
