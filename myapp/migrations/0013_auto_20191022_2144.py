# Generated by Django 2.2.5 on 2019-10-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_book_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='book',
            name='square',
            field=models.CharField(default=0, max_length=150),
        ),
    ]