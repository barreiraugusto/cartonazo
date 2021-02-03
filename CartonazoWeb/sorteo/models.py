from django.db import models

# Create your models here.

class registoSorteo(models.Model):

    numeros = models.CharField("Numero", max_length=2)
    bolilla = models.CharField("Bolilla", max_length=2)


    class Meta:
        verbose_name = ("registoSorteo")
        verbose_name_plural = ("registoSorteos")
        get_latest_by = ('bolilla')

    def __str__(self):
        return self.numeros

class Carton(models.Model):
    numero_carton = models.CharField("NumeroCarton", max_length=7)
    fila10 = models.CharField("fila10", max_length=2)
    fila11 = models.CharField("fila11", max_length=2)
    fila12 = models.CharField("fila12", max_length=2)
    fila13 = models.CharField("fila13", max_length=2)
    fila14 = models.CharField("fila14", max_length=2)
    fila20 = models.CharField("fila20", max_length=2)
    fila21 = models.CharField("fila21", max_length=2)
    fila22 = models.CharField("fila22", max_length=2)
    fila23 = models.CharField("fila23", max_length=2)
    fila24 = models.CharField("fila24", max_length=2)
    fila30 = models.CharField("fila30", max_length=2)
    fila31 = models.CharField("fila31", max_length=2)
    fila32 = models.CharField("fila32", max_length=2)
    fila33 = models.CharField("fila34", max_length=2)
    fila34 = models.CharField("fila34", max_length=2)

    class Meta:
        verbose_name = ("Carton")
        verbose_name_plural = ("Cartones")
        get_latest_by = ('numero_carton')

    def __str__(self):
        return self.numero_carton
    
    
    