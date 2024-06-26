from django.shortcuts import render
from home.models import *

# Create your views here.

def servicio(request):
    servicios = Servicio.objects.all()
    context={
        'servicios': servicios
    }
    return render(request,'servicio/servicio.html',context)
