# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devblog', '0006_auto_20150423_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdditionalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'.')),
                ('description', models.TextField(default=b'null')),
                ('gender', models.CharField(default=b'm', max_length=2, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('user', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='blogimage',
            name='user',
        ),
        migrations.DeleteModel(
            name='blogImage',
        ),
    ]
