# Generated by Django 4.2.5 on 2023-11-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipseite', '0002_concert_tour_alter_artist_activation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
