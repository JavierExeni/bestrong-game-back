# Generated by Django 3.2.8 on 2021-10-13 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('rutina', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nivel_rutina', to='workout.rutina')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]