from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

class Estudiantes (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()
    email = models.CharField(max_length=30)
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()




