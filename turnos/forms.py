from django import forms
from django.forms import DateTimeField
from datetimepicker.widgets import DateTimePicker

from .models import Turno
from turnos.models import tipos_turno, tamaños


class TurnoForm(forms.ModelForm):
    fecha = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model = Turno
        fields = ['fecha', 'nombre', 'celular', 'tipo', 'tamaño']