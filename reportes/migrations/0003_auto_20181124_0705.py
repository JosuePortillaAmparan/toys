# Generated by Django 2.1 on 2018-11-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_auto_20181124_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos_indiv',
            name='movilidad',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='productos_indiv',
            name='presentacion',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='productos_indiv',
            name='tamaño',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
