# Generated by Django 2.2.5 on 2020-01-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_player_team_name_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='kpi',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='price_change',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='top_50_count',
            field=models.IntegerField(default=0),
        ),
    ]