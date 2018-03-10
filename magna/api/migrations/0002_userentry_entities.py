# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 01:39
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='entities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=[], size=None),
        ),
    ]