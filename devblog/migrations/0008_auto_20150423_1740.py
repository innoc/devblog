# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0007_auto_20150423_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='title',
            field=models.TextField(default=b'enter a value'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopost',
            name='title',
            field=models.TextField(default=b'enter a value'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='description',
            field=models.TextField(default=b'enter a value'),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='description',
            field=models.TextField(default=b'enter a value'),
        ),
    ]
