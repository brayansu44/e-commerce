
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from tienda.models import Carro, Pedido, ArticuloPedido, Producto, Perfil
from django.http.response import JsonResponse


import random

# Create your views here.
def pedidos(request):
    if request.user.is_authenticated:
        longProductos=Carro.objects.filter(user_id=request.user.id)

        datosCarrito=Carro.objects.filter(user_id=request.user.id)
        for articulo in datosCarrito:
            if articulo.producto_qty > articulo.producto.cantidad:
                Carro.objects.delete(id=articulo.id)

        articulosDelCarrito=Carro.objects.filter(user_id=request.user.id)
        precioTotal=0
        for articulo in articulosDelCarrito:
            precioTotal=precioTotal+articulo.producto.precio_descuento * articulo.producto_qty

        perfilUsuario=Perfil.objects.filter(user=request.user).first()

        contexto={"articulos_del_carrito":articulosDelCarrito, "precio_total":precioTotal, "long_productos":len(longProductos), "perfil_usuario":perfilUsuario}    

        return render(request, "pedidos/realizar_pedido.html", contexto)
    else:
        return redirect("Index")    


def realizarPedido(request):
    if request.user.is_authenticated:
        if request.method=='POST':

            usuarioActual=User.objects.filter(id=request.user.id).first()

            if not usuarioActual.first_name:
                usuarioActual.first_name=request.POST.get('nombre')
                usuarioActual.last_name=request.POST.get('apellido')
                usuarioActual.save()

            if not Perfil.objects.filter(user=request.user):
                perfilUsuario=Perfil()
                perfilUsuario.user=request.user
                perfilUsuario.telefono=request.POST.get('telefono')
                perfilUsuario.direccion=request.POST.get('direccion')
                perfilUsuario.ciudad=request.POST.get('ciudad')
                perfilUsuario.estado=request.POST.get('estado')
                perfilUsuario.pais=request.POST.get('pais')
                perfilUsuario.codigo_pin=request.POST.get('codigo_pin')
                perfilUsuario.save()

            nuevoPedido=Pedido()
            nuevoPedido.user=request.user
            nuevoPedido.nombre=request.POST.get('nombre')
            nuevoPedido.apellido=request.POST.get('apellido')
            nuevoPedido.email=request.POST.get('email')
            nuevoPedido.telefono=request.POST.get('telefono')
            nuevoPedido.direccion=request.POST.get('direccion')
            nuevoPedido.ciudad=request.POST.get('ciudad')
            nuevoPedido.estado=request.POST.get('estado')
            nuevoPedido.pais=request.POST.get('pais')
            nuevoPedido.codigo_pin=request.POST.get('codigo_pin')

            nuevoPedido.modo_pago=request.POST.get('modo_pago')
            nuevoPedido.id_pago=request.POST.get('id_pago')

            carro=Carro.objects.filter(user=request.user)
            precio_total_carrito=0
            for articulo in carro:
                precio_total_carrito=precio_total_carrito + articulo.producto.precio_descuento * articulo.producto_qty

            nuevoPedido.precio_total=precio_total_carrito

            numeroSeguimiento='sharma'+str(random.randint(1111111,9999999))
            while Pedido.objects.filter(numero_seguimiento=numeroSeguimiento) is None:
                numeroSeguimiento='sharma'+str(random.randint(1111111,9999999))

            nuevoPedido.numero_seguimiento=numeroSeguimiento
            nuevoPedido.save()

            nuevaOrdenArticulos=Carro.objects.filter(user=request.user)
            for articulo in nuevaOrdenArticulos:
                ArticuloPedido.objects.create(
                    pedido=nuevoPedido,
                    producto=articulo.producto,
                    precio=articulo.producto.precio_descuento,
                    cantidad=articulo.producto_qty
                )

                #disminuir o reducir la cantidad del producto del stock o de la cantidad disponibles
                productoPedido=Producto.objects.filter(id=articulo.producto_id).first() 
                productoPedido.cantidad=productoPedido.cantidad - articulo.producto_qty
                productoPedido.save()

            #Limpiar o borrar el carrito de los usuarios
            Carro.objects.filter(user=request.user).delete() 


            modoPago=request.POST.get('modo_pago')
            if modoPago=="Pagado por Razorpay" or modoPago=="Pagado por PayPal":
                return JsonResponse({'estado':"Su Pedido Se Ha Realizado Correctamente"})
            else:
                messages.success(request, "Su Pedido Se Ha Realizado Correctamente")

        return redirect('Pedidos')
    else:
        return redirect("Index")   

def razorPayCheck(request):
    if request.user.is_authenticated:
        carro = Carro.objects.filter(user=request.user)
        precioTotal=0

        for articulo in carro:
            precioTotal = precioTotal + articulo.producto.precio_descuento * articulo.producto_qty
    
        return JsonResponse({
            'precio_total':precioTotal
        })    

    else:
        return redirect("Index")

def misPedidos(request):
    if request.user.is_authenticated:
        longProductos=Carro.objects.filter(user_id=request.user.id)
        pedidos = Pedido.objects.filter(user=request.user)
        contexto = {'pedidos':pedidos, "long_productos":len(longProductos)}
        return render(request, "pedidos/pedidos.html", contexto)
    else:
        return redirect("Index") 

def detallesPedido(request, no_seguimiento):
    if request.user.is_authenticated:
        longProductos=Carro.objects.filter(user_id=request.user.id)
        pedido = Pedido.objects.filter(numero_seguimiento=no_seguimiento).filter(user=request.user).first()
        articulosPedido = ArticuloPedido.objects.filter(pedido=pedido)
        contexto = {'pedido':pedido, 'articulosPedido':articulosPedido ,"long_productos":len(longProductos)}
        return render(request, "pedidos/detalles_pedido.html", contexto)
    else:
        return redirect("Index") 
