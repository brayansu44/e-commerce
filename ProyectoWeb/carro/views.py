from django.shortcuts import render, redirect
from tienda.models import Carro

# Create your views here.
def carro(request):
    if request.user.is_authenticated:
        productos=Carro.objects.filter(user_id=request.user.id)
        return render(request, "carro/carro.html", {"productos":productos})
    else:
        return redirect("Index")       