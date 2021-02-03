# Generated by Django 3.1.5 on 2021-02-01 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteo', '0002_carton'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carton',
            name='celda00',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda01',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda02',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda10',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda11',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda12',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda20',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda21',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda22',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda30',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda31',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda32',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda40',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda41',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda42',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda50',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda51',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda52',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda60',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda61',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda62',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda70',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda71',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda72',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda80',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda81',
        ),
        migrations.RemoveField(
            model_name='carton',
            name='celda82',
        ),
        migrations.AddField(
            model_name='carton',
            name='fila10',
            field=models.CharField(default=1, max_length=2, verbose_name='fila10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila11',
            field=models.CharField(default=1, max_length=2, verbose_name='fila11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila12',
            field=models.CharField(default=1, max_length=2, verbose_name='fila12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila13',
            field=models.CharField(default=11, max_length=2, verbose_name='fila13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila14',
            field=models.CharField(default=1, max_length=2, verbose_name='fila14'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila20',
            field=models.CharField(default=1, max_length=2, verbose_name='fila20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila21',
            field=models.CharField(default=1, max_length=2, verbose_name='fila21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila22',
            field=models.CharField(default=1, max_length=2, verbose_name='fila22'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila23',
            field=models.CharField(default=1, max_length=2, verbose_name='fila23'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila24',
            field=models.CharField(default=1, max_length=2, verbose_name='fila24'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila30',
            field=models.CharField(default=1, max_length=2, verbose_name='fila30'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila31',
            field=models.CharField(default=1, max_length=2, verbose_name='fila31'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila32',
            field=models.CharField(default=1, max_length=2, verbose_name='fila32'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila33',
            field=models.CharField(default=1, max_length=2, verbose_name='fila34'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carton',
            name='fila34',
            field=models.CharField(default=1, max_length=2, verbose_name='fila34'),
            preserve_default=False,
        ),
    ]
