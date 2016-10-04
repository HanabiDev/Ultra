#encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django_resized.forms import ResizedImageField

from programs.models import Province, Municipality


def get_path(instance,file):
    return 'uploads/athletes/'+str(instance.id)+'/'+file

class Athlete(models.Model):

    HEALTHCARE = (
        ('E', 'EPS'),
        ('S', 'SISBEN')
    )

    CLOTHES_SIZE = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    )

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
        upload_to=get_path, null=True, blank=True, verbose_name=u'Foto')
    dni_support = models.FileField(upload_to=get_path, verbose_name=u'Copia del documento de identidad')

    healthcare = models.CharField(max_length=1, verbose_name=u'Regimen de Salud', choices=HEALTHCARE)
    eps_name = models.CharField(max_length=50, verbose_name=u'Nombre de la empresa')
    clothes_size = models.CharField(max_length=3, verbose_name=u'Talla de ropa', choices=CLOTHES_SIZE)
    shoes_size  = models.IntegerField(verbose_name=u'Talla de zapatos')


    contact_fullname = models.CharField(max_length=100, verbose_name=u'Nombre completo')
    contact_phone = models.CharField(max_length=15, verbose_name=u'Teléfono')
    contact_address = models.CharField(max_length=70, verbose_name=u'Dirección')
    contact_mail = models.EmailField(max_length=50, verbose_name=u'Correo electrónico')


    def __unicode__(self):
        return self.first_name +" "+ self.last_name

    class Meta:
        unique_together = (("document_type", "document_number"),)



# disciplinas y clubes
class Sport(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Nombre')

    def __unicode__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Nombre')
    sport = models.ForeignKey('Sport', verbose_name=u'Deporte')

    def __unicode__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Nombre')
    league = models.ForeignKey('League', verbose_name=u'Liga')

    def __unicode__(self):
        return self.name

class SocialCard(models.Model):
    athlete = models.ForeignKey('Athlete', verbose_name=u'Deportista')
    stratum = models.CharField(max_length=10, verbose_name=u'Estrato')
    sector = models.CharField(max_length=1, choices=(('U','Urbano'),('R', 'Rural')), verbose_name=u'Sector')
    family_members = models.IntegerField(verbose_name=u'Nucleo familiar (número de personas)')
    father_job = models.CharField(max_length=30, verbose_name=u'Ocupación del padre')
    mother_job = models.CharField(max_length=30, verbose_name=u'Ocupación de la madre')
    civil_status = models.CharField(max_length=15, verbose_name=u'Estado civil')
    children = models.IntegerField(verbose_name=u'Hijos')


class SportsTab(models.Model):
    athlete = models.ForeignKey('Athlete', verbose_name=u'Deportista')
    sport = models.ForeignKey('Sport', verbose_name=u'Deporte')
    category = models.CharField(max_length=50, verbose_name=u'Categoría')
    modality = models.CharField(max_length=50, verbose_name=u'Modalidad', blank=True, null=True)
    league = models.ForeignKey('League', verbose_name=u'Liga')
    club = models.ForeignKey('Club', verbose_name=u'Club')
    admission_date = models.DateField(verbose_name=u'Fecha de ingreso')
    activity_start_date = models.DateField(verbose_name=u'Fecha de inicio en el deporte')


class Result(models.Model):
    athlete = models.ForeignKey('Athlete', verbose_name=u'Deportista')
    event = models.CharField(max_length=100, verbose_name=u'Evento')
    test = models.CharField(max_length=40, verbose_name=u'Prueba')
    result = models.CharField(max_length=1, verbose_name=u'Resultado (Puesto)')
    mark = models.FloatField(verbose_name=u'Marca', blank=True, null=True)
    result_date = models.DateField(verbose_name=u'Fecha')


    def __unicode__(self):
        return self.event+" ("+self.result+" puesto)"

class MarkReference(models.Model):
    result = models.ForeignKey('Result', verbose_name=u'Resultado')
    athlete = models.CharField(max_length=60, verbose_name=u'Deportista')
    event = models.CharField(max_length=100, verbose_name=u'Evento')
    test = models.CharField(max_length=40, verbose_name=u'Prueba')
    ref_result = models.CharField(max_length=1, verbose_name=u'Resultado (Puesto)')
    mark = models.FloatField(verbose_name=u'Marca', blank=True, null=True)
    result_date = models.DateField(verbose_name=u'Fecha')




class TestReference(models.Model):
    value = models.FloatField(verbose_name=u'Marca')

class PhysicalTest(models.Model):
    ref = models.ForeignKey('TestReference')
    test_name = models.CharField(max_length=50, verbose_name=u'Prueba')
    result = models.FloatField(verbose_name=u'Resultado')

class TechnicalTest(models.Model):
    ref = models.ForeignKey('TestReference')
    test_name = models.CharField(max_length=50, verbose_name=u'Prueba')
    result = models.FloatField(verbose_name=u'Resultado')