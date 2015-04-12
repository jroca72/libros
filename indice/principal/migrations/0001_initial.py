# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('puntuacion', models.PositiveIntegerField(default=1)),
                ('isbn', models.CharField(max_length=50)),
                ('autor', models.ForeignKey(default=None, to='principal.autores')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
