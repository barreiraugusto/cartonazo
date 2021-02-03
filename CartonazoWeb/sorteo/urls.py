from django.urls import path
from . import views
urlpatterns = [
    path('/', views.Sorteo, name="Sorteo"),
]
