from http.client import HTTPResponse
from django.shortcuts import render, redirect
from tienda.models import Producto, Carro
from django.http.response import JsonResponse
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.



def index(request):
    long_productos=Carro.objects.filter(user_id=request.user.id)
    productos=Producto.objects.all()
    return render(request, "ProyectoWebApp/index.html", {"productos":productos, "long_productos":len(long_productos)})

def prueba(request):
    return render(request, "ProyectoWebApp/carousel.html")

def carro(request):

    long_productos=Carro.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Producto.objects.get(id=prod_id)
            if product_check:
                if Carro.objects.filter(producto_id=prod_id, user_id=request.user.id):   
                    return JsonResponse({'estado':"El Producto ya se encuentra en el carrito", 'contador':len(long_productos)})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.cantidad >= prod_qty:
                        Carro.objects.create(user_id=request.user.id, producto_id=prod_id, producto_qty=prod_qty)
                        long_productos2=Carro.objects.filter(user_id=request.user.id)
                        return JsonResponse({'estado':"Producto Añadido Al Carrito", 'contador':len(long_productos2)})
                    else:
                        if product_check.cantidad == 1:
                            return JsonResponse({'estado':"Solamente queda una unidad disponible", 'contador':len(long_productos)})
                        else:
                            return JsonResponse({'estado':"Solamente quedan " + str(product_check.cantidad) + " unidades disponibles", 'contador':len(long_productos)})
            else:
                return JsonResponse({'estado':"No se encontro el producto"})
        else:
            return JsonResponse({'estado':"Inicia Sesiòn Para Continuar"})      

def actualizarCarro(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Carro.objects.filter(producto_id=prod_id, user_id=request.user.id):
            prod_qty = int(request.POST.get('product_qty'))
            carro = Carro.objects.get(producto_id=prod_id, user_id=request.user.id)
            carro.producto_qty = prod_qty
            carro.save()

            return JsonResponse({'estado':"Actualizado Con Exito"})

    return redirect('/')        

def eliminarCarroArticulo(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Carro.objects.filter(producto_id=prod_id, user_id=request.user.id):
            carro_articulo = Carro.objects.get(producto_id=prod_id, user_id=request.user.id)
            carro_articulo.delete()

            return JsonResponse({'estado':"Eliminado Con Exito"})

def registrarUsuario(request):
     if request.method=="POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]
        usuario=request.POST["usuario"]
        password=make_password(request.POST["contraseña"])
        
        user_register=User(first_name=nombre, last_name=apellido, email=email, username=usuario, password=password)
        user_register.save()

        login(request, user_register)
        messages.success(request, "Ha Iniciado Sesión Con Éxito")
        return redirect('Index')
        
      

def logear(request):
    if request.method=="POST":
        usuario=request.POST["usuario"]
        password=request.POST["contraseña"]
        user=authenticate(username=usuario, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ha Iniciado Sesión Con Éxito")
            return redirect('Index')
        else:
            messages.error(request, "Nombre De Usuario o Contraseña No Valido")    
            return redirect('Index')

    return redirect("../")

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Cerro Sesiòn Con Exito")

    return redirect('Index')



