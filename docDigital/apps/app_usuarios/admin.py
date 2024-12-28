from django.contrib import admin

from .models.ModeloPerfil import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nacimiento']
    raw_id_fields = ['usuario']
