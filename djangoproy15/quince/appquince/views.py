from django import forms
from django.shortcuts import render, redirect


from .forms import ProductosForm,  LaForm
from .models import Productos
# Create your views here.
from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from xhtml2pdf import pisa


from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.utils import ImageReader
from datetime            import datetime


from . utils import render_to_pdf



def prueba1(request):
    productos =Productos.objects.all().filter(categoria='1')
    data={
    'productos': productos
    }
    pdf=render_to_pdf('categoria1.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def prueba2(request):
    producto =Productos.objects.all().filter(categoria='2')
    data={
    'producto': producto
    }
    pdf=render_to_pdf('categoria2.html', data)
    return HttpResponse(pdf, content_type='application/pdf')    

def prueba3(request):
    producto =Productos.objects.all().filter(categoria='3')
    data={
    'producto': producto
    }
    pdf=render_to_pdf('categoria3.html', data)
    return HttpResponse(pdf, content_type='application/pdf')    




def index(request):
    productos_basicos = Productos.objects.filter(categoria='1').count()
    productos_impulso = Productos.objects.filter(categoria='2').count()
    productos_urgencia = Productos.objects.filter(categoria='3').count()

    cuantos = Productos.objects.all().count()

    contexto = {
        'cuantos': cuantos,
        'productos_basicos': productos_basicos,
        'productos_impulso': productos_impulso,
        'productos_urgencia': productos_urgencia,

    }

    return render(request, "index.html", contexto)


def ProductosCreate(request):
    if request.method == "POST":
        form = ProductosForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('index')
            except:
                pass
    else:
        form = ProductosForm()
    return render(request, 'crear.html', {'form': form})

def login(request):
    _message = 'Por favor, inicie sesión.'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('index')
            else:
                _message = 'Su cuenta no está activa.'
        else:
            _message = 'Inicio de sesión inválido, por favor intente nuevamente.'
    context = {'message': _message}
    return render(request, 'login.html', context)
    
    



def lista(request):
    productos=Productos.objects.all()
    contexto={'productos':productos}
    return render(request,'lista.html', contexto)

def basicos(request):
    productos=Productos.objects.all().filter(categoria='1')
    diccionario={'productos':productos}
    return render(request, 'basicos.html',diccionario)

def impulso(request):
    productos=Productos.objects.all().filter(categoria='2')
    diccionario={'productos':productos}
    return render(request, 'impulso.html',diccionario)

def urgencia(request):
    productos=Productos.objects.all().filter(categoria='3')
    diccionario={'productos':productos}
    return render(request, 'urgencia.html',diccionario)


