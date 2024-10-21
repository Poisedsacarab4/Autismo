# aplicacion/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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


<<<<<<< HEAD
=======
# Create your views here.
def hola(request):
    return HttpResponse("<h1>hola chavales del youtube :v</h1><h2>VOCES AUTISTAS 🗣🗣🗣🗣🗣 </h2><h3>xd</h3>")

>>>>>>> c04e14b1d91878988385dde52c3ff7e6473ca082
