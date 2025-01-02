from django import forms

from ..models.ModeloImportador import ModeloImportador

class ImportadorForm(forms.ModelForm):
    class Meta:
        model = ModeloImportador
        fields = ['nombre_importador', 'nit_importador', 'tipo_importador']
        widgets = {
            'tipo_importador': forms.Select(
                choices=ModeloImportador.TIPO_IMPORTADOR_CHOICES
            ),
        }
