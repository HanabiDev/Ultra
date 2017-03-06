# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-11 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_contestant_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='cid',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='contestant',
            unique_together=set([('event', 'cid')]),
        ),
    ]