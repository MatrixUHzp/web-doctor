from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista),
    path('crear-medico/', views.crear_medico),
]
