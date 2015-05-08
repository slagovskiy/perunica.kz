# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.apps.banner.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('link', models.CharField(verbose_name='link', max_length=255)),
                ('image', models.ImageField(null=True, verbose_name='Image', upload_to=perunica.apps.banner.models.Banner.upload_to)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
                'ordering': ['name'],
            },
        ),
    ]
