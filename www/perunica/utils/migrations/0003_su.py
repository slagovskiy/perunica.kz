# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SU',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(unique=True, default=True)),
                ('name', models.CharField(max_length=255, default='')),
                ('freezing', models.BooleanField(default=False)),
            ],
        ),
    ]
