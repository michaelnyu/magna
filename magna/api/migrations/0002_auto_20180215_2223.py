# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='arms',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='userentry',
            name='head',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='userentry',
            name='legs',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='userentry',
            name='shoes',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='userentry',
            name='torso',
            field=models.CharField(default='default', max_length=50),
        ),
    ]