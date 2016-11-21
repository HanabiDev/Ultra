#encoding: utf-8
from __future__ import unicode_literals

from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Título')
    description = models.TextField(verbose_name=u'Descripción')
    creation_date = models.DateField(auto_now=True)
    closed = models.BooleanField(verbose_name=u'Cerrada')
    hits = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Question(models.Model):
    poll = models.ForeignKey('Poll', verbose_name='Encuesta')
    statement = models.TextField(verbose_name=u'Pregunta')

    def __unicode__(self):
        return self.statement

class Option(models.Model):
    question = models.ForeignKey('Question', verbose_name=u'Pregunta')
    text = models.CharField(max_length=100,verbose_name=u'Texto de la opcion')
    hits = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text