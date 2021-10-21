from activities.models import Leccion
from base.models import TimeStampedModel
from django.db import models


class Actividad(TimeStampedModel):
    ACTIVIDAD_TRIVIA = 0
    ACTIVIDAD_COMPLETADO_COLUMNAS = 1
    ACTIVIDAD_RELACION_IAMGEN = 2

    TIPOS_ACTIVIDAD = (
        (ACTIVIDAD_TRIVIA, 'Trivia'),
        (ACTIVIDAD_COMPLETADO_COLUMNAS, 'Completado de columnas'),
        (ACTIVIDAD_RELACION_IAMGEN, 'Relacionamiento de imagenes'),
    )

    pregunta = models.CharField(max_length=500, null=True)
    tipo_actividad = models.PositiveSmallIntegerField(choices=TIPOS_ACTIVIDAD, default=1)
    # Foranea
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name="actividad_leccion")
