# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-06 01:08
from __future__ import unicode_literals

import contractors.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0010_auto_20161227_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventBeneficiaryCategory',
            fields=[
                ('beneficiarycategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contractors.BeneficiaryCategory')),
            ],
            bases=('contractors.beneficiarycategory',),
        ),
        migrations.CreateModel(
            name='MassiveEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('place', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('evidence', models.ImageField(upload_to=contractors.models.get_interv_path, verbose_name='Evidencia')),
                ('observations', models.TextField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='SessionBeneficiaryCategory',
            fields=[
                ('beneficiarycategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contractors.BeneficiaryCategory')),
                ('category_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.Session')),
            ],
            bases=('contractors.beneficiarycategory',),
        ),
        migrations.RemoveField(
            model_name='beneficiarycategory',
            name='session',
        ),
        migrations.AddField(
            model_name='eventbeneficiarycategory',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.MassiveEvent'),
        ),
    ]
