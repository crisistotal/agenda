from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

tipos_turno = (
    ('tat', 'Tatuaje'),
    ('pir', 'Piercing'),
)
tamaños = (
    ('g', 'Grande'),
    ('m', 'Mediano'),
    ('c', 'Chico'),
)

class Turno(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre Y Apellido',
        max_length=50)
    celular = models.IntegerField(
        verbose_name='Celular')
    tipo = models.CharField(
        verbose_name='Turno para?',
        max_length=3,
        choices=tipos_turno)
    tamaño = models.CharField(
        verbose_name='Tamaño',
        max_length=1,
        choices=tamaños,
        default="c")
    fecha = models.DateTimeField(default=datetime.now)
    responsable = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Responsable",blank=True,null=True,default=None)
    
    def get_absolute_url(self):
        return reverse('turnos:turno')

    def __str__(self):
        return f' {self.get_tipo_display()} de {self.nombre} con {self.celular} a las {self.fecha}'


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