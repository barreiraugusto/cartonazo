from django.contrib import admin
from cartonazowebapp.models import Usuario
from sorteo.models import registoSorteo, Carton

# Register your models here.


admin.site.register(Usuario)
admin.site.register(registoSorteo)
admin.site.register(Carton)
