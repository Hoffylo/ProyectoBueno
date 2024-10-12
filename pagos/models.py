from django.db import models
from reservas.models import Reserva

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto_reserva = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)
    tipo_comprobante = models.CharField(max_length=50)
    comprobante_pago = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=50)
