from django import forms
from django.forms import DateTimeField
from bootstrap_datepicker_plus import DateTimePickerInput
from .models import Turno
from turnos.models import tipos_turno, tamaños


class TurnoForm(forms.ModelForm):

    class Meta:  # Configuracion personalizada para el form
        model = Turno
        fields = ['nombre', 'celular', 'tipo', 'tamaño', 'fecha']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellido'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}),
            'tipo' : forms.Select(attrs={'class': 'form-control'}),
            'tamaño': forms.Select(attrs={'class':'form-control'}),
            'fecha': DateTimePickerInput(attrs={'class':'form-control'},
                format= '%d/%m/%Y %H:%M')
        }

        labels = {
            'nombre' : '',
            'celular': '', 
        }