# Generated by Django 4.1 on 2023-11-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='default_username', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
