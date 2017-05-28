from django.contrib import admin
from .models import Menu, Submenu


class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'detalle',
    ]


class SubmenuAdmin(admin.ModelAdmin):
    list_display = [
        'detalle',
    ]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Submenu, SubmenuAdmin)
