from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from tienda.models import Producto, Carro
from django.contrib import messages

# Create your views here.
def allProductos(request):
    productos=Producto.objects.all()
    long_productos=Carro.objects.filter(user_id=request.user.id)
    return render(request, "tienda/allProductos.html", {"productos":productos, "long_productos":len(long_productos)})

def listaProductosAjax(request):
    productos = Producto.objects.filter(disponibilidad=True).values_list('nombre', flat=True)
    listProductos = list(productos)

    return JsonResponse(listProductos, safe=False)

def searchProducto(request):
    if request.method == "POST":
        productoBuscado =  request.POST.get('search_producto')
        if productoBuscado == "":
            return redirect(request.META.get('HTTP_REFERRER')) 
        else:
            producto = Producto.objects.filter(nombre=productoBuscado).first()  

            if producto:
                return redirect('Index')
            else:
                messages.info(request, "Ningun producto coincide con su busqueda")
                return redirect('../productos')       

    return redirect(request.META.get('HTTP_REFERRER'))    



