from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth.decorators import login_required
from .forms import *



def tienda(request):
    return render(request, 'tienda.html')

def venta(request):
    # Aquí puedes agregar lógica relacionada con la página de ventas si es necesario
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')  # Redirige a la página principal de la tienda o donde desees después de guardar el producto
    else:
        form = ProductoForm()
    return render(request, 'tienda/venta.html', {'form': form})  # Asegúrate de tener un template 'venta.html'



@login_required
def agregar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.vendedor = request.user  # Asignar el vendedor actual
            
            # Calcular el total basado en precio_venta y cantidad
            cantidad = form.cleaned_data['cantidad']
            precio_venta = form.cleaned_data['Producto'].precio
            venta.precio_venta = precio_venta
            venta.cantidad = cantidad
            venta.total = precio_venta * cantidad
            
            venta.save()
            return redirect('tienda')  # Redirigir a la página principal de la tienda después de guardar la venta
    else:
        form = VentaForm()
    
    return render(request, 'tienda/agregar_venta.html', {'form': form})

