from django.db import models


class Producto(models.Model):
    RECETA = 0
    TRUCO = 1
    TIPOS_PRODUCTOS = (
        (RECETA, 'Receta'),
        (TRUCO, 'Truco'),
    )

    nombre = models.CharField(max_length=500)
    description = models.TextField()
    tipo_producto = models.PositiveSmallIntegerField(choices=TIPOS_PRODUCTOS)
    path_video = models.CharField(max_length=800,)
    precio_pts = models.IntegerField()