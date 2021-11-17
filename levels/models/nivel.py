from base.models import TimeStampedModel
from django.db import models


class Nivel(TimeStampedModel):
    nombre = models.CharField(max_length=200)
