from django.shortcuts import render, redirect
import random
from random import randint
from sorteo.models import registoSorteo, Numeros_sorteados
from sorteo.bolillero import GenerarBolillero
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

@staff_member_required
def Sorteo(request):
    if request.method=="POST":
        nuevoSorteo = "no"
        consulta = len(registoSorteo.objects.all())
        if consulta == 0:
            bolillero = GenerarBolillero()
            nuevoSorteo = "no"
            consulta = len(registoSorteo.objects.all())
        primeraBolilla = registoSorteo.objects.latest()
        nueva_sorteada = Numeros_sorteados.objects.create(numero= primeraBolilla)
        primeraBolilla.delete()
        restan = consulta - 1 
        if restan == 0:
            nuevoSorteo = "ok"
            nuevaRecarga = "no"
        else:
            nuevoSorteo = "no"
            nuevaRecarga = "no"
        return render(request, "sorteo.html", {"numero":primeraBolilla, "restan": restan, "nuevoSorteo": nuevoSorteo, "nuevaRecarga":nuevaRecarga})
    else:
        consulta = len(registoSorteo.objects.all())
        if consulta == 0:
            nuevaRecarga = "ok"
            nuevoSorteo = "ok"
        else:
            nuevaRecarga = "no"
            nuevoSorteo = "no"
        return render(request, "sorteo.html", {"nuevaRecarga":nuevaRecarga, "nuevoSorteo":nuevoSorteo})