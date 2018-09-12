# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0013_publicacion_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('imagen', models.FileField(upload_to='uploads')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name_plural': 'Imagen',
                'verbose_name': 'Imagen',
            },
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.FileField(upload_to='documentos'),
        ),
    ]
