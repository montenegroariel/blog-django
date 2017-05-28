# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0004_formapago_periodo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ciudad',
            new_name='Provincia',
        ),
        migrations.AlterModelOptions(
            name='condicionempresa',
            options={'verbose_name': 'Condición de Empresa', 'verbose_name_plural': 'Condiciones de Empresas'},
        ),
        migrations.AlterModelOptions(
            name='formapago',
            options={'verbose_name': 'Forma de Pago', 'verbose_name_plural': 'Formas de Pago'},
        ),
        migrations.AlterModelOptions(
            name='mes',
            options={'verbose_name': 'Mes', 'verbose_name_plural': 'Meses'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='periodo',
            options={'verbose_name': 'Periodo', 'verbose_name_plural': 'Periodos'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'verbose_name': 'Provincia', 'verbose_name_plural': 'Provincias'},
        ),
        migrations.AlterModelOptions(
            name='tipoempresa',
            options={'verbose_name': 'Tipo de Empresa', 'verbose_name_plural': 'Tipos de Empresas'},
        ),
    ]
