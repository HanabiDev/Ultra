# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-20 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0008_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
            preserve_default=False,
        ),
    ]