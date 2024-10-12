from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estacionamientos, name='lista_estacionamientos'),
    path('estacionamientos/nuevo/', views.crear_estacionamiento, name='crear_estacionamiento'),
    path('estacionamientos/detalle/<int:id_estacionamiento>/', views.detalle_estacionamiento, name='detalle_estacionamiento'),
    path('estacionamientos/editar/<int:id_estacionamiento>/', views.editar_estacionamiento, name='editar_estacionamiento'),
    path('estacionamientos/borrar/<int:id_estacionamiento>/', views.borrar_estacionamiento, name='borrar_estacionamiento'),
]
