# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devblog', '0003_auto_20150422_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='author',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagepost',
            name='category',
            field=models.CharField(default=b'bk', max_length=5, choices=[(b'bk', b'Backend development'), (b'fr', b'Frontend development'), (b'gr', b'Graphic design')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagepost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagepost',
            name='description',
            field=models.TextField(default=b'null'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopost',
            name='author',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopost',
            name='category',
            field=models.CharField(default=b'bk', max_length=5, choices=[(b'bk', b'Backend development'), (b'fr', b'Frontend development'), (b'gr', b'Graphic design')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopost',
            name='description',
            field=models.TextField(default=b'null'),
            preserve_default=True,
        ),
    ]
