# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-06 02:14
from __future__ import unicode_literals

import contractors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0011_auto_20170305_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='plist',
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='', max_length=1, verbose_name='G\xe9nero'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='massiveevent',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='massiveevent',
            name='evidence',
            field=models.ImageField(upload_to=contractors.models.get_event_path, verbose_name='Evidencia'),
        ),
    ]
