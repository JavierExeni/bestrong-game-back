from base.models import TimeStampedModel
from django.db import models

from workout.models import Rutina


class Ejercicio(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest = models.CharField(max_length=400)
    # Foranea
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name="ejercicio_rutina")
