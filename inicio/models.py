from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
