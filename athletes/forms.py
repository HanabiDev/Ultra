#encoding: utf-8

from betterforms.forms import Fieldset
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from betterforms import forms as b_forms
from django import forms

from athletes.models import Athlete


class Button(Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        return format_html(u'<a{}>Cambiar contraseña</a>', (flatatt(final_attrs)))

class AthleteForm(b_forms.BetterModelForm):

    def __init__(self, *args, **kwargs):
        super(AthleteForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super(AthleteForm, self).save(commit=False)

        if commit:
            user.save()
        return user

    class Meta:
        model = Athlete
        fields = [
            'first_name', 'last_name', 'document_type', 'document_number',
            'birth_date',
            #'birthplace',
            'province', 'municipality', 'address', 'phone',
            'photo', 'email', 'school_level', 'institution',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'document_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'province': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'municipality': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'school_level': forms.Select(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
        }

        fieldsets = (

            Fieldset('basic', fields=(
                'first_name', 'last_name', 'document_type','document_number', 'birth_date', 'province', 'municipality',
                'address',
            ), legend=u'1. Datos básicos'),

            Fieldset('additional', fields=(
                'photo', 'phone', 'email', 'school_level', 'institution',
            ), legend=u'2. Datos Adicionales'),
        )