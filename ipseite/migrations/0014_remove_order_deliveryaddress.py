# Generated by Django 4.2.5 on 2024-01-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipseite', '0013_remove_cart_orderdate_remove_cart_ordered_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='deliveryAddress',
        ),
    ]
