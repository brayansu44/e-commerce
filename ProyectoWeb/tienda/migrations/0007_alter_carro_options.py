# Generated by Django 4.1 on 2022-10-11 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_carro_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carro',
            options={'verbose_name': 'carro', 'verbose_name_plural': 'carritos'},
        ),
    ]
