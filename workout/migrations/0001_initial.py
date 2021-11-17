# Generated by Django 3.2.8 on 2021-11-13 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('rest', models.CharField(max_length=400)),
                ('path_video', models.CharField(max_length=800)),
                ('file', models.FileField(db_column='image_url', null=True, upload_to='images/ejercicio')),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicio_rutina', to='workout.rutina')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
