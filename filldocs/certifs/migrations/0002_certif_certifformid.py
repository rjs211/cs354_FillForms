# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certif',
            name='certifFormId',
            field=models.IntegerField(default=1),
        ),
    ]