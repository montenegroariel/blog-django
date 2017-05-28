# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='nombre',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='detalle',
            field=models.CharField(max_length=1000),
        ),
    ]
