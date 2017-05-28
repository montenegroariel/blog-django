# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0005_auto_20160615_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='encabezado',
            field=tinymce.models.HTMLField(),
        ),
    ]
