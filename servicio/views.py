from django.shortcuts import render, get_object_or_404, redirect
from home.models import *



# Create your views here.

def servicio(request):
    servicios = Servicio.objects.all()
    context={
        'servicios': servicios
    }
    return render(request,'servicio/servicio.html',context)


def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, id=pk)

    if request.method == 'POST':
        servicio.cod = request.POST.get('cod')
        servicio.marca = request.POST.get('marca')
        servicio.modelo = request.POST.get('modelo')
        servicio.aro = request.POST.get('aro')
        servicio.diagnostico = request.POST.get('diagnostico')
        
        if 'imagen' in request.FILES:
            servicio.imagen = request.FILES['imagen']
        
        servicio.rut = request.POST.get('rut')
        servicio.dv = request.POST.get('dv')
        servicio.nombre_completo = request.POST.get('nombre_completo')
        servicio.telefono = request.POST.get('telefono')
        servicio.mail = request.POST.get('mail')
        servicio.valor_cotizado = request.POST.get('valor_cotizado')
        servicio.valor_repuestos = request.POST.get('valor_repuestos')
        servicio.metodo_pago = request.POST.get('metodo_pago')
        servicio.ingreso = request.POST.get('ingreso')
        servicio.estado = request.POST.get('estado')
        servicio.comentarios = request.POST.get('comentarios')
        servicio.finalizado = request.POST.get('finalizado')
        
        servicio.save()

        return redirect('servicio')

    context = {
        'servicio': servicio,
    }
    return render(request, 'servicio/editar_servicio.html', context)

def elimina(request, pk):
    try:
        servicio = Servicio.objects.get(id=pk)
        nombre_servicio = servicio.nombre_completo  # Guardar el nombre antes de eliminar
        servicio.delete()
        
        mensaje = f'Servicio "{nombre_servicio}" eliminado correctamente.'
    except Servicio.DoesNotExist:
        mensaje = 'El servicio que intentas eliminar no existe.'

    # Recuperar todos los servicios después de la eliminación
    servicios = Servicio.objects.all()
    context = {
        'servicios': servicios,
        'mensaje': mensaje  # Pasar el mensaje al contexto
    }
    
    return render(request, 'servicio/servicio.html', context)
