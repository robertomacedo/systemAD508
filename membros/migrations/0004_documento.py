# Generated by Django 3.1.5 on 2021-01-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0003_remove_cadmembro_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=20)),
                ('rg', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=20)),
                ('cnh', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
