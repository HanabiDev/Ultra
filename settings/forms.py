#encoding: utf-8
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



from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class AddUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Usuario"
		self.fields['password1'].label = "Contraseña"
		self.fields['password2'].label = "Confirmar contraseña"

		self.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario', 'class':'form-control'})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Nueva contraseña', 'class':'form-control'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirmación', 'class':'form-control'})

