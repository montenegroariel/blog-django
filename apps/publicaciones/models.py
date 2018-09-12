from django.db import models
from apps.categorias.models import Categoria


class Publicacion(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField(max_length=200)
    portada = models.ImageField(upload_to='portada', null=True, blank=True) 
    slug = models.SlugField(unique=False)
    encabezado = models.TextField()
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    visitas = models.IntegerField(default=0)

    def __str__(self):
       return str(self.titulo)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'


class Documento(models.Model):
    documento = models.FileField(upload_to='documentos')

    def __str__(self):
       return  str(self.documento)


    class Meta:
        ordering = ['-pk']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class Imagen(models.Model):
    imagen = models.FileField(upload_to='uploads')

    def __str__(self):
       return  str(self.imagen)


    class Meta:
        ordering = ['-pk']
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagen'