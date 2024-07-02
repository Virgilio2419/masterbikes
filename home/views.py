from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    bicicletas = Bicicleta.objects.all()
    context={
        'bicicletas': bicicletas
    }
    return render(request,'index/home.html',context)

def preguntas(request):
    return render(request, 'index/preguntas_frecuentes.html')

def servicio(request):
    
    return render(request,'servicio/servicio.html')

def tienda(request):
    bicicletas = Bicicleta.objects.all()
    accesorios = Accesorio.objects.all()
    context={
        'bicicletas': bicicletas
        ,'accesorios': accesorios
    }
    return render(request,'tienda/tienda.html',context)
