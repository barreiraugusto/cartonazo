from django.shortcuts import render, redirect, HttpResponse
from cartonazowebapp.forms import FormularioDescarga, CustomUserForm
from cartonazowebapp.models import Usuario
from cartonazowebapp.generarcartones import GenerarCarton
from django.core.mail import EmailMessage, EmailMultiAlternatives
import os
from random import randint
from random import shuffle
import operator
from sorteo.models import Carton
from django.template.loader import get_template 
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from usuario.models import Usuario
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    usuario = request.user.username
    return render(request, 'home.html', {'nombre':usuario})

@login_required
def DescargaCarton(request):
    usuario = request.user.pk
    carton = Carton.objects.filter(participante=usuario)
    if len(carton) == 1:
        return render(request, 'error.html', {"mensaje_error":"EL DOCUMENTO {} YA ESTA REGISTRADO!!".format(request.user.documento)})
    formulario_descarga = FormularioDescarga(request.POST)
    if request.method == "POST" and formulario_descarga.is_valid():
        nombre = request.user.username
        email = request.user.email
        carton = GenerarCarton(request.user)
        Carton_bd = Carton.objects.latest()
        fila0 = carton["fila00"]
        fila1 = carton["fila01"]
        fila2 = carton["fila02"]
        content = {"nombre":nombre, "email":email}
        content.update(fila0)
        content.update(fila1)
        content.update(fila2)
        content["Carton_bd"] = Carton_bd.numero_carton
        plaintext = get_template('email.txt')
        htmly = get_template('email.html')
        subject, from_email, to = 'Nueva inscripcion', 'barreiraugusto@gmail.com', '{}'.format(email)
        text_content = plaintext.render(content) 
        html_content = htmly.render(content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to]) 
        msg.attach_alternative(html_content, "text/html") 
        msg.send()
        return render(request, "gracias.html", content)
    else:
        formulario_descarga = FormularioDescarga()
    return render(request, "descarga.html", {"formulario_descarga":formulario_descarga})

def registro_usuario(request):
    data = {'form':CustomUserForm()}
    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, 'registration/registro.html', data)


@login_required
def controlar_numeros(request):
    cartones = Carton.objects.all()
    usuario = request.user.pk
    carton = Carton.objects.filter(participante=usuario)
    if len(carton) == 0:
        return render(request, 'error.html', {"mensaje_error":"NO TIENEN CARTON GENERALO!!"})
    content = {"nombre":request.user.username, "email":request.user.email}
    for car in cartones:
        if car == carton[0]: 
            fila1 = car.fila1
            fila2 = car.fila2
            fila3 = car.fila3
            fila1 = fila1.strip('{ }').split(",")
            celda1 = fila1[0].split(":")[0].strip('\' ')
            num1 = fila1[0].split(":")[1].strip('\' ')
            celda2 = fila1[1].split(":")[0].strip('\' ')
            num2 = fila1[1].split(":")[1].strip('\' ')
            celda3 = fila1[2].split(":")[0].strip('\' ')
            num3 = fila1[2].split(":")[1].strip('\' ')
            celda4 = fila1[3].split(":")[0].strip('\' ')
            num4 = fila1[3].split(":")[1].strip('\' ')
            celda5 = fila1[4].split(":")[0].strip('\' ')
            num5 = fila1[4].split(":")[1].strip('\' ')

            fila2 = fila2.strip('{ }').split(",")
            celda12 = fila2[0].split(":")[0].strip('\' ')
            num12 = fila2[0].split(":")[1].strip('\' ')
            celda22 = fila2[1].split(":")[0].strip('\' ')
            num22 = fila2[1].split(":")[1].strip('\' ')
            celda32 = fila2[2].split(":")[0].strip('\' ')
            num32 = fila2[2].split(":")[1].strip('\' ')
            celda42 = fila2[3].split(":")[0].strip('\' ')
            num42 = fila2[3].split(":")[1].strip('\' ')
            celda52 = fila2[4].split(":")[0].strip('\' ')
            num52 = fila2[4].split(":")[1].strip('\' ')

            fila3 = fila3.strip('{ }').split(",")
            celda13 = fila3[0].split(":")[0].strip('\' ')
            num13 = fila3[0].split(":")[1].strip('\' ')
            celda23 = fila3[1].split(":")[0].strip('\' ')
            num23 = fila3[1].split(":")[1].strip('\' ')
            celda33 = fila3[2].split(":")[0].strip('\' ')
            num33 = fila3[2].split(":")[1].strip('\' ')
            celda43 = fila3[3].split(":")[0].strip('\' ')
            num43 = fila3[3].split(":")[1].strip('\' ')
            celda53 = fila3[4].split(":")[0].strip('\' ')
            num53 = fila3[4].split(":")[1].strip('\' ')

            dic1 = {celda1:num1,celda2:num2,celda3:num3,celda4:num4,celda5:num5}
            dic2 = {celda12:num12,celda22:num22,celda32:num32,celda42:num42,celda52:num52}
            dic3 = {celda13:num13,celda23:num23,celda33:num33,celda43:num43,celda53:num53}
            content.update(dic1)
            content.update(dic2)
            content.update(dic3)
            content["Carton_bd"] = carton[0]

    return render(request, "control_numeros.html", content)
