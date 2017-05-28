# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0011_auto_20170224_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ['-pk'], 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'ordering': ['-fecha'], 'verbose_name': 'Publicación', 'verbose_name_plural': 'Publicaciones'},
        ),
    ]
