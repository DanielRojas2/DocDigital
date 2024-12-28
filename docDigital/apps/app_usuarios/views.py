from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EditarPerfilUsuarioForm, EditarUsuarioForm
from .models.ModeloPerfil import PerfilUsuario

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario_usuario = EditarUsuarioForm(
            instance=request.user, data=request.POST
        )
        formulario_perfil = EditarPerfilUsuarioForm(
            instance=request.user.perfilusuario, data=request.POST
        )

        if formulario_usuario.is_valid() and formulario_perfil.is_valid():
            formulario_usuario.save()
            formulario_perfil.save()
            messages.success(
                request, 'Perfil actualizado correctamente.'
            )
        else:
            messages.error(
                request, 'Error al actualizar perfil.'
            )
    else:
        formulario_usuario = EditarUsuarioForm(instance=request.user)
        formulario_perfil = EditarPerfilUsuarioForm(
            instance=request.user.perfilusuario
        )
    
    return render(
        request, 'usuario/editar_perfil.html',
        {
            'formulario_usuario': formulario_usuario,
            'formulario_perfil': formulario_perfil
        }
    )
