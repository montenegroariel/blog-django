from django.db import models
from apps.categorias.models import Categoria


class Menu(models.Model):
    detalle = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='#')


    def __str__(self):
        return str(self.detalle)


class Submenu(models.Model):
    detalle = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria)
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return str(self.detalle)