from activities.models import Actividad
from base.models import TimeStampedModel
from django.db import models


class Opcion(TimeStampedModel):
    opcion = models.CharField(max_length=500, null=True)
    op_correcta = models.CharField(max_length=500, null=True)
    # Foraneas
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="opcion_actividad")