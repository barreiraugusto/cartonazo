# Generated by Django 3.1.5 on 2021-02-04 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorteo', '0004_auto_20210202_1051'),
        ('cartonazowebapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]
