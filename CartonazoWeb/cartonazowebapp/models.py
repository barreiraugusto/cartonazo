from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    documento = models.CharField(max_length=8)
    email = models.EmailField()
    telefono = models.CharField(max_length=11)

    def __str__(self):
        return "Nombre: {} {}, DNI: {}".format(self.nombre, self.apellido, self.documento)

