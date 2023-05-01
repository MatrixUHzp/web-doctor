from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),


    #Pacientes con CBV
    path('lista-pacientes/', views.ListaPacientes.as_view(), name='lista_pacientes'),
    path('pacientes/crear/', views.CrearPaciente.as_view(), name='crear_paciente'),
    path('pacientes/<int:pk>/modificar/', views.ModificarPaciente.as_view(), name='modificar_pacientes'),
    path('pacientes/<int:pk>/eliminar/', views.EliminarPaciente.as_view(), name='eliminar_paciente'),
]
