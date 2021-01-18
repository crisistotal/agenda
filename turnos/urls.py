from django.urls import path
from .views import TurnoCreateView, TurnoListView , TurnoUpdateView, TurnoDeleteView

app_name = 'turnos'

urlpatterns = [
    path('turno/',TurnoListView.as_view(),name='turno'),
    path('create_turno/',TurnoCreateView.as_view(),name='create_turno'),
    path('<int:pk>/update_turno',TurnoUpdateView.as_view(),name='update_turno'),
    path('<int:pk>/delete_turno',TurnoDeleteView.as_view(),name='delete_turno'),
]