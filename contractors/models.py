#encoding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django_resized.forms import ResizedImageField

from programs.models import Subprogram, Municipality, Province


def get_path(instance,file):
    return 'uploads/contractors/'+str(instance.trainer.id)+'/'+file

class AppUser(User):
    ResizedImageField(
        size=[150, 150], crop=['middle', 'center'],
        upload_to=get_path, null=False, blank=False, verbose_name=u'Foto'
    ).contribute_to_class(User, 'avatar')


class Contractor(AppUser):

    CONTRACTOR_TYPES = (
        ('I', 'Instructor'),
        ('M', 'Monitor'),
        ('E', 'Entrenador'),
    )

    DNI_TYPES = (
        ('C', 'Cédula de Ciudadanía'),
        ('E', 'Cédula de Extranjería'),
    )

    models.CharField(max_length=1, verbose_name=u'Tipo de contratista', choices=CONTRACTOR_TYPES).contribute_to_class(User, 'type')
    models.CharField(max_length=30, verbose_name=u'Tipo de documento', choices=DNI_TYPES).contribute_to_class(User, 'dni_type')
    models.CharField(max_length=30, verbose_name=u'Número de documento', unique=True).contribute_to_class(User, 'dni')
    models.CharField(max_length=100, verbose_name=u'Dirección').contribute_to_class(User, 'address')
    models.CharField(max_length=10, verbose_name=u'Teléfono Fijo').contribute_to_class(User, 'phone')
    models.CharField(max_length=12, verbose_name=u'Teléfono Móvil').contribute_to_class(User, 'mobile')

    def __unicode__(self):
        return self.get_full_name()



class FormationItem(models.Model):
    trainer = models.ForeignKey('Contractor', verbose_name=u'Contratista')
    description = models.CharField(max_length=100, verbose_name=u'Descripción');
    year = models.CharField(max_length=4, verbose_name=u'Año');
    support = models.FileField(upload_to=get_path, verbose_name=u'Soporte')

    class Meta:
        ordering = ['-year']


class SportsAchievements(models.Model):
    trainer = models.ForeignKey('Contractor', verbose_name=u'Contratista')
    description = models.CharField(max_length=100, verbose_name=u'Descripción');
    year = models.CharField(max_length=4, verbose_name=u'Año');
    support = models.FileField(upload_to=get_path, verbose_name=u'Soporte')

    class Meta:
        ordering = ['-year']



class Intervention(models.Model):
    contractor = models.ForeignKey('Contractor', verbose_name=u'Contratista', null=True, blank=True)
    subprogram = models.ForeignKey(Subprogram, verbose_name=u'Subprograma')
    province = models.ForeignKey(Province, verbose_name=u'Provincia')
    municipality = models.ForeignKey(Municipality, verbose_name=u'Municipio')
    neighborhood = models.CharField(max_length=60, verbose_name=u'Barrio/Vereda')
    address = models.CharField(max_length=100, verbose_name=u'Dirección')



class TimeSchedule(models.Model):

    WEEK_DAYS = (
        ('Lu', 'Lunes'),
        ('Ma', 'Martes'),
        ('Mi', 'Miércoles'),
        ('Ju', 'Jueves'),
        ('Vi', 'Viernes'),
    )

    intervention = models.ForeignKey('Intervention')
    day = models.CharField(max_length=2, choices=WEEK_DAYS)
    startTime = models.TimeField()
    endTime = models.TimeField()


class Session(models.Model):
    date = models.DateTimeField(auto_now=True)
    intervention = models.ForeignKey('Intervention')


class BeneficiaryCategory(models.Model):

    AGE_RANGES = (
        ('1','0 a 5 Años'),
        ('2', '6 a 12 Años'),
        ('3', '13 a 17 Años'),
        ('4', '18 a 29 Años'),
        ('5', '30 a 59 Años'),
        ('6', 'Más de 60 Años')
    )
    session = models.ForeignKey('Session')
    age_range =  models.CharField(max_length=2, choices=AGE_RANGES)


class BeneficiaryGroup(models.Model):
    SOCIAL_CONDITIONS = (
        ('M', 'Mestizos'),
        ('I', 'Indígenas'),
        ('C', 'Campesinos'),
        ('D', 'Discapacitados'),
        ('A', 'Afrodescendientes')

    )

    category = models.ForeignKey('BeneficiaryCategory')
    group_name = models.CharField(max_length=2, choices=SOCIAL_CONDITIONS)
    femenine_individuals = models.IntegerField()
    masculine_individuals = models.IntegerField()
