# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20150507_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsgroup',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=255, default=''),
        ),
    ]
