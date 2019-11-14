from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'producto/index.html', {})

def contacto(request):
    return render(request, 'producto/contacto.html',{})

def login(request):
    return render(request, 'producto/login.html',{})

def productos(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()

    if request.POST.get('nombreMarca'):
        nombre=request.POST.get('nombreMarca')
        marcas = Marca.objects.filter(nombre=nombre).get()
        productos = Producto.objects.filter(marcaId=marcas.idMarca)
    elif request.POST.get('menor'):
        productos = Producto.objects.order_by('precio')
    elif request.POST.get('mayor'):
        productos = Producto.objects.order_by('-precio')
    else:
        productos = Producto.objects.all()

    marcas = Marca.objects.all()

    return render(request, 'producto/productos.html', {'productos' : productos, 'marcas' : marcas})

def infoProducto(request, pk):
    productos = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/infoProducto.html', {'producto' :productos })

