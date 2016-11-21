#encoding: utf-8

from betterforms.forms import Fieldset
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from betterforms import forms as b_forms
from django import forms

from athletes.models import Athlete, SportsTab, Result, MarkReference, SocialCard, AptitudeTest, SFPBValoration, AntropometricValoration, PsicologicValoration, \
    TestReference, PhysicalTest
from athletes.models import PhysiologicalTest

class Button(Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        return format_html(u'<a{}>Cambiar contraseña</a>', (flatatt(final_attrs)))

class AthleteForm(b_forms.BetterModelForm):


    class Meta:
        model = Athlete
        fields = [
            'first_name', 'last_name', 'document_type', 'document_number',
            'birth_date', 'birthplace', 'genre','rh',
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
            'birth_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'birthplace': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'rh': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
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

            Fieldset('additional', fields=(
                'genre','rh','photo', 'dni_support', 'healthcare', 'eps_name', 'clothes_size', 'shoes_size'
            ), legend=u'2. Información adicional'),

            Fieldset('contact', fields=(
                'province', 'municipality', 'address', 'phone', 'email'
            ), legend=u'3. Información de contacto'),

            Fieldset('alternate_contact', fields=(
                'contact_fullname', 'contact_phone', 'contact_address', 'contact_mail',
            ), legend=u'4. Contacto alternativo'),
        )



class AthleteCardForm(forms.ModelForm):

    class Meta:
        model = SportsTab
        fields = [
            'athlete', 'sport', 'priorization', 'league', 'club', 'admission_date', 'category', 'modality', 'functional', 'activity_start_date'
        ]

        widgets = {
            'athlete': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'sport': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'priorization': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'league': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'club': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'admission_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'modality': forms.TextInput(attrs={'class': 'form-control'}),
            'functional': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }


class AthleteSocialCardForm(forms.ModelForm):

    class Meta:
        model = SocialCard
        fields = [
            'athlete', 'stratum', 'sector', 'family_members', 'father_job', 'mother_job', 'civil_status', 'children'
        ]

        widgets = {
            'athlete': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'stratum': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'family_members': forms.NumberInput(attrs={'class': 'form-control'}),
            'father_job': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_job': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_status': forms.TextInput(attrs={'class': 'form-control'}),
            'children': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AthleteResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = [
            'athlete','event', 'result_date', 'test', 'result', 'mark'
        ]

        widgets = {
            'athlete': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'test': forms.TextInput(attrs={'class': 'form-control'}),
            'result': forms.TextInput(attrs={'class': 'form-control'}),
            'mark': forms.NumberInput(attrs={'class': 'form-control'}),
            'result_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),

        }


class AthleteResultRefForm(forms.ModelForm):

    class Meta:
        model = MarkReference
        fields = [
            'result', 'athlete','event', 'result_date', 'test', 'ref_result', 'mark'
        ]

        widgets = {
            'result': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'athlete': forms.TextInput(attrs={'class': 'form-control'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'test': forms.TextInput(attrs={'class': 'form-control'}),
            'ref_result': forms.TextInput(attrs={'class': 'form-control'}),
            'mark': forms.NumberInput(attrs={'class': 'form-control'}),
            'result_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }


class AptitudeTestForm(forms.ModelForm):

    class Meta:
        model = AptitudeTest
        fields = '__all__'

        widgets = {
            'tab': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'diagnostic': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
        }

class SFPBValorationForm(forms.ModelForm):

    class Meta:
        model = SFPBValoration
        fields = '__all__'

        widgets = {
            'tab': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'diagnostic': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AntropometricValorationForm(forms.ModelForm):

    class Meta:
        model = AntropometricValoration
        fields = '__all__'

        widgets = {
            'tab': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'diagnostic': forms.Textarea(attrs={'class': 'form-control'}),
            'body_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'muscle_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'six_skinfolds': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        
class PsicologicValorationForm(forms.ModelForm):
    class Meta:
        model = PsicologicValoration
        fields = '__all__'

        widgets = {
            'tab': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'diagnostic': forms.Textarea(attrs={'class': 'form-control'}),
            'confidence':forms.NumberInput(attrs={'class': 'form-control'}),
            'motivation':forms.NumberInput(attrs={'class': 'form-control'}),
            'concentration':forms.NumberInput(attrs={'class': 'form-control'}),
            'emotinal_sensibility':forms.NumberInput(attrs={'class': 'form-control'}),
            'imagination':forms.NumberInput(attrs={'class': 'form-control'}),
            'positive_attitude':forms.NumberInput(attrs={'class': 'form-control'}),
            'competitive_challege':forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PhysiologicalTestForm(forms.ModelForm):

    class Meta:
        model = PhysiologicalTest
        fields = '__all__'

        widgets = {
            'tab': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'vo2_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'aerobic_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'fc_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'speed_power_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'wingate': forms.NumberInput(attrs={'class': 'form-control'}),
            'squat_jump': forms.NumberInput(attrs={'class': 'form-control'}),
            'counter_movement_jump': forms.NumberInput(attrs={'class': 'form-control'}),
            'drop_jump': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TestReferenceForm(forms.ModelForm):

    class Meta:
        model = TestReference
        fields = '__all__'

        widgets = {
            'athlete': forms.TextInput(attrs={'class': 'form-control'}),
            'intl': forms.CheckboxInput(),
            'value': forms.NumberInput(attrs={'step':'0.001', 'class':'form-control'}),
        }


class PhysicalTestForm(forms.ModelForm):
    class Meta:
        model = PhysicalTest
        fields = '__all__'

        widgets = {
            'ref': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'test_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'result': forms.NumberInput(attrs={'step': '0.001', 'class': 'form-control'}),
        }

