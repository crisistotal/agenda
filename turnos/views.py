from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Turno
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import TurnoForm
from django.urls import reverse_lazy

# Create your views here.

class TurnoListView(ListView):
    model = Turno

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm

    
    def form_valid(self,form):
        '''
        Se remplaza el metodo form_valid por defecto para hacer ingresar el usuario que esta cargando el mismo
        '''
        turno = form.save(commit=False)
        turno.responsable = self.request.user
        turno.save()
        return super(TurnoCreateView, self).form_valid(form)
 

class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name_suffix = "_update_form"
    # Esto debera volver a otro lado
    def get_success_url(self):
        return reverse_lazy('turnos:update_turno', args=[self.object.id]) + '?ok'

class TurnoDeleteView(DeleteView):
    model = Turno
    success_url = reverse_lazy('turnos:turno')

    
