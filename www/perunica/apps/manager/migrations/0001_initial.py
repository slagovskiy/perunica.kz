# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('login', models.CharField(unique=True, verbose_name='Login', default='', max_length=255)),
                ('password', models.TextField(verbose_name='Password', default='', max_length=255)),
                ('name', models.CharField(verbose_name='Name', default='', max_length=255)),
                ('email', models.EmailField(null=True, verbose_name='Email', blank=True, default='', max_length=255)),
            ],
        ),
    ]
