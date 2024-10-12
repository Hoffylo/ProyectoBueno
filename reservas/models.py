from django.db import models
from vehiculos.models import Vehiculo
from estacionamientos.models import Estacionamiento, Espacio

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    espacio_reservado = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField()
    hora_salida = models.DateTimeField()
    estado_reserva = models.CharField(max_length=100)
