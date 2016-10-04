#encoding: utf-8

from betterforms.forms import Fieldset
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from betterforms import forms as b_forms
from django import forms

from athletes.models import Athlete, SportsTab


class Button(Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        return format_html(u'<a{}>Cambiar contraseña</a>', (flatatt(final_attrs)))

class AthleteForm(b_forms.BetterModelForm):


    class Meta:
        model = Athlete
        fields = [
            'first_name', 'last_name', 'document_type', 'document_number',
            'birth_date', 'birthplace',
            'province', 'municipality', 'address', 'phone',
            'photo', 'email', 'school_level', 'institution', 'dni_support',
            'contact_fullname', 'contact_phone', 'contact_address', 'contact_mail',
            'healthcare', 'eps_name', 'clothes_size', 'shoes_size'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'document_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'birthplace': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'municipality': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'school_level': forms.Select(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'dni_support': forms.FileInput(attrs={'class': 'form-control'}),
            'contact_fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_mail': forms.TextInput(attrs={'class': 'form-control'}),
            'healthcare': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'eps_name': forms.TextInput(attrs={'class': 'form-control'}),
            'clothes_size': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'shoes_size': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        fieldsets = (

            Fieldset('basic', fields=(
                'first_name', 'last_name', 'document_type','document_number',
                'birth_date', 'birthplace', 'school_level', 'institution'

            ), legend=u'1. Información básica'),

            Fieldset('contact', fields=(
                'province', 'municipality', 'address', 'phone', 'email'
            ), legend=u'2. Información de contacto'),

            Fieldset('additional', fields=(
                'photo', 'dni_support', 'healthcare', 'eps_name', 'clothes_size', 'shoes_size'
            ), legend=u'3. Información adicional'),

            Fieldset('alternate_contact', fields=(
                'contact_fullname', 'contact_phone', 'contact_address', 'contact_mail',
            ), legend=u'4. Contacto alternativo'),
        )


class AthleteCardForm(forms.ModelForm):

    class Meta:
        model = SportsTab
        fields = [
            'athlete', 'sport', 'league', 'club', 'admission_date', 'category', 'modality', 'activity_start_date'
        ]

        widgets = {
            'athlete': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'sport': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'league': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'club': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'admission_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'modality': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),

        }

