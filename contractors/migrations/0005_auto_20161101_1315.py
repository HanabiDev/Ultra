# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0004_auto_20161031_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='group_name',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre del grupo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intervention',
            name='veedor',
            field=models.CharField(default='', max_length=100, verbose_name='Veedor del grupo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intervention',
            name='veedor_phone',
            field=models.CharField(default='', max_length=100, verbose_name='Tel\xe9fono del veedor'),
            preserve_default=False,
        ),
    ]