from base.models import TimeStampedModel
from django.db import models


class BodyInfo(TimeStampedModel):
    ECTOMORFO = 0
    ENDOMORFO = 1
    MESOMORFO = 2
    TIPOS_CUERPOS = (
        (ECTOMORFO, 'Ectomorfo'),
        (ENDOMORFO, 'Endomorfo'),
        (MESOMORFO, 'Mesomorfo'),
    )

    HIPERTROFIA = 0
    DEFINICION = 1
    RESISTENCIA = 2
    TIPO_OBJETIVO = (
        (HIPERTROFIA, 'Hipertrofia'),
        (DEFINICION, 'Definición'),
        (RESISTENCIA, 'Resistencia'),
    )

    altura = models.IntegerField(default=0)
    peso = models.IntegerField(default=0)
    calorias = models.IntegerField(default=0)
    body_type = models.PositiveSmallIntegerField(choices=TIPOS_CUERPOS, default=0)
    objetivo = models.PositiveSmallIntegerField(choices=TIPO_OBJETIVO, default=0)
