# Generated by Django 3.0.7 on 2020-09-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_cartitemmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemmodel',
            name='quantity',
            field=models.IntegerField(default=False),
        ),
    ]