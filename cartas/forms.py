from django import forms
from .models import Respuesta

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu respuesta aquí...'}),
        }

        
class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu respuesta aquí...'}),
        }