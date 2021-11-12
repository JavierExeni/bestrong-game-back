from activities.models import Actividad
from base.models import TimeStampedModel
from django.db import models


class Opcion(TimeStampedModel):
    opcion = models.CharField(max_length=800)
    op_correcta = models.BooleanField()
    # Foraneas
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="opcion_actividad")