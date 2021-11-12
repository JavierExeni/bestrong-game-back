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

    altura = models.IntegerField()
    peso = models.IntegerField()
    calorias = models.FloatField()
    body_type = models.PositiveSmallIntegerField(choices=TIPOS_CUERPOS)
    objetivo = models.PositiveSmallIntegerField(choices=TIPO_OBJETIVO)
