from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

# app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('cambio-contraseña/', views.CambioContraseña.as_view(), name='cambio_contraseña'),

]
