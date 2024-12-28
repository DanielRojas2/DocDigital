from django import forms
from django.contrib.auth.models import User

from .models.ModeloPerfil import PerfilUsuario

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(
            id=self.instance.id
        ).filter(email=data)

        if qs.exists():
            raise forms.ValidationError('El email ingresado ya esta en uso')
        return data
    
class EditarPerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['nacimiento']
