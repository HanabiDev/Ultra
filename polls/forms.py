#encoding: utf-8

from betterforms import forms as b_forms
from django import forms

from polls.models import Poll, Question, Option
from programs.models import Program, Subprogram, Project


from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PollForm(b_forms.BetterModelForm):

    class Meta:
        model = Poll
        exclude = ['hits']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'closed': forms.CheckboxInput(),
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