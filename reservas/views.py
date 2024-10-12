from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Reserva
from .forms import ReservaForm

# Vista para listar las reservas
def lista_reservas(request):
    reservas = Reserva.objects.all()  # Ordena las reservas por la fecha de inicio
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

# Vista para crear una nueva reserva
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva reserva
            return redirect('lista_reservas')  # Redirige a la lista de reservas
    else:
        form = ReservaForm()  # Si no es POST, muestra el formulario vacío

    return render(request, 'reservas/crear_reserva.html', {'form': form})

# Vista para editar una reserva existente
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('lista_reservas')  # Redirige a la lista de reservas
    else:
        form = ReservaForm(instance=reserva)  # Si no es POST, muestra el formulario con los datos existentes
    
    return render(request, 'reservas/editar_reserva.html', {'form': form})

# Vista para eliminar una reserva
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    
    if request.method == 'POST':
        reserva.delete()  # Elimina la reserva
        return redirect('lista_reservas')  # Redirige a la lista de reservas
    
    return render(request, 'reservas/eliminar_reserva.html', {'reserva': reserva})


def detalle_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, id_reserva=id_reserva)
    return render(request, 'usuarios/detalle_reserva.html', {'reserva': reserva})