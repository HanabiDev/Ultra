# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-10 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('contestant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Contestant')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rank',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
