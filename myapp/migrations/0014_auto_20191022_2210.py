# Generated by Django 2.2.5 on 2019-10-23 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20191022_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cost',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='square',
            new_name='sqft',
        ),
    ]
