from django.db import models

# Create your models here.
class cartas(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.TextField()
    usuario=models.ForeignKey(auth_user, on_delete=models.CASCADE)
                            
