# Generated by Django 3.2.6 on 2021-08-03 01:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
