from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

#Almacenar los productos
class Producto(models.Model):
    idProducto  = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField(validators=[MaxValueValidator(99999)])
    imagen = models.ImageField(upload_to='images/')
    descripcion = models.TextField(max_length=100)

    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre
    
    
