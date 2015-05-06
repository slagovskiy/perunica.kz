# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('name', models.TextField(max_length=255, verbose_name='Name')),
                ('sort', models.IntegerField(verbose_name='Sort', default=10)),
            ],
            options={
                'verbose_name': 'Menu',
                'ordering': ['sort', 'name'],
                'verbose_name_plural': 'Main menu',
            },
        ),
    ]
