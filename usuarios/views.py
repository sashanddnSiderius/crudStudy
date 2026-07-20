from django.shortcuts import render
from .models import Usuario

# Create your views here.
def criar_usuario(request):
    return render(request, 'usuarios/criar_usuario.html')

def listar_usuarios(request):

    usuarios = Usuario.objects.all()
    
    return render(request, 'usuarios/listar_usuarios.html', {"usuarios": usuarios})
