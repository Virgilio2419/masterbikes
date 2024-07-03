from django.shortcuts import render,redirect
from home.models import *
from .forms import VentaForm
# Create your views here.

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')  # Redirige a la lista de clientes
    else:
        form = VentaForm()

    productos = Producto.objects.all()
    clientes = Cliente.objects.all()

    context = {
        'form': form,
        'productos': productos,
        'clientes': clientes,
    }

    return render(request, 'crear_venta.html', context)

def ventas(request):
    return render(request, 'tienda/tienda.html')