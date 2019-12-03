from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

#Almacenar los productos
class Producto(models.Model):
    idProducto  = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(validators=[MaxValueValidator(99999)])
    imagen = models.ImageField(upload_to='images/')
    descripcion = models.TextField(max_length=350)
    marcaId = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True)
    

    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def guardar(self):
        self.save()
    
    def __str__(self):
        return self.nombre

class ExtendedUser(models.Model):
    telefono = models.IntegerField(validators=[MaxValueValidator(999999999)])
    edad = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)


