# Generated by Django 4.1 on 2022-10-11 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_carro_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
