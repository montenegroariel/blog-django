# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0012_auto_20170528_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portada'),
        ),
    ]
