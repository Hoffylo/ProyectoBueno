from django.db import models

class Estacionamiento(models.Model):
    id_estacionamiento = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)
    capacidad_total = models.IntegerField()
    espacios_disponibles = models.IntegerField()
    tarifa_hora = models.IntegerField()
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()

class Espacio(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    numero_espacio = models.CharField(max_length=10)
    piso = models.IntegerField()
    tipo_espacio = models.CharField(max_length=100)
    ocupado = models.BooleanField(default=False)
    sensor_id = models.IntegerField()
