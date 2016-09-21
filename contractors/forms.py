#encoding: utf-8

from contractors.models import Contractor, FormationItem
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from betterforms.forms import Fieldset
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from betterforms import forms as b_forms
from django import forms
from django.urls.base import reverse_lazy

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

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

class EditContractorForm(b_forms.BetterModelForm):

    def __init__(self, *args, **kwargs):
        super(EditContractorForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        self.fields['avatar'].required = False
        self.fields['password'].required = False
        self.fields['password'].widget = Button(
            attrs={
                'class':'btn waves-attach col-xs-12', 
                'href':reverse_lazy('contractors:pass', kwargs={'user_id':self.instance.id})
            }
        )

    def save(self, commit=True):
        user = super(EditContractorForm, self).save(commit=False)
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

class PasswordForm(SetPasswordForm):


    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "Contraseña nueva"
        self.fields['new_password2'].label = "Contraseña nueva (confirmación)"
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})


    class Meta:
        model = Contractor
        fields = '__all__'

        widgets = {
            'new_password1':forms.PasswordInput(attrs={'class':'form-control'})
        }


class FormationItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormationItemForm, self).__init__(*args, **kwargs)
        
        if kwargs.get('initial'):
            trainer = kwargs.get('initial').get('trainer')
            if trainer:
                self.fields['trainer'].choices = [(trainer.id, trainer.get_full_name())]


    class Meta:
        model = FormationItem
        fields = '__all__'

        widgets = {
            'trainer': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'support': forms.FileInput(attrs={'class': 'form-control'}),
        }