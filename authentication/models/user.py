from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.models import BodyInfo


class User(AbstractUser):
    MASCULINO = 0
    FEMENINO = 1
    TIPOS_GENEROS = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    )

    edad = models.IntegerField(default=18)
    genero = models.PositiveSmallIntegerField(choices=TIPOS_GENEROS, default=1)
    puntos = models.IntegerField(default=0)
    # Llaves foraneas
    bodyinfo = models.OneToOneField(BodyInfo, on_delete=models.CASCADE, related_name="user_bodyInfo")
