# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0011_auto_20150423_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='post_type',
            field=models.CharField(default=b'', max_length=5, choices=[(b'i', b'image'), (b'v', b'video')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopost',
            name='post_type',
            field=models.CharField(default=b'', max_length=5, choices=[(b'i', b'image'), (b'v', b'video')]),
            preserve_default=True,
        ),
    ]
