from base.models import TimeStampedModel
from django.db import models

from levels.models import Nivel


class Leccion(TimeStampedModel):
    nombre = models.CharField(max_length=500)
    descripcion = models.TextField()
    path_video = models.CharField(max_length=800)
    # Foranea
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name="leccion_nivel")