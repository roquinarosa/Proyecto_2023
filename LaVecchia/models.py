from django.db import models

# Create your models here.
class Menu(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

