from django.db import models
from django.db import models
from django.contrib.auth.models import Group,User
Group.objects.get_or_create(name='Usuario')
Group.objects.get_or_create(name='Administrador')

# Create your models here.
# Equipos, Noticias
class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=80)
    pais =models.CharField(max_length=70)
    titulos = models.PositiveIntegerField()
    fundado = models.DateTimeField()
    def __str__(self):
        return self.nombre

class Jugadores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    pertenece_id = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    resultado = models.CharField(max_length=50)
    encuentros = models.CharField(max_length=100)
    analisis = models.CharField(max_length=100)

    def __str__(self):
        return self.resultado