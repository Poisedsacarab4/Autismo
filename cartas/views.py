from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hola(request):
    return HttpResponse("<h1>hola chavales del youtube :v</h1><h2>que gei</h2><h3>hola</h3>")

