# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0008_documento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='publicacion',
            name='image',
            field=filebrowser.fields.FileBrowseField(null=True, max_length=200, verbose_name='Image', blank=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='image_extensions',
            field=filebrowser.fields.FileBrowseField(null=True, help_text='Only jpg-Images allowed.', max_length=200, verbose_name='Image (Extensions)', blank=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='image_format',
            field=filebrowser.fields.FileBrowseField(null=True, max_length=200, verbose_name='Image (Format)', blank=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='image_initialdir',
            field=filebrowser.fields.FileBrowseField(null=True, max_length=200, verbose_name='Image (Initial Directory)', blank=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='pdf',
            field=filebrowser.fields.FileBrowseField(null=True, max_length=200, verbose_name='PDF', blank=True),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='encabezado',
            field=models.TextField(),
        ),
    ]
