from django.db import models
from django.conf import settings

class PerfilUsuario(models.Model):
    usuario =  models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    nacimiento = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'
