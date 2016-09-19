#encoding: utf-8

from betterforms import forms as b_forms
from django import forms
from programs.models import Program, Subprogram


from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProgramForm(b_forms.BetterModelForm):

    class Meta:
        model = Program
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'description': SummernoteWidget(),
        }


class SubprogramForm(b_forms.BetterModelForm):

    class Meta:
        model = Subprogram
        fields = '__all__'

        widgets = {
        	'program': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'description': SummernoteWidget(),
        }