from base.models import TimeStampedModel
from django.db import models

from workout.models import Rutina


class Ejercicio(TimeStampedModel):
    nombre = models.CharField(max_length=200, null=True)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    rest = models.IntegerField(default=0)
    # Foranea
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name="ejercicio_rutina")
