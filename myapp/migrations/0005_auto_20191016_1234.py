# Generated by Django 2.2.5 on 2019-10-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191015_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
