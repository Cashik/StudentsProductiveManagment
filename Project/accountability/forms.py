from django import forms
from .models import Specialties


class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialties
        fields = ('id', 'name', 'description')
