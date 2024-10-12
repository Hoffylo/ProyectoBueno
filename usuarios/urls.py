from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('<int:rut>/', views.detalle_usuario, name='detalle_usuario'),
    path('nuevo/', views.crear_usuario, name='crear_usuario'),
    path('<int:rut>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<int:rut>/borrar/', views.borrar_usuario, name='borrar_usuario'),
]
