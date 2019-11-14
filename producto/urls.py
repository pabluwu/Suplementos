from django.urls import path
from producto import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('producto/contacto', views.contacto, name='contacto'),
    path('producto/productos', views.productos, name='productos'),
    path('producto/<int:pk>/', views.infoProducto, name='infoProducto'),
    path('producto/nuevo',views.nuevo, name='nuevo'),
    path('producto/login2', views.login2, name='login2'),

] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
