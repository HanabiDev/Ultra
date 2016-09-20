#encoding: utf-8

from betterforms import forms as b_forms
from django import forms
from programs.models import Program, Subprogram, Project


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

    def __init__(self, *args, **kwargs):
        super(SubprogramForm, self).__init__(*args, **kwargs)
        
        if kwargs.get('initial'):
            program = kwargs.get('initial').get('program')
            if program:
                self.fields['program'].choices = [(program.id, program.name)]

    class Meta:
        model = Subprogram
        fields = '__all__'

        widgets = {
        	'program': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'description': SummernoteWidget(),
        }


class ProjectForm(b_forms.BetterModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        if kwargs.get('initial'):
            subprogram = kwargs.get('initial').get('subprogram')
            if subprogram:
                self.fields['subprogram'].choices = [(subprogram.id, subprogram.name)]

    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'subprogram': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'consecutive': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'description': SummernoteWidget(),
        }