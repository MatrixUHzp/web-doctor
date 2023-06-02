from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    año_nacimiento = models.IntegerField()
    dni = models.IntegerField(null=True)

    def __str__(self):
        return f'Soy {self.nombre} {self.apellido} mi dni es {self.dni} y nací en {self.año_nacimiento}'
    
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='index.html', null=True, blank=True)

