from django.db import models
from django.utils.timezone import now

from auditlog.registry import auditlog

class ModeloPersonalAgencia(models.Model):
    nombre_personal = models.CharField(
        max_length=25, blank=False, null=False
    )
    apellido_personal = models.CharField(
        max_length=25, blank=False, null=False
    )
    telefono_personal = models.CharField(
        max_length=8, blank=True, null=True
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal Agencia'

        constraints = [
            models.UniqueConstraint(
                fields=['nombre_personal', 'apellido_personal'],
                name='unique_nombre_apellido'
            )
        ]

        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]

    def __str__(self):
        return f"{self.nombre_personal} {self.apellido_personal}"

auditlog.register(ModeloPersonalAgencia)
