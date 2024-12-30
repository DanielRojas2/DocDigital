from django.db import models
from django.utils.timezone import now

from auditlog.registry import auditlog

class ModeloAduanaDespacho(models.Model):
    aduana_despacho = models.CharField(
        max_length=25, blank=False, null=False, unique=True,
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Aduana Despacho'
        verbose_name_plural = 'Aduana Despacho'
    
    def __str__(self):
        return f"{self.aduana_despacho}"
    
auditlog.register(ModeloAduanaDespacho)
