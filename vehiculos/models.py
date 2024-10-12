from django.db import models
from usuarios.models import Usuario

class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    placa = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    año = models.IntegerField()
