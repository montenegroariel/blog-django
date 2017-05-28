from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = [
        'publicacion',
        'detalle',
        'nombre',
    ]


admin.site.register(Comentario, ComentarioAdmin)
