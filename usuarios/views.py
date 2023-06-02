from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from usuarios.forms import MiFormularioDeCreacion, EdicionDatosUsuario, LoginUsuario
from usuarios.models import InformacionExtra

# Create your views here.

def login(request):

    if request.method == 'POST':
        formulario = LoginUsuario(request, data=request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            django_login(request, usuario)

            InformacionExtra.objects.get_or_create(user=request.user)
            return redirect('inicio')
        else:
            return render(request, 'usuarios/login.html', {'formulario': formulario})

    formulario = LoginUsuario()
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):

    if request.method == "POST":
        formulario = MiFormularioDeCreacion(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})
    
    formulario = MiFormularioDeCreacion()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    
    if request.method == "POST":
        formulario = EdicionDatosUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                request.user.informacionextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.informacionextra.save()
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})
    
    formulario = EdicionDatosUsuario(initial={'avatar':request.user.informacionextra.avatar,
                                              'link':request.user.informacionextra.link}, instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class CambioContraseña(PasswordChangeView):
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url = reverse_lazy('editar_perfil')