#encoding: utf-8

from betterforms import forms as b_forms
from django import forms

from events.models import Event, Contestant
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


class ContestantForm(b_forms.BetterModelForm):
    def __init__(self, *args, **kwargs):
        super(ContestantForm, self).__init__(*args, **kwargs)

        if kwargs.get('initial'):
            event = kwargs.get('initial').get('event')
            if event:
                self.fields['event'].choices = [(event.id, event.name)]

    class Meta:
        model = Contestant
        fields = '__all__'

        widgets = {
            'event': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'support': forms.FileInput(attrs={'class': 'form-control'}),
            'cid': forms.HiddenInput()
        }
