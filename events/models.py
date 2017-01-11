#encoding:utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from athletes.models import Sport
from contractors.models import AppUser


class Event(models.Model):
    owner = models.ForeignKey(AppUser, verbose_name=u'Organizador')
    name = models.CharField(max_length=100, verbose_name=u'Nombre del evento')
    description = models.TextField(verbose_name=u'Descripción')
    sport = models.ForeignKey(Sport, verbose_name=u'Deporte')
    start_date = models.DateField(verbose_name=u'Inicio')
    end_date = models.DateField(verbose_name=u'Finalización')
    price = models.FloatField(verbose_name=u'Costo (opcional)', blank=True, null=True)
    attachment = models.FileField(upload_to='uploads/events/atachments/', verbose_name=u'Adjunto', blank=True, null=True)
    open = models.BooleanField(default=True, verbose_name=u'Inscripciones abiertas')

    def __unicode__(self):
        return self.name

class Contestant(models.Model):
    event = models.ForeignKey('Event', verbose_name=u'Evento')
    first_name = models.CharField(max_length=50, verbose_name=u'Nombres')
    last_name = models.CharField(max_length=50, verbose_name=u'Apellidos')
    dni = models.CharField(max_length=30, verbose_name=u'Número de documento', unique=True)
    phone = models.CharField(max_length=15, verbose_name=u'Teléfono')
    city = models.CharField(max_length=100, verbose_name=u'Ciudad')
    email = models.EmailField(max_length=50, verbose_name=u'Correo electrónico')
    support = models.FileField(upload_to='uploads/events/supports/')
    cid = models.IntegerField()

    class Meta:
        unique_together = ['event', 'cid']

class Rank(models.Model):
    event = models.ForeignKey('Event')
    contestant = models.ForeignKey('Contestant')
    rank = models.IntegerField()

