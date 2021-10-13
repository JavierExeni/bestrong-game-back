from base.models import TimeStampedModel
from django.db import models

from workout.models import Rutina


class Nivel(TimeStampedModel):
    nombre = models.CharField(max_length=200, null=True)
    # Foraneas
    rutina = models.OneToOneField(Rutina, on_delete=models.CASCADE, related_name="nivel_rutina")
