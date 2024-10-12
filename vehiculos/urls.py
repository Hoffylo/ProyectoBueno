from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vehiculos, name='lista_vehiculos'),
    path('nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('<int:id_vehiculo>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('<int:id_vehiculo>/editar/', views.editar_vehiculo, name='editar_vehiculo'),
    path('<int:id_vehiculo>/borrar/', views.borrar_vehiculo, name='borrar_vehiculo'),
]
