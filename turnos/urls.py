from django.urls import path
from .views import AgendaListView, AgendaDetailView

app_name = 'turnos'

urlpatterns = [
    path('agenda/',AgendaListView.as_view(),name='Agenda'),

]