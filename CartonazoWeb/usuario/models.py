from django.contrib.auth.models import  AbstractUser
from django.db import models

# Create your models here.


class Usuario(AbstractUser):
    direccion = models.CharField(max_length=30)
    documento = models.CharField(max_length=8)
    telefono = models.CharField(max_length=11)

    class Meta():
        get_latest_by = "documento"

