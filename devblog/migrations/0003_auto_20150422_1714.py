# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0002_auto_20150422_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basepost',
            name='author',
        ),
        migrations.DeleteModel(
            name='basePost',
        ),
    ]
