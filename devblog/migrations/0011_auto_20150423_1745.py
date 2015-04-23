# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0010_auto_20150423_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
