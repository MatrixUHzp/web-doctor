from django.urls import path
from inicio import views

# app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-medico/', views.crear_medico, name='doctor'),
    path('crear-paciente/', views.crear_paciente, name='paciente'),
    path('mostrar-pacientes/', views.lista_pacientes, name='mostrar_pacientes')

]
