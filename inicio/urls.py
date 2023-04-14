from django.urls import path
from inicio import views

# app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-medico/', views.crear_medico, name='doctor'),

    #Pacientes Con vistas
    # path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    # path('pacientes/crear/', views.crear_paciente, name='paciente'),
    # path('pacientes/<int:id_paciente>/eliminar/', views.eliminar_paciente, name='eliminar_pacientes'),
    # path('pacientes/<int:id_paciente>/modificar/', views.modificar_paciente, name='modificar_pacientes'),

    #Pacientes con CBV
    path('lista-pacientes/', views.ListaPacientes.as_view(), name='lista_pacientes'),
    path('pacientes/crear/', views.CrearPaciente.as_view(), name='crear_paciente'),
    path('pacientes/<int:pk>/modificar/', views.ModificarPaciente.as_view(), name='modificar_pacientes'),
    path('pacientes/<int:pk>/eliminar/', views.EliminarPaciente.as_view(), name='eliminar_paciente'),

]
