# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autores',
            name='autor',
            field=models.CharField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libros',
            name='isbn',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libros',
            name='titulo',
            field=models.CharField(max_length=85),
            preserve_default=True,
        ),
    ]
