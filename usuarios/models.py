from django.db import models

class Usuario(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=100)
    tipo_user = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)


