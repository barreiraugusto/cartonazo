from django.shortcuts import render, redirect, HttpResponse
from cartonazowebapp.forms import FormularioDescarga, CustomUserForm
from cartonazowebapp.models import Usuario
from cartonazowebapp.generarcartones import GenerarCarton
from django.core.mail import EmailMessage, EmailMultiAlternatives
import os
from random import randint
from random import shuffle
import operator
from sorteo.models import Carton, Numeros_sorteados
from django.template.loader import get_template 
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from usuario.models import Usuario
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.core.serializers import serialize


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



def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

@login_required
def controlar_numeros(request):
    
    v1 = False
    v2 = False
    v3 = False
    v4 = False
    v5 = False
    v6 = False
    v7 = False
    v8 = False
    v9 = False
    v10 = False
    v11 = False
    v12 = False
    v13 = False
    v14 = False
    v15 = False
    cartones = Carton.objects.all()
    usuario = request.user.pk
    carton = Carton.objects.filter(participante=usuario)
    num_sorteo = Numeros_sorteados.objects.all()
    lista_num_sorteo = []
    for num in num_sorteo:
        lista_num_sorteo.append(num.numero)
    
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
            celda6 = fila2[0].split(":")[0].strip('\' ')
            num6 = fila2[0].split(":")[1].strip('\' ')
            celda7 = fila2[1].split(":")[0].strip('\' ')
            num7 = fila2[1].split(":")[1].strip('\' ')
            celda8 = fila2[2].split(":")[0].strip('\' ')
            num8 = fila2[2].split(":")[1].strip('\' ')
            celda9 = fila2[3].split(":")[0].strip('\' ')
            num9 = fila2[3].split(":")[1].strip('\' ')
            celda10 = fila2[4].split(":")[0].strip('\' ')
            num10 = fila2[4].split(":")[1].strip('\' ')

            fila3 = fila3.strip('{ }').split(",")
            celda11 = fila3[0].split(":")[0].strip('\' ')
            num11 = fila3[0].split(":")[1].strip('\' ')
            celda12 = fila3[1].split(":")[0].strip('\' ')
            num12 = fila3[1].split(":")[1].strip('\' ')
            celda13 = fila3[2].split(":")[0].strip('\' ')
            num13 = fila3[2].split(":")[1].strip('\' ')
            celda14 = fila3[3].split(":")[0].strip('\' ')
            num14 = fila3[3].split(":")[1].strip('\' ')
            celda15 = fila3[4].split(":")[0].strip('\' ')
            num15 = fila3[4].split(":")[1].strip('\' ')
            if num1 in lista_num_sorteo:
                v1 = True
            if num2 in lista_num_sorteo:
                v2 = True
            if num3 in lista_num_sorteo:
                v3 = True
            if num4 in lista_num_sorteo:
                v4 = True
            if num5 in lista_num_sorteo:
                v5 = True
            if num6 in lista_num_sorteo:
                v6 = True
            if num7 in lista_num_sorteo:
                v7 = True
            if num8 in lista_num_sorteo:
                v8 = True
            if num9 in lista_num_sorteo:
                v9 = True
            if num10 in lista_num_sorteo:
                v10 = True
            if num11 in lista_num_sorteo:
                v11 = True
            if num12 in lista_num_sorteo:
                v12 = True
            if num13 in lista_num_sorteo:
                v13 = True
            if num14 in lista_num_sorteo:
                v14 = True
            if num15 in lista_num_sorteo:
                v15 = True

            dic1 = {celda1:(num1,v1),celda2:(num2,v2),celda3:(num3,v3),celda4:(num4,v4),celda5:(num5,v5)}
            dic2 = {celda6:(num6,v6),celda7:(num7,v7),celda8:(num8,v8),celda9:(num9,v9),celda10:(num10,v10)}
            dic3 = {celda11:(num11,v11),celda12:(num12,v12),celda13:(num13,v13),celda14:(num14,v14),celda15:(num15,v15)}
            content.update(dic1)
            content.update(dic2)
            content.update(dic3)
            #content["Carton_bd"] = carton[0]

    if request.is_ajax():
        #json_data = json.dumps(content, indent=2)
        #json_data = serialize('json', content)
        json_data = json.dumps(content, default=dumper, indent=2)
        return JsonResponse(content)
        #, safe=False)

    return render(request, "control_numeros.html", content)
