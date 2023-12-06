# Generated by Django 4.2.5 on 2023-12-06 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipseite', '0005_festival_description_ticket_emplacement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='name',
            field=models.CharField(default='festoche', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ipseite.evenement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
