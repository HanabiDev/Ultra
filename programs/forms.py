#encoding: utf-8

from betterforms import forms as b_forms
from django import forms
from programs.models import Program


class ProgramForm(b_forms.BetterModelForm):

    class Meta:
        model = Program
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }