from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('<int:id_reserva>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:id_reserva>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:id_reserva>/', views.eliminar_reserva, name='eliminar_reserva'),
]
