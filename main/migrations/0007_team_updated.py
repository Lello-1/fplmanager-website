# Generated by Django 2.2.5 on 2019-10-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]