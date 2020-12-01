# Generated by Django 3.1.3 on 2020-11-30 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='tamaño',
            field=models.CharField(choices=[('g', 'Grande'), ('m', 'Mediano'), ('c', 'chico')], default='Solo Piercing', max_length=1, verbose_name='Tamaño'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='celular',
            field=models.IntegerField(verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre Y Apellido'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='tipo',
            field=models.CharField(choices=[('tat', 'Tatuaje'), ('pir', 'Piercing')], max_length=3, verbose_name='Tipo de Turno'),
        ),
    ]
