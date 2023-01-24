from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=500)
    cantidad=models.IntegerField()
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    precio_original=models.IntegerField()
    precio_descuento=models.IntegerField()
    disponibilidad=models.BooleanField(default=True)
    tendencia=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre

class Carro(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    producto_qty=models.IntegerField(null=False, blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='carro'
        verbose_name_plural='carritos'
    
    def __str__(self):
        return self.producto.nombre

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150, null=False)
    apellido=models.CharField(max_length=150, null=False)
    email=models.CharField(max_length=150, null=False)
    telefono=models.CharField(max_length=50, null=False)
    direccion=models.TextField(null=False)
    ciudad=models.CharField(max_length=150, null=False)
    estado=models.CharField(max_length=150, null=False)
    pais=models.CharField(max_length=150, null=False)
    codigo_pin=models.CharField(max_length=150, null=False)
    precio_total=models.IntegerField(null=False)
    modo_pago=models.CharField(max_length=150, null=False)
    id_pago=models.CharField(max_length=250, null=True)
    estados_pedido=(
        ('Pendiente','Pendiente'),
        ('Completado','Completado'),
        ('Cancelado','Cancelado'),
    )
    estado_pedido=models.CharField(max_length=150, choices=estados_pedido, default='Pendiente')
    mensaje=models.TextField(null=True)
    numero_seguimiento=models.CharField(max_length=150, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.numero_seguimiento)

class ArticuloPedido(models.Model):
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio=models.IntegerField(null=False)
    cantidad=models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.pedido.id, self.pedido.numero_seguimiento)

class Perfil(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    telefono=models.CharField(max_length=50, null=False)
    direccion=models.TextField(null=False)
    ciudad=models.CharField(max_length=150, null=False)
    estado=models.CharField(max_length=150, null=False)
    pais=models.CharField(max_length=150, null=False)
    codigo_pin=models.CharField(max_length=150, null=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'

    def __str__(self):
        return self.user.username
