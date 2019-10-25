# Generated by Django 2.2.5 on 2019-10-23 01:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20191022_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bedrooms',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]