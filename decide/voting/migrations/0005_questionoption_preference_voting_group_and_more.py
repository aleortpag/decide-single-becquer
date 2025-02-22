# Generated by Django 4.1 on 2023-12-17 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0002_censusgroup'),
        ('voting', '0004_alter_voting_postproc_alter_voting_tally'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoption',
            name='preference',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='voting',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votings', to='census.censusgroup'),
        ),
        migrations.AddField(
            model_name='voting',
            name='voting_type',
            field=models.CharField(choices=[('preference', 'Preference-Based Voting'), ('normal', 'Normal voting')], default='normal', max_length=15),
        ),
    ]
