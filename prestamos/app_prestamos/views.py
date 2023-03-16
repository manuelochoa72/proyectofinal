from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Cliente, Prestamo
from django.urls import reverse

# Create your views here.
def index(request):
    # Consulta la base de dartos el nombre de la tabla clientes
    # SQL: Select*from cliente orden by Nombre
    tolal_clientes=Cliente.objects.order_by('-Nombre')
    salida_clientes=', ' .join([
        cliente.Nombre for cliente in tolal_clientes
    ])

    template =loader.get_template('app_prestamos/index.html')
    contexto = {
        'total_clientes': tolal_clientes
    }

    return HttpResponse(template.render(contexto, request))

def detalle(request, id_cliente):
    try:
        # Select *  from cliente where id= id_cliente  
        cliente = Cliente.objects.get(pk=id_cliente) 

        template = loader.get_template('app_prestamos/detalle.html')
        contexto = {
            'cliente':cliente
        }

        return HttpResponse(template.render(contexto, request))
    except Cliente.DoesNotExist: # para detectar el error de cliente no exista
        raise Http404("El cliente no existe")

def resultados (request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    template = loader.get_template('app_prestamos/resultados.html')
    contexto = {
        'cliente':cliente
    }
    return HttpResponse(template.render(contexto, request))

def prestamos(request, id_cliente):
    return HttpResponse(f"Prestamos de: {id_cliente}")

def agregar_prestamo(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    try:
        monto_seleccionado = Prestamo.objects.get(pk=request.POST["monto"])
        num_prestamo_sel = Prestamo.objects.get(pk=request.POST["num_prestamo"]) 
        fecha_seleccionada = Prestamo.objects.get(pk=request.POST["fecha"])
        interes_seleccionado = Prestamo.objects.get(pk=request.POST["interes"])
        total_pago_seleccionado = Prestamo.objects.get(pk=request.POST["total_pago"])
    except(KeyError, Prestamo.DoesNotExist):
        template_detalle = loader.get_template("app_prestamos/detalle.html")
        contexto = {
            'cliente':cliente,
            'mensaje_error': "Falta un dato" 
        }
        return HttpResponse(template_detalle.render(contexto, request))
    else: 
        
        monto_seleccionado.save()
        num_prestamo_sel.save()
        fecha_seleccionada.save()
        interes_seleccionado.save()
        total_pago_seleccionado.save()

        return HttpResponseRedirect(reverse('app_prestamos:resultados', args=(cliente.id,)))


