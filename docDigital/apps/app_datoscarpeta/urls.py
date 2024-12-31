from django.urls import path

from .views.AduanaDespachoView import (
    lista_aduana_despacho, editar_aduana_despacho, elimiar_aduana_despacho
)

urlpatterns = [
    path('recintos_aduaneros/', lista_aduana_despacho, name='recintos_aduaneros'),
    path('editar_recinto/<int:pk>/', editar_aduana_despacho, name='editar_recinto'),
    path('eliminar_recinto/<int:pk>/', elimiar_aduana_despacho, name='eliminar_recinto'),
]
