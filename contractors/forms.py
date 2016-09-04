from contractors.models import Contractor
from django import forms


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor