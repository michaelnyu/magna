# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180308_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='character_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]