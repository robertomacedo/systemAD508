# Generated by Django 3.1.5 on 2021-01-24 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0002_auto_20210124_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadmembro',
            name='cpf',
        ),
    ]
