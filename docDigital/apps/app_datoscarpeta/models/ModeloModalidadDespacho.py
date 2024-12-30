from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.utils.timezone import now

from auditlog.registry import auditlog

class ModeloModalidadDespacho(models.Model):
    MODALIDADDESPACHO_CHOICES = (
        ('anticipado', 'anticipado'),
        ('abreviado', 'abreviado'),
        ('general', 'general')
    )

    tipo_despacho = models.CharField(
        max_length=10, blank=False, null=False, unique=True,
        choices=MODALIDADDESPACHO_CHOICES,
        validators=[
            RegexValidator(
                regex='^(anticipado|abreviado|general)',
                message='Modalidad de despacho inválido'
            )
        ]
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Modalidad de Despacho'
        verbose_name_plural = 'Modalidad de Despacho'
    
    def clean(self):
        self.tipo_despacho = escape(self.tipo_despacho)

        if self.tipo_despacho not in dict(self.MODALIDADDESPACHO_CHOICES).keys():
            raise ValidationError(
                f"{self.tipo_despacho} no es una modalidad de despacho válida"
            )
    
    def __str__(self):
        return f"{self.tipo_despacho}"
    
auditlog.register(ModeloModalidadDespacho)
