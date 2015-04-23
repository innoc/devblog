# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0005_blogimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogimage',
            old_name='image',
            new_name='blogimage',
        ),
    ]
