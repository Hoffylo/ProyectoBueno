from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm  # Asegúrate de haber creado un formulario en forms.py

# Vista para listar usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# Vista para mostrar detalles de un usuario
def detalle_usuario(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    return render(request, 'usuarios/detalle_usuario.html', {'usuario': usuario})

# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

# Vista para editar un usuario existente
def editar_usuario(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})

def borrar_usuario(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    if request.method == "POST":
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/borrar_usuario.html', {'usuario': usuario})
