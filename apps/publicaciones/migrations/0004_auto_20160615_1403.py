# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_auto_20150924_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=models.CharField(max_length=30000),
        ),
    ]
