from django.shortcuts import render, redirect
from .models import Producto
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

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

def nuevo(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    form.fields['username'].help_text = 'Nombre de Usuario'
    form.fields['password1'].help_text = 'Contraseña'
    form.fields['password2'].help_text = 'Repita Contraseña'
    return render(request, 'producto/nuevo.html', {'form':form})
    

def login2(request):
     
    form = AuthenticationForm()
    if request.method == "POST":
        
        form = AuthenticationForm(data=request.POST)
       
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

          
            user = authenticate(username=username, password=password)

          
            if user is not None:
                
                do_login(request, user)
                
                return redirect('/')

  
    return render(request, "producto/login2.html", {'form': form})