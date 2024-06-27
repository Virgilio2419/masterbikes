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
                # Manejo del campo finalizado
        finalizado = request.POST.get('finalizado')
        if finalizado:
            servicio.finalizado = finalizado
        else:
            servicio.finalizado = None
        
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


def agrega_servicio(request):
    if request.method == 'POST':
        cod_cliente = request.POST.get('cod')
        cliente_obj = get_object_or_404(cliente, id=cod_cliente)

        if cliente_obj:
            marca = request.POST.get('marca')
            modelo = request.POST.get('modelo')
            aro = request.POST.get('aro')
            diagnostico = request.POST.get('diagnostico')
            imagen = request.FILES.get('imagen')
            rut = request.POST.get('rut')
            dv = request.POST.get('dv')
            nombre_completo = request.POST.get('nombre_completo')
            telefono = request.POST.get('telefono')
            mail = request.POST.get('mail')
            valor_cotizado = request.POST.get('valor_cotizado')
            valor_repuestos = request.POST.get('valor_repuestos')
            metodo_pago = request.POST.get('metodo_pago')
            ingreso = request.POST.get('ingreso')
            estado = request.POST.get('estado')
            comentarios = request.POST.get('comentarios')
            finalizado = request.POST.get('finalizado') if request.POST.get('finalizado') else None

            servicio = Servicio.objects.create(
                cod=cliente_obj,
                marca=marca,
                modelo=modelo,
                aro=aro,
                diagnostico=diagnostico,
                imagen=imagen,
                rut=rut,
                dv=dv,
                nombre_completo=nombre_completo,
                telefono=telefono,
                mail=mail,
                valor_cotizado=valor_cotizado,
                valor_repuestos=valor_repuestos,
                metodo_pago=metodo_pago,
                ingreso=ingreso,
                estado=estado,
                comentarios=comentarios,
                finalizado=finalizado
            )

            return redirect('servicio')
        else:
            # Cliente no encontrado, mostrar mensaje de error y redirigir al formulario
            mensaje_error = 'El cliente no existe. Agrega primero al cliente antes de asignarle un servicio.'
            metodo_pago_choices = Servicio.METODO_PAGO_CHOICES
            estado_choices = Servicio.estados_CHOICES

            context = {
                'metodo_pago_choices': metodo_pago_choices,
                'estado': estado_choices,
                'mensaje_error': mensaje_error
            }

            return render(request, 'servicio/agrega_servicio.html', context)

    # Si no es un POST, simplemente renderiza el formulario vacío
    metodo_pago_choices = Servicio.METODO_PAGO_CHOICES
    estado_choices = Servicio.estados_CHOICES

    context = {
        'metodo_pago_choices': metodo_pago_choices,
        'estado': estado_choices,
    }

    return render(request, 'servicio/agrega_servicio.html', context)

