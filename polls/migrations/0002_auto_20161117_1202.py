# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poll',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
