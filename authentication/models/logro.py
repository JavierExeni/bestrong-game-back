from django.db import models

from base.models import TimeStampedModel


class Logro(TimeStampedModel):
    nombre = models.CharField(max_length=500)
    file = models.FileField(db_column='image_url', blank=False, null=True, upload_to='images/logro')
