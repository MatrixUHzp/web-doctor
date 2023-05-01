from django import forms

class BuscarPaciente(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)