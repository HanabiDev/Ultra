#encoding: utf-8
from __future__ import unicode_literals

from django.db import models

from programs.models import Province, Municipality


class Athlete(models.Model):

    DNI_TYPES = (
        ('R', 'Registro Civil'),
        ('T', 'Tarjeta de Identidad'),
        ('C', 'Cédula de Ciudadanía'),
        ('E', 'Cédula de Extranjería')
    )

    first_name = models.CharField(max_length=50, verbose_name=u'Nombres')
    last_name = models.CharField(max_length=50, verbose_name=u'Apellidos')
    document_type = models.CharField(max_length=1, verbose_name=u'Tipo de documento', choices=DNI_TYPES)
    document_number = models.CharField(max_length=30, verbose_name=u'Número de documento')
    phone = models.CharField(max_length=15, verbose_name=u'Teléfono')

    province = models.ForeignKey(Province, verbose_name=u'Provincias')
    municipality = models.ForeignKey(Municipality, verbose_name=u'Municipio')
    address = models.CharField(max_length=30, verbose_name=u'Dirección')

    email = models.EmailField(max_length=50, verbose_name=u'Correo electrónico')
    birth_date = models.DateField(verbose_name=u'Fecha de nacimiento')
    birthplace = models.CharField(max_length=50, verbose_name=u'Lugar de nacimiento')

    school_level = models.CharField(max_length=20, verbose_name=u'Nivel de estudios')
    institution = models.CharField(max_length=50, verbose_name=u'Institucion educativa')

    photo = models.CharField(max_length=100, verbose_name=u'Foto')

    def __unicode__(self):
        return self.first_name +" "+ self.last_name
