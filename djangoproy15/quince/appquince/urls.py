from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crear/', views.ProductosCreate, name="crear"),
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('listar/', views.lista, name="listar"),
    path('basicos/', views.basicos, name="basicos"),
    path('impulso/', views.impulso, name="impulso"),
    path('urgencia/', views.urgencia, name="urgencia"),
    path('pdf1/', views.prueba1, name="lista1"),
    path('pdf2/', views.prueba2, name="lista2"),
    path('pdf3/', views.prueba3, name="lista3"),
]




