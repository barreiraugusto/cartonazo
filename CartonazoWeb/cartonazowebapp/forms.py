from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class FormularioDescarga(forms.Form):
    pass
    
class CustomUserForm(UserCreationForm):
    documento = forms.CharField( label="Documento", max_length=50, required=True)
    direccion = forms.CharField( label="Direccion", max_length=50, required=True)
    email = forms.EmailField( label="Email", max_length=50, required=True)
    telefono = forms.CharField(label="Telefono", max_length=11, required=True)


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "documento", "direccion", "telefono", "email", "password1", "password2")

def save(self, commit=True):
    user = super(CustomUserForm, self).save(commit=False)
    user.documento = self.cleaned_data["documento"]
    user.apellido = self.cleaned_data["apellido"]
    user.direccion = self.cleaned_data["direccion"]
    user.email = self.cleaned_data["email"]
    user.telefono = self.cleaned_data["telefono"]
    if commit:
        user.save()
    return user