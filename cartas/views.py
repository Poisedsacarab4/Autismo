# aplicacion/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cartas.models import Carta  # Asegúrate de que el modelo esté importado


def index(request):
    return render(request, "index.html")  # Renderiza la página principal

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página principal después de iniciar sesión
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')  # Redirige a la página principal después de cerrar sesión



@login_required  # Asegúrate de que solo los usuarios autenticados puedan enviar cartas
def escribir_carta(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        
        # Crea y guarda una nueva carta en la base de datos
        nueva_carta = Carta(titulo=titulo, contenido=contenido, autor=request.user)
        nueva_carta.save()
        
        return redirect('index')  # Redirige a la página principal (ajusta el nombre según tu URL)
    
    return render(request, 'escrbir.html')  # Cambia el nombre del template al correcto