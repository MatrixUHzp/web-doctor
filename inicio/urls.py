from django.urls import path
from django.contrib.auth.decorators import login_required
from inicio import views


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),

    #Pacientes con CBV
    path('lista-pacientes/', login_required(views.ListaPacientes.as_view()), name='lista_pacientes'),
    path('pacientes/crear/', login_required(views.CrearPaciente.as_view()), name='crear_paciente'),
    path('pacientes/<int:pk>/modificar/', login_required(views.ModificarPaciente.as_view()), name='modificar_pacientes'),
    path('pacientes/<int:pk>/eliminar/', login_required(views.EliminarPaciente.as_view()), name='eliminar_paciente'),
]
