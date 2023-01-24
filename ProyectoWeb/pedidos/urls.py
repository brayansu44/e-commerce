from xml.dom.minidom import Document
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pedidos, name="Verificar"),
    path('realizar_pedido', views.realizarPedido, name="realizarPedido"),
    path('proceder-a-pagar', views.razorPayCheck),
    path('mis-pedidos', views.misPedidos, name="Pedidos"),
    path('detalles-pedido/<str:no_seguimiento>', views.detallesPedido, name="detallesPedido"),
]