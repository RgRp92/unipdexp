# Generated by Django 2.2.12 on 2021-09-24 08:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Sezione_7', '0015_auto_20210923_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='businesstype',
            field=otree.db.models.StringField(choices=[['1', 'Specializzata in seminativi'], ['2', 'Mista colture'], ['3', 'Mista colture e allevamento']], max_length=10000, null=True, verbose_name='9. Tipologia azienda'),
        ),
    ]
