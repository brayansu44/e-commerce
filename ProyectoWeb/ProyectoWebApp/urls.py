from django.contrib import admin
from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Index"),
    path('prueba', views.prueba, name="Prueba"),
    path('carro', views.carro, name="carro"),
    path('actualizar-carro', views.actualizarCarro, name="actualizarCarro"),
    path('eliminar-carro-articulo', views.eliminarCarroArticulo, name="eliminarCarroArticulo"),
    path('registrar', views.registrarUsuario, name="Registrar"),
    path('logear', views.logear, name="Login"),
    path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)