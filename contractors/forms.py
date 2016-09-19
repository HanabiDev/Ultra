#encoding: utf-8

from contractors.models import Contractor
from django import forms


from betterforms.forms import Fieldset
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from betterforms import forms as b_forms
from django import forms


class Button(Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        return format_html(u'<a{}>Cambiar contraseña</a>', (flatatt(final_attrs)))

class ContractorForm(b_forms.BetterModelForm):

    def __init__(self, *args, **kwargs):
        super(ContractorForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super(ContractorForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user

    class Meta:
        model = Contractor
        fields = [
            'first_name', 'last_name', 'dni_type','dni', 'address',
            'phone', 'mobile', 'avatar', 'type', 'username', 'password', 'email',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni_type': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),

            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        fieldsets = (

            Fieldset('basic', fields=(
                'first_name', 'last_name', 'dni_type','dni', 'address', 'phone', 'mobile'
            ), legend=u'1. Datos básicos'),

            Fieldset('account', fields=(
                'avatar', 'type', 'username', 'password', 'email',
            ), legend=u'2. Información de la cuenta'),
        )