from django import forms

from ..models.ModeloMercaderia import ModeloMercaderia

class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = ModeloMercaderia
        fields = ['nombre_mercaderia']
