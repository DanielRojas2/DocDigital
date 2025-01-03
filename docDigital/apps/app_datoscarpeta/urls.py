from django.urls import path

from .views.AduanaDespachoView import (
    lista_aduana_despacho, editar_aduana_despacho, elimiar_aduana_despacho
)
from .views.ImportadorView import (
    listar_importador, editar_importador, eliminar_importador
)
from .views.MercaderiaView import (
    mercaderia, editar_mercaderia, eliminar_mercaderia
)

urlpatterns = [
    path('recintos_aduaneros/', lista_aduana_despacho, name='recintos_aduaneros'),
    path('editar_recinto/<int:pk>/', editar_aduana_despacho, name='editar_recinto'),
    path('eliminar_recinto/<int:pk>/', elimiar_aduana_despacho, name='eliminar_recinto'),
    path('importadores/', listar_importador, name='importadores'),
    path('editar_importador/<int:pk>/', editar_importador, name='editar_importador'),
    path('eliminar_importador/<int:pk>/', eliminar_importador, name='eliminar_importador'),
    path('mercaderia/', mercaderia, name='mercaderia'),
    path('editar_mercaderia/<int:pk>/', editar_mercaderia, name='editar_mercaderia'),
    path('eliminar_mercaderia/<int:pk>/', eliminar_mercaderia, name='eliminar_mercaderia'),
]
