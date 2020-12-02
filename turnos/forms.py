from django import forms
from .models import Turno
from django.forms import DateTimeField
from datetimepicker.widgets import DateTimePicker




class TurnoForm(forms.ModelForm):

    class Meta:
        model = Turno
        fields = ['nombre', 'celular', 'tipo', 'tamaño', 'fecha']
        widgets = {'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date','id':'datetimepicker'})
        }
