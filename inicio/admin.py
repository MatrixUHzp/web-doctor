from django.contrib import admin
from inicio.models import Medico, Paciente

# Register your models here.

admin.site.register([Medico, Paciente])


