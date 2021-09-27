# Generated by Django 2.2.12 on 2021-09-22 14:43

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Sezione_7', '0003_player_year_azienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gender',
            field=otree.db.models.StringField(choices=[['1', 'M'], ['2', 'F']], max_length=10000, null=True, verbose_name='3. Genere'),
        ),
        migrations.AlterField(
            model_name='player',
            name='year_azienda',
            field=otree.db.models.IntegerField(null=True, verbose_name='2. Anno di insediamento aziendale'),
        ),
    ]
