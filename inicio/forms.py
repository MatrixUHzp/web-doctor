from django import forms

class CreacionPacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    año_nacimiento = forms.IntegerField()

class BuscarPaciente(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)