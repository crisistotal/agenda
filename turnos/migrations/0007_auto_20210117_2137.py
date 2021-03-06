# Generated by Django 3.1.3 on 2021-01-18 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnos', '0006_auto_20201201_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='responsable',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turno',
            name='tamaño',
            field=models.CharField(choices=[('g', 'Grande'), ('m', 'Mediano'), ('c', 'Chico')], default='c', max_length=1, verbose_name='Tamaño'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='tipo',
            field=models.CharField(choices=[('tat', 'Tatuaje'), ('pir', 'Piercing')], max_length=3, verbose_name='Turno para?'),
        ),
    ]
