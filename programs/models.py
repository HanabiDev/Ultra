#encoding: utf-8
from __future__ import unicode_literals

from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Municipality(models.Model):
    province = models.ForeignKey('Province')
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

STATUS_TYPES = (
    ('A', 'Aprobado'),
    ('E', 'Ejecución'),
    ('F', 'Finalizado')
)

class Program(models.Model):

    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    status = models.CharField(max_length=1, choices=STATUS_TYPES, verbose_name=u'Estado')
    description = models.TextField(verbose_name=u'Descripción')

    def __unicode__(self):
        return self.name

class Subprogram(models.Model):
    program = models.ForeignKey('Program', verbose_name=u'Programa')
    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    status = models.CharField(max_length=1, choices=STATUS_TYPES, verbose_name=u'Estado')
    description = models.TextField(verbose_name=u'Descripción')

    def __unicode__(self):
        return self.name


class Project(models.Model):
    subprogram = models.ForeignKey('Subprogram', verbose_name=u'Subprograma')
    consecutive = models.CharField(max_length=100, verbose_name=u'Registro')
    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    status = models.CharField(max_length=1, choices=STATUS_TYPES, verbose_name=u'Estado')
    description = models.TextField(verbose_name=u'Descripción')

    def __unicode__(self):
        return self.name