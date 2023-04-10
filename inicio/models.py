from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    año_nacimiento = models.IntegerField()

    def __str__(self):
        return f'Soy {self.nombre} {self.apellido} y nací en {self.año_nacimiento}'

