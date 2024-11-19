from django.db import models
from django.contrib.auth.models import User

class Carta(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    ## Nuevo por dieguito :3
    Order = models.IntegerField()
    Type = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    carta = models.ForeignKey(Carta, related_name='respuestas', on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Respuesta a: {self.carta.titulo}'
