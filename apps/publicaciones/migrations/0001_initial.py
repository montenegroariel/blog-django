# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('encabezado', models.CharField(max_length=300)),
                ('contenido', tinymce.models.HTMLField()),
                ('favorito', models.IntegerField()),
                ('categoria', models.ForeignKey(to='categorias.Categoria')),
            ],
        ),
    ]
