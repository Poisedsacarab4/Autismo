from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hola(request):
    return HttpResponse("<h1>hola chavales del youtube</h1>")

