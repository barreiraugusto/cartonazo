from django import forms

class FormularioDescarga(forms.Form):
    nombre = forms.CharField( label="Nombre",max_length=30)
    apellido = forms.CharField( label="Apellido", max_length=50)
    direccion = forms.CharField( label="Direccion", max_length=50)
    documento = forms.CharField( label="Documento", max_length=50)
    email = forms.EmailField( label="Email", max_length=50)
    telefono = forms.CharField(label="Telefono", max_length=11)