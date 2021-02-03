from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    documento = models.CharField(max_length=8)
    email = models.EmailField()
    telefono = models.CharField(max_length=11)

