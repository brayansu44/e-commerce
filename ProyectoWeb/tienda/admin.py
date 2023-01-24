from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


class CarroAdmin(admin.ModelAdmin):
     readonly_fields=('created', 'updated')

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
 

admin.site.register(CategoriaProd, CategoriaProdAdmin)    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carro)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ArticuloPedido)
admin.site.register(Perfil)