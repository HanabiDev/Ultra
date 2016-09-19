#encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django_resized.forms import ResizedImageField

from programs.models import Province, Municipality


class Athlete(models.Model):

    DNI_TYPES = (
        ('R', 'Registro Civil'),
        ('T', 'Tarjeta de Identidad'),
        ('C', 'Cédula de Ciudadanía'),
        ('E', 'Cédula de Extranjería')
    )

    SCHOOL_LEVELS = (
        ('P', 'Primaria'),
        ('S', 'Secundario'),
        ('T', 'Media Técnica'),
        ('U', 'Universidad')
    )

    GENRES = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    RH = (
        ("AP", "A+"),
        ("AM", "A-"),
        ("ABP", "AB+"),
        ("ABM", "AB-"),
        ("BP", "B+"),
        ("BM", "B-"),
        ("OP", "O+"),
        ("OM", "O-"),
    )

    first_name = models.CharField(max_length=50, verbose_name=u'Nombres')
    last_name = models.CharField(max_length=50, verbose_name=u'Apellidos')
    document_type = models.CharField(max_length=1, verbose_name=u'Tipo de documento', choices=DNI_TYPES)
    document_number = models.CharField(max_length=30, verbose_name=u'Número de documento', unique=True)
    phone = models.CharField(max_length=15, verbose_name=u'Teléfono')
    genre = models.CharField(max_length=1, verbose_name=u'Género', choices=GENRES)
    rh = models.CharField(max_length=3, choices=RH, verbose_name=u'RH')

    province = models.ForeignKey(Province, verbose_name=u'Provincia')
    municipality = models.ForeignKey(Municipality, verbose_name=u'Municipio')
    address = models.CharField(max_length=30, verbose_name=u'Dirección')

    email = models.EmailField(max_length=50, verbose_name=u'Correo electrónico')
    birth_date = models.DateField(verbose_name=u'Fecha de nacimiento')
    birthplace = models.CharField(max_length=50, verbose_name=u'Lugar de nacimiento')

    school_level = models.CharField(max_length=20, verbose_name=u'Nivel de estudios', choices=SCHOOL_LEVELS)
    institution = models.CharField(max_length=50, verbose_name=u'Institucion educativa')

    photo = ResizedImageField(size=[150, 150], crop=['middle', 'center'],
        upload_to='uploads/avatars', null=True, blank=True, verbose_name=u'Foto')

    def __unicode__(self):
        return self.first_name +" "+ self.last_name

    class Meta:
        unique_together = (("document_type", "document_number"),)



# disciplinas y clubes


