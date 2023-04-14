from django import forms

class BasePacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    año_nacimiento = forms.IntegerField()


class CreacionPacienteFormulario(forms.Form):
    ...

class ModificarPacienteFormulario(forms.Form):
    ...
    
class BuscarPaciente(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)