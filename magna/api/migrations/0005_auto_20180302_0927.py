# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180302_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='region',
            field=models.CharField(default='US', max_length=50),
        ),
    ]
