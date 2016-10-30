# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20161004_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stratum', models.CharField(max_length=10, verbose_name='Estrato')),
                ('sector', models.CharField(choices=[('U', 'Urbano'), ('R', 'Rural')], max_length=1, verbose_name='Sector')),
                ('family_members', models.IntegerField(verbose_name='Nucleo familiar (n\xfamero de personas)')),
                ('father_job', models.CharField(max_length=30, verbose_name='Ocupaci\xf3n del padre')),
                ('mother_job', models.CharField(max_length=30, verbose_name='Ocupaci\xf3n de la madre')),
                ('civil_status', models.CharField(max_length=15, verbose_name='Estado civil')),
                ('children', models.IntegerField(verbose_name='Hijos')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete')),
            ],
        ),
        migrations.AlterField(
            model_name='markreference',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Result', verbose_name='Resultado'),
        ),
    ]