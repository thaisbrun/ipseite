# Generated by Django 4.2.5 on 2024-01-11 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipseite', '0015_remove_evenement_tickets_evenement_nbplaces_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evenement',
            old_name='nbPlaces',
            new_name='nbTickets',
        ),
    ]
