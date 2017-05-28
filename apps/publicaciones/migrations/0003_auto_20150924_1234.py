# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_auto_20150918_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicacion',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
