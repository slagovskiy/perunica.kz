# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('active', models.BooleanField(unique=True, verbose_name='Active', default=True)),
                ('meta_title', models.CharField(verbose_name='Meta title', max_length=255, default='')),
                ('meta_description', models.TextField(verbose_name='Meta description', max_length=1024, default='')),
                ('meta_keywords', models.TextField(verbose_name='Meta keywords', max_length=1024, default='')),
                ('order_min_sum', models.FloatField(verbose_name='Minimal order sum', default=300)),
            ],
        ),
    ]
