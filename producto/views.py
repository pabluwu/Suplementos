from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'producto/index.html', {})

def contacto(request):
    return render(request, 'producto/contacto.html',{})

def login(request):
    return render(request, 'producto/login.html',{})