# Generated by Django 2.2.12 on 2021-09-22 10:37

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Sezione_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='tab_1',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_2',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_3',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_4',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_5',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_6',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_7',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_8',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tab_9',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]