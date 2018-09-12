from django.contrib import admin
from .models import Publicacion, Documento, Imagen
from .forms import PublicacionForm, DocumentoForm, ImagenForm


class PublicacionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

    form = PublicacionForm

    fieldsets = (

        (None, {
            'classes': ('suit-tab suit-tab-media',),
            'fields': ['fecha', 'titulo', 'portada', 'slug', 'categoria', 'visitas'],
        }),

        ('CKEditor', {
            'classes': ('full-width',),
            'fields': ('encabezado','contenido')
        }),
    )

    ordering = ('-fecha',)

    list_display = ('fecha', 'titulo')
    suit_form_tabs = (('media', 'Media'),)
    search_fields = [
        'titulo'
    ]


class DocumentoAdmin(admin.ModelAdmin):
    form = DocumentoForm
    list_display = [
        'id',
        'documento',
    ]

    list_filter = [
        'documento'
    ]

    search_fields = [
        'documento'
    ]

class ImagenAdmin(admin.ModelAdmin):
    form = ImagenForm
    list_display = [
        'id',
        'imagen',
    ]

    list_filter = [
        'imagen'
    ]

    search_fields = [
        'imagen'
    ]

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Imagen, ImagenAdmin)