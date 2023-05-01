from django.shortcuts import render
from inicio.models import Paciente
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from inicio.forms import BuscarPaciente

def mi_vista(request):
    return render(request, r'inicio/index.html')


def acerca(request):
    return render(request, 'inicio/acerca.html')

class ListaPacientes(ListView):
    model = Paciente
    template_name = 'inicio/CBV/lista_pacientes.html'

class CrearPaciente(CreateView):
    model = Paciente
    template_name = 'inicio/CBV/crear_paciente.html'
    success_url = reverse_lazy('lista_pacientes')
    fields = ['nombre', 'apellido', 'dni', 'año_nacimiento']

class ModificarPaciente(LoginRequiredMixin, UpdateView):
    model = Paciente
    template_name = 'inicio/CBV/modificar_pacientes.html'
    success_url = reverse_lazy('lista_pacientes')
    fields = ['nombre', 'apellido', 'dni', 'año_nacimiento']

class EliminarPaciente(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'inicio/CBV/eliminar_paciente.html'
    success_url = reverse_lazy('lista_pacientes')