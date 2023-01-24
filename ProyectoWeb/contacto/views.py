from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def contacto(request):

    subject="Atencion Al Cliente"

    mensaje=render_to_string("emails/contacto.html",{
        "nombre": request.POST["nombre"],
        "mensaje": request.POST["mensaje"],
        "telefono": request.POST["telefono"],
        "email": request.POST["email"]
    })

    email_from=settings.EMAIL_HOST_USER
    recipient_list=["brayansayrez400@gmail.com"]

    #to=request.POST["email"]

    send_mail(subject, mensaje, email_from, recipient_list, html_message=mensaje)

    messages.success(request, "Correo Enviado Correctamente")
        
    return redirect("../")