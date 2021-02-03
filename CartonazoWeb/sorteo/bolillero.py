import random
from random import randint
from sorteo.models import registoSorteo


def GenerarBolillero ():
    numeros = []
    bolilla = 0
    while len(numeros)<50:
        numero_gen = randint(1,90)
        numeros.append(numero_gen)
        if numeros.count(numero_gen) == 2:
            numeros.remove(numero_gen)
    for numero in numeros:
        bolilla = bolilla + 1
        nuevo = registoSorteo.objects.create(numeros=numero, bolilla = bolilla)
    
    return numeros


