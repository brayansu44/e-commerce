from xml.dom.minidom import Document
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allProductos, name="Productos"),
    path('lista-productos', views.listaProductosAjax),
    path('search-producto', views.searchProducto, name="searchproducto"),
]