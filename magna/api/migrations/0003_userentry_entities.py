# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 20:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180311_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='entities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=[], size=None),
        ),
    ]
