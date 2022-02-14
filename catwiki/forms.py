from django import forms
from .services import get_breeds


class SelectBreedForm(forms.Form):
    breeds = get_breeds('/breeds')
    breed = forms.CharField(label=False, widget=forms.Select(choices=breeds['list']))
