from django.db import models
from apps.publicaciones.models import Publicacion


class Comentario(models.Model):
    nombre = models.CharField(max_length=50, default='Anonymous')
    detalle = models.CharField(max_length=1000)
    publicacion = models.ForeignKey(Publicacion)

    def __str__(self):
        return str(self.detalle)
