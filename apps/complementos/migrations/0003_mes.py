# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0002_condicionempresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
    ]
