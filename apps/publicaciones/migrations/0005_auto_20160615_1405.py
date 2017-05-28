# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_auto_20160615_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
