from django.shortcuts import render, redirect
from inicio.models import Medico
from inicio.models import Paciente
from inicio.forms import CreacionPacienteFormulario, BuscarPaciente

def mi_vista(request):
    return render(request, r'inicio/index.html')

def crear_medico(request):
    medico1 = Medico(nombre='Marisel', edad=32)
    # medico1.save()
    datos = {'medico': medico1}
    return render(request, r'inicio/crear_medico.html', datos)

def crear_paciente(request):

    if request.method == "POST":
        formulario = CreacionPacienteFormulario(request.POST)

        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data

            paciente = Paciente(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'], dni=datos_correctos['dni'], año_nacimiento=datos_correctos['año_nacimiento'])
            paciente.save()

            return redirect('mostrar_pacientes')

    formulario = CreacionPacienteFormulario()
    return render(request, r'inicio/crear_paciente.html', {'formulario': formulario})

def lista_pacientes(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        pacientes = Paciente.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        pacientes = Paciente.objects.all()
    formulario_busqueda = BuscarPaciente()
    return render(request, r'inicio/mostrar_pacientes.html', {'pacientes': pacientes, 'formulario_busqueda': formulario_busqueda})

