# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0009_auto_20161007_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='image',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='image_extensions',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='image_format',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='image_initialdir',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='pdf',
        ),
    ]
