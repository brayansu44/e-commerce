# Generated by Django 4.1 on 2022-09-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_descuento',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_original',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
