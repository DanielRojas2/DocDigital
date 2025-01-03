from django import forms

from ..models.ModeloPersonalAgencia import ModeloPersonalAgencia

class PersonalAgenciaForm(forms.ModelForm):
    class Meta:
        model = ModeloPersonalAgencia
        fields = ['nombre_personal', 'apellido_personal', 'telefono_personal']
