from django.shortcuts import render
from cartonazowebapp.forms import FormularioDescarga
from cartonazowebapp.models import Usuarios
from cartonazowebapp.generarcartones import GenerarCarton
from cartonazowebapp.miscartones import IngresarCarton
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
        carton = GenerarCarton()
        
        nombre = datos_usuario['nombre']
        apellido = datos_usuario['apellido']
        direccion = datos_usuario['direccion']
        documento = datos_usuario['documento']
        email = datos_usuario['email']
        telefono = datos_usuario['telefono']
        
        datos_db = Usuarios.objects.all()
        Carton_bd = Carton.objects.latest()

        se_encuentra = False

        for valor in datos_db:
            if valor.documento == documento:
                return render(request, "error.html", {"documento":documento})
            else:
                se_encuentra = False
        
        if se_encuentra == False:          
            ingreso_usuario = Usuarios(nombre=nombre, apellido=apellido, direccion=direccion, documento=documento,
            email=email, telefono=telefono)
            ingreso_usuario.save()

            IngresarCarton(carton)

            fila0 = carton["fila00"]
            fila1 = carton["fila01"]
            fila2 = carton["fila02"]
            content = {"nombre":nombre, "email":email}
            content.update(fila0)
            content.update(fila1)
            content.update(fila2)
            content["Carton_bd"] = Carton_bd.numero_carton

            #email_confirmacion = EmailMultiAlternatives("Nueva inscripcion",
            # """Nombre: {}\n
            # Apellido: {}\n
            # Direccion: {}\n
            #Documento: {}\n
            # E-mail: {}\n 
            # Telefono: {}\n 
            # Carton N°:{}\n 
            # Numeros: """.format(nombre, apellido, direccion, documento, email, telefono, Carton_bd),
            # "", [email],["barreiraugusto@gmail.com"], reply_to=[email])
            #email_confirmacion.attach_file('C:/Users/Augusto/Desktop/ProyectosDjango/CARTONAZOWEB/CartonazoWeb/cartonazowebapp/static/img/carton.jpg')
            


            plaintext = get_template('email.txt')
            htmly = get_template('email.html')

            subject, from_email, to = 'Nueva inscripcion', 'barreiraugusto@gmail.com', '{}'.format(email)
            
            #text_content = """Nombre: {}\n
             #Apellido: {}\n
             #Direccion: {}\n
             #Documento: {}\n
             #E-mail: {}\n 
             #Telefono: {}\n 
             #Carton N°:{}\n 
             #Numeros: """.format(nombre, apellido, direccion, documento, email, telefono, Carton_bd)
                      
            #html_content = """<p><strong>Nombre: </strong>{}</p> 
             #<p><strong>Apellido: </strong>{}</p>
             #<p><strong>Direccion: </strong>{}</p>
             #<p><strong>Documento: </strong>{}</p>
             #<p><strong>E-mail: </strong>{}</p>
             #<p><strong>Telefono: </strong>{}</p>
             #<p><strong>Carton N°: </strong>{}</p>
             #<p><strong>Numeros:</strong</p>""".format(nombre, apellido, direccion, documento, email, telefono, Carton_bd)
           
            text_content = plaintext.render(content) 
            html_content = htmly.render(content)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to]) 
            msg.attach_alternative(html_content, "text/html") 
            msg.send()

            
            return render(request, "gracias.html", content)

    else:
        formulario_descarga = FormularioDescarga()

    return render(request, "descarga.html", {"formulario_descarga":formulario_descarga})

