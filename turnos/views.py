from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Turno
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import TurnoForm
from django.urls import reverse_lazy

# Create your views here.

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    success_url = reverse_lazy('turnos:turno')

class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name_suffix = "_update_form"
    # Esto debera volver a otro lado
    def get_success_url(self):
        return reverse_lazy('turnos:update_turno', args=[self.object.id]) + '?ok'


class TurnoDetailView(DetailView):
    model = Turno

class TurnoListView(ListView):
    model = Turno