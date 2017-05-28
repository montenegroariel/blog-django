from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]

admin.site.register(Categoria, CategoriaAdmin)