from django.db import models
from Aplicaciones.Impresoras.models import Impresora
# Create your models here.

class Mantenimiento(models.Model):
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    tecnico = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    informe_pdf = models.BinaryField(blank=True, null=True)  # Para almacenar el PDF como binario

    def __str__(self):
        return f"Mantenimiento {self.id} - {self.impresora}"