from django.urls import path
from producto import views

urlpatterns = [
    path('', views.index, name='index'),
]
