# Generated by Django 3.1.5 on 2021-02-04 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartonazowebapp', '0002_auto_20210203_2104'),
        ('sorteo', '0004_auto_20210202_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='carton',
            name='participante',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='cartonazowebapp.usuario'),
            preserve_default=False,
        ),
    ]