# Generated by Django 3.1.3 on 2020-11-16 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_total_matches'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-points', '-nrr']},
        ),
    ]
