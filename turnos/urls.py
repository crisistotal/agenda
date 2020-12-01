from django.urls import path
from .views import TurnoCreateView, TurnoListView

app_name = 'turnos'

urlpatterns = [
    path('turno/',TurnoListView.as_view(),name='turno'),
    path('create_turno/',TurnoCreateView.as_view(),name='create_turno')
]