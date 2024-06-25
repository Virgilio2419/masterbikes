from django.shortcuts import render, redirect
from .models import Vehiculo

def inicio(request):
    return render(request, 'core/inicio.html')

def lista(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, 'core/lista.html', context)

def elimina(request, pk):
    try:
        vehiculo = Vehiculo.objects.get(id=pk)
        vehiculo.delete()
        mensaje = "Vehiculo eliminado con exito!"
    except Vehiculo.DoesNotExist:
        mensaje = "El vehiculo no existe."

    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos,
        'mensaje': mensaje
    }
    return render(request, 'core/lista.html', context)

def agrega(request):
    if request.method == 'POST':
        vehiculo = Vehiculo.objects.create(
            marca=request.POST.get("marca"),
            modelo=request.POST.get("modelo"),
            anio=request.POST.get("anio"),
            precio=request.POST.get("precio"),
            hp=request.POST.get("hp"),
            color=request.POST.get("color")
        )
        vehiculo.save()
        return redirect('lista')
    else:
        return render(request, 'core/agrega.html')
    
def nuevo(request):
    return render(request, 'core/agrega.html')


def modificar(request, pk):
    vehiculo = Vehiculo.objects.get(id=pk)
    if request.method == 'POST':
        vehiculo.marca = request.POST.get("marca")
        vehiculo.modelo = request.POST.get("modelo")
        vehiculo.anio = request.POST.get("anio")
        vehiculo.precio = request.POST.get("precio")
        vehiculo.hp = request.POST.get("hp")
        vehiculo.color = request.POST.get("color")
        vehiculo.save()
        return redirect('lista')
    else:
        context = {
            'vehiculo': vehiculo
        }
        return render(request, 'core/modificar.html', context)
