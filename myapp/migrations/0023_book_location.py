# Generated by Django 2.2.5 on 2019-10-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20191022_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.CharField(default='address', max_length=255),
        ),
    ]
