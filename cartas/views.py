# aplicacion/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carta, Respuesta
from .forms import RespuestaForm
import random

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


def buzon(request):
    usuario_actual = request.user
    cartas_disponibles = Carta.objects.exclude(autor=usuario_actual)

    carta_aleatoria = None
    if cartas_disponibles.exists():
        carta_aleatoria = random.choice(cartas_disponibles)

    return render(request, 'buzon.html', {'carta': carta_aleatoria})

def responder_carta(request, carta_id):
    carta = get_object_or_404(Carta, id=carta_id)

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.carta = carta
            respuesta.autor = request.user
            respuesta.save()
            return redirect('ver_carta', carta_id=carta.id)  # Redirigir a la vista de la carta

    else:
        form = RespuestaForm()

    return render(request, 'responder_carta.html', {'carta': carta, 'form': form})

def ver_carta(request, carta_id):
    carta = get_object_or_404(Carta, id=carta_id)
    respuestas = carta.respuestas.all()  # Obtener respuestas relacionadas

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.carta = carta
            respuesta.autor = request.user
            respuesta.save()
            return redirect('ver_carta', carta_id=carta.id)  # Redirigir a la misma vista

    else:
        form = RespuestaForm()

    return render(request, 'ver_carta.html', {'carta': carta, 'respuestas': respuestas, 'form': form})

def mis_cartas(request):
    usuario_actual = request.user
    cartas = Carta.objects.filter(autor=usuario_actual).prefetch_related('respuestas')  # Cargar respuestas relacionadas

    if request.method == 'POST':
        respuesta_id = request.POST.get('respuesta_id')
        respuesta = get_object_or_404(Respuesta, id=respuesta_id)
        form = RespuestaForm(request.POST)

        if form.is_valid():
            nueva_respuesta = form.save(commit=False)
            nueva_respuesta.carta = respuesta.carta  # Asociar a la carta original
            nueva_respuesta.autor = request.user  # Establecer el autor como el usuario actual
            nueva_respuesta.save()
            return redirect('mis_cartas')  # Redirigir a la misma vista

    else:
        form = RespuestaForm()

    return render(request, 'mis_cartas.html', {'cartas': cartas, 'form': form})