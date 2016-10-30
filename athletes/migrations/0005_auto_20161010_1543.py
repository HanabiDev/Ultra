# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 15:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0004_auto_20161004_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntropometricValoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.TextField(verbose_name='Diagn\xf3stico')),
                ('body_weight', models.FloatField(verbose_name='Peso corporal')),
                ('muscle_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Peso muscular (%)')),
                ('fat_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Peso graso (%)')),
                ('six_skinfolds', models.FloatField(verbose_name='Sumatoria de seis pliegues')),
            ],
        ),
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.TextField(verbose_name='Diagn\xf3stico')),
                ('status', models.CharField(choices=[('A', 'APTO'), ('N', 'NO APTO'), ('R', 'APTO CON RECOMENDACIONES'), ('X', 'APTO CON RESTRICCIONES')], max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='BiomedicTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete', verbose_name='Deportista')),
            ],
        ),
        migrations.CreateModel(
            name='PhysiologicalTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vo2_max', models.FloatField(verbose_name='VO2 M\xe1x')),
                ('aerobic_capacity', models.FloatField(verbose_name='Capacidad aer\xf3bica')),
                ('fc_max', models.FloatField(verbose_name='FC M\xe1x')),
                ('speed_power_max', models.FloatField(verbose_name='Velocidad o Potencia M\xe1x')),
                ('wingate', models.FloatField(verbose_name='Wingate')),
                ('squat_jump', models.FloatField(verbose_name='Squat Jump')),
                ('counter_movement_jump', models.FloatField(verbose_name='Counter Movement Jump')),
                ('drop_jump', models.FloatField(verbose_name='Drop Jump')),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.BiomedicTab', verbose_name='Deportista')),
            ],
        ),
        migrations.CreateModel(
            name='PsicologicValoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.TextField(verbose_name='Diagn\xf3stico')),
                ('confidence', models.IntegerField(verbose_name='Confianza')),
                ('motivation', models.IntegerField(verbose_name='Motivaci\xf3n')),
                ('concentration', models.IntegerField(verbose_name='Concentraci\xf3n')),
                ('emotinal_sensibility', models.IntegerField(verbose_name='Sensibilidad emocional')),
                ('imagination', models.IntegerField(verbose_name='Imaginaci\xf3n')),
                ('positive_attitude', models.IntegerField(verbose_name='Actitud positiva')),
                ('competitive_challege', models.IntegerField(verbose_name='Reto competitivo')),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.BiomedicTab', verbose_name='Deportista')),
            ],
        ),
        migrations.CreateModel(
            name='SFPBValoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.TextField(verbose_name='Diagn\xf3stico')),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.BiomedicTab', verbose_name='Deportista')),
            ],
        ),
        migrations.AlterField(
            model_name='socialcard',
            name='athlete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete', verbose_name='Deportista'),
        ),
        migrations.AlterField(
            model_name='sportstab',
            name='athlete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete', verbose_name='Deportista'),
        ),
        migrations.AddField(
            model_name='aptitudetest',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.BiomedicTab', verbose_name='Deportista'),
        ),
        migrations.AddField(
            model_name='antropometricvaloration',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.BiomedicTab', verbose_name='Deportista'),
        ),
    ]