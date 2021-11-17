from base.models import TimeStampedModel
from django.db import models
from authentication.models import User
from levels.models import Nivel


class Rutina(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    finalizado = models.BooleanField(default=False)

    # Foregin
    nivel = models.OneToOneField(Nivel, on_delete=models.CASCADE, related_name="rutina_nivel")
    user = models.ManyToManyField(User, blank=True)
