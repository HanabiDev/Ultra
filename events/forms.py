#encoding: utf-8

from betterforms import forms as b_forms
from django import forms

from events.models import Event
from polls.models import Poll, Question, Option
from programs.models import Program, Subprogram, Project


from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class EventForm(b_forms.BetterModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        if kwargs.get('initial'):
            owner = kwargs.get('initial').get('owner')
            if owner:
                self.fields['owner'].choices = [(owner.id, owner)]

    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'owner': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sport': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'btn-info btn-fill btn-block'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'open': forms.CheckboxInput(),
            'description': SummernoteWidget(),
        }


class QuestionForm(b_forms.BetterModelForm):

    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'poll': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'statement': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OptionForm(b_forms.BetterModelForm):

    class Meta:
        model = Option
        exclude = ['hits']

        widgets = {
            'question': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }