from django.shortcuts import render
from cartonazowebapp.forms import FormularioDescarga
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

# Create your views here.

def DescargaCarton(request):

    formulario_descarga = FormularioDescarga(request.POST)

    if request.method == "POST" and formulario_descarga.is_valid():

        datos_usuario = formulario_descarga.cleaned_data
        
        
        nombre = datos_usuario['nombre']
        apellido = datos_usuario['apellido']
        direccion = datos_usuario['direccion']
        documento = datos_usuario['documento']
        email = datos_usuario['email']
        telefono = datos_usuario['telefono']
        
        datos_db = Usuario.objects.all()

        

        se_encuentra = False

        for valor in datos_db:
            if valor.documento == documento:
                return render(request, "error.html", {"documento":documento})
            else:
                se_encuentra = False
        
        if se_encuentra == False:          
            ingreso_usuario = Usuario(nombre=nombre, apellido=apellido, direccion=direccion, documento=documento,
            email=email, telefono=telefono)
            ingreso_usuario.save()

            carton = GenerarCarton(ingreso_usuario)

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

