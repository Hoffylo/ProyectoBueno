from django import forms
from .models import Estacionamiento

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = [
            'ubicacion', 'capacidad_total', 'espacios_disponibles', 'tarifa_hora', 'horario_apertura', 'horario_cierre'
        ]
