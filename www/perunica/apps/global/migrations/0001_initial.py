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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('active', models.BooleanField(unique=True, default=True, verbose_name='Active')),
                ('meta_title', models.CharField(max_length=255, verbose_name='Meta title', default='')),
                ('meta_description', models.TextField(max_length=1024, verbose_name='Meta description', default='')),
                ('meta_keywords', models.TextField(max_length=1024, verbose_name='Meta keywords', default='')),
                ('first_page_text', models.TextField(verbose_name='First page text', default='')),
            ],
        ),
    ]
