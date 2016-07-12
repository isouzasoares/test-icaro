# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20160712_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instance',
            name='amount_of_cpu',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='CPUs'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='amount_of_hd',
            field=models.FloatField(verbose_name='Hd (GB)'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='amount_of_memory',
            field=models.FloatField(verbose_name='Memory (GB)'),
        ),
    ]
