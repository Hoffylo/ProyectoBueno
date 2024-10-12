from django.shortcuts import render, get_object_or_404, redirect
from .models import Estacionamiento
from .forms import EstacionamientoForm

# Vista para listar los estacionamientos
def lista_estacionamientos(request):
    estacionamientos = Estacionamiento.objects.all()
    return render(request, 'estacionamientos/lista_estacionamientos.html', {'estacionamientos': estacionamientos})

# Vista para crear un nuevo estacionamiento
def crear_estacionamiento(request):
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estacionamientos')
    else:
        form = EstacionamientoForm()
    return render(request, 'estacionamientos/crear_estacionamiento.html', {'form': form})

# Vista para ver el detalle de un estacionamiento
def detalle_estacionamiento(request, id_estacionamiento):
    estacionamiento = get_object_or_404(Estacionamiento, id_estacionamiento=id_estacionamiento)
    return render(request, 'estacionamientos/detalle_estacionamiento.html', {'estacionamiento': estacionamiento})

# Vista para editar un estacionamiento existente
def editar_estacionamiento(request, id_estacionamiento):
    estacionamiento = get_object_or_404(Estacionamiento, id_estacionamiento=id_estacionamiento)
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST, instance=estacionamiento)
        if form.is_valid():
            form.save()
            return redirect('lista_estacionamientos')
    else:
        form = EstacionamientoForm(instance=estacionamiento)
    return render(request, 'estacionamientos/editar_estacionamiento.html', {'form': form, 'estacionamiento': estacionamiento})

# Vista para borrar un estacionamiento
def borrar_estacionamiento(request, id_estacionamiento):
    estacionamiento = get_object_or_404(Estacionamiento, id_estacionamiento=id_estacionamiento)
    if request.method == "POST":
        estacionamiento.delete()
        return redirect('lista_estacionamientos')
    return render(request, 'estacionamientos/borrar_estacionamiento.html', {'estacionamiento': estacionamiento})
