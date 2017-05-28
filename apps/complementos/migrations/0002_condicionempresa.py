# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CondicionEmpresa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
    ]
