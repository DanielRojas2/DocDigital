from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.utils.timezone import now

from auditlog.registry import auditlog

class ModeloImportador(models.Model):
    TIPO_IMPORTADOR_CHOICES = (
        ('unipersonal', 'Unipersonal'),
        ('empresa', 'Empresa')
    )
    
    nombre_importador = models.CharField(
        max_length=50, blank=False, null=False, unique=True
    )
    nit_importador = models.CharField(
        max_length=20, blank=False, null=False, unique=True
    )
    tipo_importador = models.CharField(
        max_length=11, blank=False, null=False,
        choices=TIPO_IMPORTADOR_CHOICES,
        validators=[
            RegexValidator(
                regex='^(unipersonal|empresa)$',
                message='Tipo de importador no válido'
            )
        ]
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Importador'
        verbose_name_plural = 'Importadores'

    def clean(self):
        self.tipo_importador = escape(self.tipo_importador)

        if self.tipo_importador not in dict(self.TIPO_IMPORTADOR_CHOICES).keys():
            raise ValidationError(
                f"{self.tipo_importador} no es un tipo de importador válido"
            )
    
    def __str__(self):
        return f"Importador: {self.nombre_importador}\nNIT: {self.nit_importador}"

auditlog.register(ModeloImportador)
