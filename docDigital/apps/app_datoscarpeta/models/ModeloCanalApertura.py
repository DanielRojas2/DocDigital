from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.utils.timezone import now

from auditlog.registry import auditlog

class ModeloCanalApertura(models.Model):
    CANAL_CHOICES = (
        ('rojo', 'rojo'),
        ('amarillo', 'amarillo'),
        ('verde', 'verde')
    )
    tipo_canal = models.CharField(
        max_length=8, blank=False, null=True, unique=True,
        choices=CANAL_CHOICES,
        validators=[
            RegexValidator(
                regex='^(rojo|amarillo|verde)$',
                message='Canal de apertura inválido'
            )
        ]
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Canal'
    
    def clean(self):
        self.tipo_canal = escape(self.tipo_canal)

        if self.tipo_canal not in dict(self.CANAL_CHOICES).keys():
            raise ValidationError(
                f"{self.tipo_canal} no es un canal válido"
            )
    
    def __str__(self):
        return f"{self.tipo_canal}"

auditlog.register(ModeloCanalApertura)
