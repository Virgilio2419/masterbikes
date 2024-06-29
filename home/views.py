from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required




# Create your views here.

def home(request):
    bicicletas = Bicicleta.objects.all()
    context={
        'bicicletas': bicicletas
    }
    return render(request,'index/home.html',context)


def tienda(request):
    return render(request, 'index/tienda.html')

@login_required
def preguntas(request):
    return render(request, 'index/preguntas_frecuentes.html')




