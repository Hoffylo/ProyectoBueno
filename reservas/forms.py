from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['placa', 'rut', 'id_estacionamiento', 'espacio_reservado', 'hora_entrada', 'hora_salida', 'estado_reserva']
        widgets = {
            'hora_entrada': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input'}),
            'hora_salida': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input'}),
        }
