# Generated by Django 4.1 on 2022-10-22 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_alter_pedido_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='estado',
            new_name='estado_pedido',
        ),
    ]