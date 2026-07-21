from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def criar_usuario(request):
    
    if request.method == "POST":
        
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    else:
        
        form = UsuarioForm()
    
    return render(request, 'usuarios/criar_usuario.html', {"form": form})       

def listar_usuarios(request):

    usuarios = Usuario.objects.all()
    
    return render(request, 'usuarios/listar_usuarios.html', {"usuarios": usuarios})

