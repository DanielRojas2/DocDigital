from django.contrib import admin

from .models.ModeloAduanaDespacho import ModeloAduanaDespacho
from .models.ModeloCanalApertura import ModeloCanalApertura
from .models.ModeloImportador import ModeloImportador
from .models.ModeloMercaderia import ModeloMercaderia
from .models.ModeloModalidadDespacho import ModeloModalidadDespacho
from .models.ModeloPersonalAgencia import ModeloPersonalAgencia

@admin.register(ModeloAduanaDespacho)
class AduanaDespachoAdmin(admin.ModelAdmin):
    list_display = ['aduana_despacho', 'creado']
    search_fields = ['aduana_despacho']
    date_hierarchy = ['creado']

@admin.register(ModeloCanalApertura)
class CanalAperturaAdmin(admin.ModelAdmin):
    list_display = ['tipo_canal', 'creado']
    search_fields = ['tipo_canal']
    date_hierarchy = ['creado']

@admin.register(ModeloImportador)
class ImportadorAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_importador', 'nit_importador', 'tipo_importador', 'creado'
    ]
    list_filter = ['tipo_importador']
    search_fields = ['nombre_importador', 'nit_importador']
