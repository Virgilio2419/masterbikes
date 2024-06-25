from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    bicicletas = Bicicleta.objects.all()
    context={
        'bicicletas': bicicletas
    }
    return render(request,'index/home.html',context)

