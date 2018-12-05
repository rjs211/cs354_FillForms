# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-01 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duminfo', '0009_auto_20181201_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumuser',
            name='FName',
            field=models.CharField(max_length=20, null=True, verbose_name='your First Name'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='LName',
            field=models.CharField(max_length=20, null=True, verbose_name='your Last Name'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='PakAdL1',
            field=models.CharField(blank=True, help_text='If originally a resident of Pakistan, the address in that Country and the date of migration to Indian Union.', max_length=100, null=True, verbose_name='Pakisthan Adddress if Any line 1'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='PakAdL2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Pakisthan Adddress 2'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='PakAdL3',
            field=models.CharField(blank=True, help_text='Village, Thana and District', max_length=100, null=True, verbose_name='Pakisthan Adddress if Any line 13'),
        ),
        migrations.AlterField(
            model_name='dumuser',
            name='crimeDesc',
            field=models.CharField(default='No', help_text='If the answer to any of above mentioned question is ‘Yes’, give full particulars of the case / arrest/ detention/ fine/ conviction/ sentence/ punishment etc. and / or the nature of the case pending in the Court/ University/ Education Authority etc., at time of filling up this form', max_length=40, null=True, verbose_name='Description of Above'),
        ),
    ]
