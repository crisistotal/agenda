from django.urls import path
from .views import TurnoCreateView, TurnoListView , TurnoUpdateView, TurnoDetailView

app_name = 'turnos'

urlpatterns = [
    path('turno/',TurnoListView.as_view(),name='turno'),
    path('create_turno/',TurnoCreateView.as_view(),name='create_turno'),
    path('<int:pk>/update_turno',TurnoUpdateView.as_view(),name='update_turno'),
    path('<int:pk>/<slug:slug>', TurnoDetailView.as_view(), name='detail_turno')
]