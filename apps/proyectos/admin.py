from django.contrib import admin
from .models import Clasificacion, Estado, Proyecto


class ClasificacionAdmin(admin.ModelAdmin):
    list_display = [
        'detalle',
        'color',
    ]


class EstadoAdmin(admin.ModelAdmin):
    list_display = [
        'detalle',
    ]


class ProyectoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'area',
        'clasificacion',
        'mes',
        'anio',
        'pais',
        'provincia',
        'responsables',
        'entidades_asociadas',
        'estado',
        'link',
    ]

admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Proyecto, ProyectoAdmin)

"""
from django.forms import ModelForm
from suit.widgets import HTML5Input

class ProductForm(ModelForm):
    class Meta:
        widgets = {
            'color': HTML5Input(input_type='color'),
        }
"""