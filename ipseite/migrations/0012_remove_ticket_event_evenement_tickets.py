# Generated by Django 4.2.5 on 2023-12-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipseite', '0011_remove_evenement_tickets_ticket_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='event',
        ),
        migrations.AddField(
            model_name='evenement',
            name='tickets',
            field=models.ManyToManyField(to='ipseite.ticket'),
        ),
    ]
