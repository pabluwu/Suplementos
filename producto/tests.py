from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your tests here.

class TestUsuario(TestCase):
    def setUp(self):
        user = User.objects.create_user(username= 'jose123',
                                                first_name= 'jose',
                                                last_name= 'perez',
                                                password= '1jose2',
                                                email= 'jose@jose.com')
        phnum = 123   
        age= datetime.today()
        newExtendedUser = ExtendedUser(telefono=phnum, edad=age, user=user)

    def testUsuarioCreado(self):
        exists = User.objects.filter(username='jose123').exists()
        self.assertEqual(exists, True)

class TestProducto(TestCase):
    def setUp(self):
        marca = Marca.objects.create(idMarca=1999, nombre='Prueba1')
        producto= Producto.objects.create(idProducto=512, nombre='PruebaProducto', precio=19999, descripcion='prueba unitaria', marcaId=marca.idMarca)
        
    def testProductoMarcaCreado(self):
        marcaExiste = Marca.objects.filter(idMarca=1999).exists()
        productoExiste = Producto.objects.filter(idProducto=512).exists()

        self.assertEqual(marcaExiste, True)
        self.assertEqual(productoExiste, True)

class TestProducto(TestCase):
    def setUp(self):
        marca = Marca.objects.create(idMarca=1999, nombre='Prueba1')
        producto= Producto.objects.create(idProducto=512, nombre='PruebaProducto', precio=19999, descripcion='prueba unitaria', marcaId=marca.idMarca)

    def testProductoMarcaEliminar(self):
        marca = Marca.objects.get(idMarca=1999)
        producto = Producto.objects.get(idProducto=512)
        producto.delete()
        marca.delete()

        marcaExiste = Marca.objects.filter(idMarca=1999).exists()
        productoExiste = Producto.objects.filter(idProducto=512).exists()
        self.assertEqual(marcaExiste, False)
        self.assertEqual(productoExiste, False)