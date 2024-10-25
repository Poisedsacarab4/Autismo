from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario predeterminado

class Carta(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    titulo = models.CharField(max_length=255)  # Título de la carta
    contenido = models.TextField()  # Contenido de la carta
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    creada_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def _str_(self):
        return f'{self.titulo} - {self.autor.username}'