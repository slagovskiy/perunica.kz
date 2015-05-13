# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perunica.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Image name', max_length=256, default='')),
                ('image', models.ImageField(verbose_name='Image', null=True, upload_to=perunica.utils.models.Image.upload_to)),
            ],
        ),
    ]
