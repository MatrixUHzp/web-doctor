from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class EdicionDatosUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', max_length=20)
    last_name = forms.CharField(label='Apellido', max_length=20)
    avatar = forms.ImageField(required=False)
    link = forms.URLField(label='Enlace', required=False)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}) ,required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'link', 'descripcion']

class LoginUsuario(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)