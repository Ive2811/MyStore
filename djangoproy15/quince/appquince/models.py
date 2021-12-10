from django.db import models

# Create your models here.
opciones_estado = (
    ("1", "Disponible"),
    ("2", "Reservado"),
    ("3", "Agotado"),
)

opciones_categoria = (
    ("1", "Productos de consumo básico"),
    ("2", "Productos de impulso"),
    ("3", "Productos de urgencia"),
)
class Productos(models.Model):

    # fields of the model
    nombre = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    categoria = models.CharField(
    max_length=20,
        choices=opciones_categoria,
    default='1')
    estado = models.CharField(
    max_length=20,
        choices=opciones_estado,
    default='1')
    imagen = models.ImageField(blank=True,upload_to='media')

