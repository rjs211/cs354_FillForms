# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-30 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duminfo', '0005_auto_20181130_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumuser',
            name='timeOfJoin',
            field=models.TimeField(null=True, verbose_name='Time of Joining '),
        ),
    ]