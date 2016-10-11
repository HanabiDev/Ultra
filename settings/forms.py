from athletes.models import Sport, League, Club
from django import forms


class SportForm(forms.ModelForm):
	class Meta:
		model = Sport
		fields = '__all__'

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'})
		}


class LeagueForm(forms.ModelForm):
	class Meta:
		model = League
		fields = ['sport', 'name']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'sport': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
		}


class ClubForm(forms.ModelForm):
	class Meta:
		model = Club
		fields = ['league', 'name']

		widgets = {
			'league': forms.Select(attrs={'class': 'selectpicker', 'data-style':'btn-info btn-fill btn-block'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
		}