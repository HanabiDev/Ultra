# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0003_auto_20161030_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='latitude',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intervention',
            name='longitude',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
