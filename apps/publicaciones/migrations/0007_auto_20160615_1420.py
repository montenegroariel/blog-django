# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0006_auto_20160615_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(),
        ),
    ]
