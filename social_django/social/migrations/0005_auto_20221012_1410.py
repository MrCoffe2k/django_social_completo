# Generated by Django 3.1.2 on 2022-10-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20221012_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
