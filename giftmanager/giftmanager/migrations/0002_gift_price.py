# Generated by Django 3.0 on 2019-12-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]