from django.contrib import admin
from .models import Pais, Provincia, TipoEmpresa, CondicionEmpresa, \
    Mes, Periodo, FormaPago


class PaisAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]


class TipoEmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]


class CondicionEmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]

class MesAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]

class PeriodoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]

# class FormaPagoAdmin(admin.ModelAdmin):
#     list_display = [
#         'nombre',
#     ]

admin.site.register(Mes, MesAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Periodo, PeriodoAdmin)
# admin.site.register(FormaPago, FormaPagoAdmin)
admin.site.register(TipoEmpresa, TipoEmpresaAdmin)
admin.site.register(CondicionEmpresa, CondicionEmpresaAdmin)