# Generated by Django 2.2.5 on 2019-10-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20191021_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='SOME STRING', max_length=300),
        ),
    ]
