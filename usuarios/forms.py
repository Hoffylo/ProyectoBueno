from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'tipo_user']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        usuario_id = self.instance.rut

        if Usuario.objects.filter(rut=rut).exclude(rut=usuario_id).exists():
            raise forms.ValidationError("El RUT ya está en uso por otro usuario.")
        
        return rut
