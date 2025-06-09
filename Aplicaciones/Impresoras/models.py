from django.db import models

# Create your models here.
class Impresora(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    fecha_adquisicion = models.DateField()
    imagen = models.BinaryField(blank=True, null=True)  # Para almacenar la imagen como binario

    def __str__(self):
        return f"{self.marca} {self.modelo}"