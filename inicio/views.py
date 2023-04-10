from django.shortcuts import render
from inicio.models import Medico
from inicio.models import Paciente

def mi_vista(request):
    return render(request, r'inicio/index.html')

def crear_medico(request):
    medico1 = Medico(nombre='Marisel', edad=32)
    # medico1.save()
    datos = {'medico': medico1}
    return render(request, r'inicio/crear_medico.html', datos)

def crear_paciente(request):
    paciente1 = Paciente(nombre='Matias', apellido='Rasmussen', fecha_nacimiento = 1707)
    # paciente1.save()
    datos = {'paciente': paciente1}
    return render(request, r'inicio/crear_paciente.html', datos)

