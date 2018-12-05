# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 12:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DumUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=100, null=True)),
                ('f2', models.CharField(max_length=20, null=True)),
                ('f3', models.CharField(max_length=3, null=True)),
                ('f4', models.DateField(null=True)),
                ('f5', models.CharField(max_length=3, null=True)),
                ('f6', models.DateField(null=True)),
                ('orguser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]