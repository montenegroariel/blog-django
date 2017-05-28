from django.db import models
#from tinymce import models as tinymce_models
from apps.categorias.models import Categoria
#from filebrowser.fields import FileBrowseField


class Publicacion(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    encabezado = models.TextField()
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    visitas = models.IntegerField(default=0)

    # class Meta:
    #     ordering = ['image', ]

    verbose_name = 'publicacion'
    verbose_name_plural = 'publicaciones'

    def __str__(self):
       return str(self.titulo)

    class Meta:
        ordering = ['-fecha']


class Documento(models.Model):
    documento = models.FileField(upload_to='images')

    def __str__(self):
       return  str(self.documento)


    class Meta:
        ordering = ['-pk']