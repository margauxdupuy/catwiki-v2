from django import forms
from .models import Cat


class SelectBreedForm(forms.Form):
    cats_qs = Cat.objects.all()
    breed = forms.CharField(label=False, widget=forms.Select(choices=[(x.id_name, x.name) for x in cats_qs]))
