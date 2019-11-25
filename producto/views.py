from .models import *
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'producto/index.html', {})

def contacto(request):
    return render(request, 'producto/contacto.html',{})


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

def nuevo(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST['uname'])
            except User.DoesNotExist:
                user = User.objects.create_user(username= request.POST['uname'],
                                                first_name= request.POST['fname'],
                                                last_name= request.POST['lname'],
                                                password= request.POST['pass'],
                                                email= request.POST['correo'])
                phnum = request.POST['phone']   
                age = request.POST['age']
                newExtendedUser = ExtendedUser(telefono=phnum, edad=age, user=user)
                newExtendedUser.save()
                auth.login(request,user)
                return render(request, 'producto/index.html',{})
        else:
            return render(request , 'producto/nuevo.html', {'error': 'Las contraseñas no coinciden'})
    else:
        return render(request, 'producto/nuevo.html',{})
    

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