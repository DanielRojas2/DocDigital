from django.db import models
from django.utils.timezone import now

from auditlog.registry import auditlog

class ModeloMercaderia(models.Model):

    nombre_mercaderia = models.CharField(
        max_length=75, blank=False, null=False, unique=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mercadería'
        verbose_name_plural = 'Mercadería'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]

    def __str__(self):
        return f"{self.nombre_mercaderia}"
    
auditlog.register(ModeloMercaderia)
