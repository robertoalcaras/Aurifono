from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscaPaciente, name='buscaPaciente'),
    path('paciente/<int:id>', views.paciente, name='paciente'),
    path('novoPaciente/', views.novoPaciente, name='Novo Paciente'),
    path('editar/<int:id>', views.editarPaciente, name='Editar Paciente'),
    path('', views.index, name='index'),
]
