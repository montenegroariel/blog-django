from django.db import models

from apps.complementos.models import Mes, Pais, Periodo, Provincia


class Clasificacion(models.Model):
    detalle = models.CharField(max_length=300)
    color = models.CharField(max_length=20)


class Estado(models.Model):
    detalle = models.CharField(max_length=300)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    clasificacion = models.ForeignKey(Clasificacion)
    mes = models.ForeignKey(Mes)
    anio = models.ForeignKey(Periodo)
    pais = models.ForeignKey(Pais)
    provincia = models.ForeignKey(Provincia)
    responsables = models.CharField(max_length=500)
    entidades_asociadas = models.CharField(max_length=500)
    estado = models.ForeignKey(Estado)
    link = models.CharField(max_length=500)