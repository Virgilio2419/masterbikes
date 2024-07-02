from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def exit(request):
    logout(request)
    return redirect('home')


def home(request):
    bicicletas = Bicicleta.objects.all()
    context={
        'bicicletas': bicicletas
    }
    return render(request,'index/home.html',context)

def tienda(request):
    return render(request, 'index/tienda.html')

def preguntas(request):
    return render(request, 'index/preguntas_frecuentes.html')




def tienda(request):
    bicicletas = Bicicleta.objects.all()
    accesorios = Accesorio.objects.all()
    context={
        'bicicletas': bicicletas
        ,'accesorios': accesorios
    }
    return render(request,'tienda/tienda.html',context)
