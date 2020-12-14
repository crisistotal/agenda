from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic import CreateView
from .models import Turno
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import TurnoForm
from django.urls import reverse_lazy

# Create your views here.

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    success_url = reverse_lazy('turnos:turno')

class TurnoListView(ListView):
    model = Turno