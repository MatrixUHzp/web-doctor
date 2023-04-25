from django.shortcuts import render, redirect
from inicio.models import Paciente
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from inicio.forms import CreacionPacienteFormulario, BuscarPaciente, ModificarPacienteFormulario

def mi_vista(request):
    return render(request, r'inicio/index.html')

def crear_paciente(request):

    if request.method == "POST":
        formulario = CreacionPacienteFormulario(request.POST)

        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data

            paciente = Paciente(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'], dni=datos_correctos['dni'], año_nacimiento=datos_correctos['año_nacimiento'])
            paciente.save()

            return redirect('lista_pacientes')

    formulario = CreacionPacienteFormulario()
    return render(request, r'inicio/crear_paciente.html', {'formulario': formulario})

def eliminar_paciente(request, id_paciente):
    paciente_a_eliminar = Paciente.objects.get(id=id_paciente)
    paciente_a_eliminar.delete()
    return redirect('lista_pacientes')

def modificar_paciente(request, id_paciente):
    paciente_a_modificar = Paciente.objects.get(id=id_paciente)

    if request.method == "POST":
        formulario = ModificarPacienteFormulario(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            paciente_a_modificar.nombre = data_limpia['nombre']            
            paciente_a_modificar.apellido = data_limpia['apellido']            
            paciente_a_modificar.dni = data_limpia['dni']     
            paciente_a_modificar.año_nacimiento = data_limpia['año_nacimiento']
            paciente_a_modificar.save()            
            return redirect('lista_pacientes')
        else:
            return render(request, r'inicio/modificar_pacientes.html', {'formulario': formulario, 'id_paciente': id_paciente})
    
    formulario = ModificarPacienteFormulario(initial={'nombre': paciente_a_modificar.nombre,'apellido': paciente_a_modificar.apellido, 'dni': paciente_a_modificar.dni, 'año_nacimiento': paciente_a_modificar.año_nacimiento,})
    return render(request, 'inicio/modificar_pacientes.html', {'formulario': formulario, 'id_paciente': id_paciente})

def lista_pacientes(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        pacientes = Paciente.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        pacientes = Paciente.objects.all()
    formulario_busqueda = BuscarPaciente()
    return render(request, r'inicio/mostrar_pacientes.html', {'pacientes': pacientes, 'formulario_busqueda': formulario_busqueda})

def acerca(request):
    return render(request, 'inicio/acerca.html')

class ListaPacientes(ListView):
    model = Paciente
    template_name = 'inicio/CBV/lista_pacientes.html'

class CrearPaciente(CreateView):
    model = Paciente
    template_name = 'inicio/CBV/crear_paciente.html'
    success_url = '/lista-pacientes/'
    fields = ['nombre', 'apellido', 'dni', 'año_nacimiento']

class ModificarPaciente(LoginRequiredMixin, UpdateView):
    model = Paciente
    template_name = 'inicio/CBV/modificar_pacientes.html'
    success_url = '/lista-pacientes/'
    fields = ['nombre', 'apellido', 'dni', 'año_nacimiento']

class EliminarPaciente(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'inicio/CBV/eliminar_paciente.html'
    success_url = '/lista-pacientes/'