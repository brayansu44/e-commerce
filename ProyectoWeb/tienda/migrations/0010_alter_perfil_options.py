# Generated by Django 4.1 on 2022-10-14 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_alter_pedido_telefono_perfil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
    ]
