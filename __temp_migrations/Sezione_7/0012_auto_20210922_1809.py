# Generated by Django 2.2.12 on 2021-09-22 16:09

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Sezione_7', '0011_auto_20210922_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='qc1',
            field=otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', '6'], ['7', '']], max_length=10000, null=True, verbose_name=''),
        ),
    ]