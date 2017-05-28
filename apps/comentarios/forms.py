from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    detalle = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comentario'}))

    class Meta:
        model = Comentario
        fields = '__all__'
        # exclude = ['publicacion']