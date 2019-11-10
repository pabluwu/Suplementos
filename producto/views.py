from django.shortcuts import render
from .models import Producto
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
    return render(request, 'producto/productos.html', {'productos' : productos})

