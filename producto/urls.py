from django.urls import path
from producto import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/contacto', views.contacto, name='contacto'),
    path('producto/login', views.login, name='login'),
]
