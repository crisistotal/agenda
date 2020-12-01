from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.


class Turno(models.Model):
    tipos_turno = (
        ('tat', 'Tatuaje'),
        ('pir', 'Piercing'),
    )
    tamaños = (
        ('g', 'Grande'),
        ('m', 'Mediano'),
        ('c', 'Chico'),
    )

    nombre = models.CharField(verbose_name='Nombre Y Apellido', max_length=50)
    celular = models.IntegerField(verbose_name='Celular')
    tipo = models.CharField(verbose_name='Tipo de Turno',
                            max_length=3, choices=tipos_turno)
    tamaño = models.CharField(
        verbose_name='Tamaño', max_length=1, choices=tamaños, default="Solo Piercing")
    
    fecha = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f'{self.nombre} / {self.celular} / {self.tipo} / {self.tamaño}'


    # @property
    # def disponibilidad(self):
    #     disponible = True
    #     if self.fecha == self.fecha:
    #         print("No esta disponible")
    #         disponible = False
    #     else:
    #         print("Si esta disponible")
    #         disponible = True
    #     return disponible