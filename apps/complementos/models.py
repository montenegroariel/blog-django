from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return str(self.nombre)


class Provincia(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return str(self.nombre)


class TipoEmpresa(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Tipo de Empresa'
        verbose_name_plural = 'Tipos de Empresas'

    def __str__(self):
        return str(self.nombre)


class CondicionEmpresa(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Condición de Empresa'
        verbose_name_plural = 'Condiciones de Empresas'

    def __str__(self):
        return str(self.nombre)


class Mes(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Mes'
        verbose_name_plural = 'Meses'

    def __str__(self):
        return str(self.nombre)


class Periodo(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return str(self.nombre)


class FormaPago(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'

    def __str__(self):
        return str(self.nombre)