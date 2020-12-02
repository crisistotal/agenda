from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Turno
from .forms import TurnoForm

# Create your views here.

class TurnoCreateView(FormView):
    template_name = 'turnos/turno_form.html'
    form_class = TurnoForm
    success_url = '/turno'

class TurnoListView(ListView):
    model = Turno