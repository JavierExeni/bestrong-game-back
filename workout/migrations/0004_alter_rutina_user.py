# Generated by Django 3.2.8 on 2021-11-14 20:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout', '0003_alter_rutina_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutina',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]