
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', include('home.urls')),
    path('vehiculos/', include('vehiculos.urls')),
    path('estacionamientos/', include('estacionamientos.urls')),
    path('reservas/', include('reservas.urls')),
    #path('pagos/', include('pagos.urls')),
]
