from django.urls import path, include
from producto import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', views.index, name='index'),
    path('producto/contacto', views.contacto, name='contacto'),
    path('producto/productos', views.productos, name='productos'),
    path('producto/<int:pk>/', views.infoProducto, name='infoProducto'),
    path('producto/nuevo',views.nuevo, name='nuevo'),
    path('producto/login2', views.login2, name='login2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('producto/password_reset', PasswordResetView.as_view(template_name='producto/password_reset.html', email_template_name='producto/password_reset_email.html'), name='password_reset'),
    path('producto/password_reset/done', PasswordResetDoneView.as_view(template_name='producto/password_reset_done.html'), name='password_reset_done'),
    path('producto/password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='producto/password_reset_confirm.html'), name='password_reset_confirm'),
    path('producto/password_reset/complete', PasswordResetCompleteView.as_view(template_name='producto/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
