from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo
from .forms import VehiculoForm

# Vista para listar los vehículos
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/lista_vehiculos.html', {'vehiculos': vehiculos})

# Vista para crear un nuevo vehículo
def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/crear_vehiculo.html', {'form': form})

# Vista para ver el detalle de un vehículo
def detalle_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id_vehiculo=id_vehiculo)
    return render(request, 'vehiculos/detalle_vehiculo.html', {'vehiculo': vehiculo})

# Vista para editar un vehículo existente
def editar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id_vehiculo=id_vehiculo)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

# Vista para borrar un vehículo
def borrar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id_vehiculo=id_vehiculo)
    if request.method == "POST":
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'vehiculos/borrar_vehiculo.html', {'vehiculo': vehiculo})
