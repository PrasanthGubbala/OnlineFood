# Generated by Django 3.0.7 on 2020-09-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20200925_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='items',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='status',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='c_id',
            field=models.ManyToManyField(to='customer.CartItemModel'),
        ),
    ]