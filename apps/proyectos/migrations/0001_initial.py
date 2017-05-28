# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0005_auto_20170528_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('detalle', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('detalle', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=500)),
                ('area', models.CharField(max_length=500)),
                ('responsables', models.CharField(max_length=500)),
                ('entidades_asociadas', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('anio', models.ForeignKey(to='complementos.Periodo')),
                ('clasificacion', models.ForeignKey(to='proyectos.Clasificacion')),
                ('estado', models.ForeignKey(to='proyectos.Estado')),
                ('mes', models.ForeignKey(to='complementos.Mes')),
                ('pais', models.ForeignKey(to='complementos.Pais')),
                ('provincia', models.ForeignKey(to='complementos.Provincia')),
            ],
        ),
    ]
