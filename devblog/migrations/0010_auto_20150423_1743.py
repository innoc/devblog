# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0009_auto_20150423_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='title',
            field=models.CharField(default=b'enter a title', max_length=100),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='title',
            field=models.CharField(default=b'enter a title', max_length=100),
        ),
    ]
