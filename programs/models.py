from __future__ import unicode_literals

from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=30)


class Municipality(models.Model):
    province = models.ForeignKey('Province')
    name = models.CharField(max_length=50)


class Program(models.Model):
    name = models.CharField(max_length=100)

class Subprogram(models.Model):
    program = models.ForeignKey('Program')
    name = models.CharField(max_length=100)