# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0010_auto_20161007_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='favorito',
            new_name='visitas',
        ),
    ]
