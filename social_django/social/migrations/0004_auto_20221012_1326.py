# Generated by Django 3.1.2 on 2022-10-12 18:26

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20221012_1324'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='paciente',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
