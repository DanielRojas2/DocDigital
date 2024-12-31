from django import forms
from ..models.ModeloAduanaDespacho import ModeloAduanaDespacho

class RegistroAduanaDespachoForm(forms.ModelForm):
    class Meta:
        model = ModeloAduanaDespacho
        fields = ['aduana_despacho']
