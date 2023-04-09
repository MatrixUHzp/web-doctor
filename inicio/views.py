from django.shortcuts import render
from inicio.models import Medico

def mi_vista(request):
    return render(request, r'inicio/index.html')

def crear_medico(request):
    medico1 = Medico(nombre='Marisel', edad=32)
    medico1.save()
    datos = {'medico': medico1}
    return render(request, r'inicio/crear_medico.html', datos)
