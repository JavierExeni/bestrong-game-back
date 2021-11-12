# Generated by Django 3.2.8 on 2021-11-04 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
        ('authentication', '0002_auto_20211103_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nivel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_nivel', to='levels.nivel'),
            preserve_default=False,
        ),
    ]