from base.models import TimeStampedModel
from django.db import models

from workout.models import Rutina


class Ejercicio(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest = models.CharField(max_length=400)
    path_video = models.CharField(max_length=800)
    file = models.FileField(db_column='image_url', blank=False, null=True, upload_to='images/ejercicio')
    # Foranea
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name="ejercicio_rutina")
