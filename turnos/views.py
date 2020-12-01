from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Agenda

# Create your views here.
class AgendaListView(ListView):
    model = Agenda      

class AgendaDetailView(DetailView):
    model = Agenda