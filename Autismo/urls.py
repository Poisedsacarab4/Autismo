"""
URL configuration for Autismo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cartas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página principal
    path('login/', views.user_login, name='login'),  # Vista de login
    path('logout/', views.user_logout, name='logout'),  # Vista de logout
    path('escribir/',views.escribir_carta, name='escribir'),
    path('buzon/', views.buzon , name='buzon'),
    path('buzon/responder/<int:carta_id>/', views.responder_carta, name='responder_carta'),
    path('buzon/ver/<int:carta_id>/',views. ver_carta, name='ver_carta'),
    path('mis_cartas/',views. mis_cartas, name='mis_cartas'), 
]
