from django.contrib import admin
from sorteo.models import registoSorteo, Carton, Numeros_sorteados

# Register your models here.


admin.site.register(registoSorteo)
admin.site.register(Carton)
admin.site.register(Numeros_sorteados)
