from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Turno
from .forms import TurnoForm

# Create your views here.

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm

class TurnoListView(ListView):
    model = Turno