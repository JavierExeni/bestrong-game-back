from django.db import models


class Producto(models.Model):
    RECETA = 0
    TRUCO = 1
    TIPOS_PRODUCTOS = (
        (RECETA, 'Receta'),
        (TRUCO, 'Truco'),
    )

    nombre = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    tipo_producto = models.PositiveSmallIntegerField(choices=TIPOS_PRODUCTOS, default=1)
    path_video = models.CharField(max_length=500, null=True)
    precio_pts = models.IntegerField(default=0)