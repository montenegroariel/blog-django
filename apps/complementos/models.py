from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    verbose_name = 'Pais'
    verbose_name_plural = 'Paises'

    def __str__(self):
        return str(self.nombre)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)
    verbose_name = 'Ciudad'
    verbose_name_plural = 'Ciudades'

    def __str__(self):
        return str(self.nombre)


class TipoEmpresa(models.Model):
    nombre = models.CharField(max_length=200)
    verbose_name = 'Tipo de Empresa'
    verbose_name_plural = 'Tipos de Empresas'

    def __str__(self):
        return str(self.nombre)


class CondicionEmpresa(models.Model):
    nombre = models.CharField(max_length=200)
    verbose_name = 'Condición de la Empresa'
    verbose_name_plural = 'Condiciones de Empresas'

    def __str__(self):
        return str(self.nombre)


class Mes(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nombre)


class Periodo(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nombre)


class FormaPago(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nombre)