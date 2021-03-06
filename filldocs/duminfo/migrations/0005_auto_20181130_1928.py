# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-30 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duminfo', '0004_auto_20181130_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dumuser',
            old_name='HadLn1',
            new_name='HAdLn1',
        ),
        migrations.RenameField(
            model_name='dumuser',
            old_name='HadLn2',
            new_name='HAdLn2',
        ),
        migrations.RenameField(
            model_name='dumuser',
            old_name='HadLn3',
            new_name='HAdLn3',
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='TodayDate',
            field=models.DateField(null=True, verbose_name='Today Date '),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='dept',
            field=models.CharField(help_text='dept/center/section', max_length=40, null=True, verbose_name='Department '),
        ),
    ]
