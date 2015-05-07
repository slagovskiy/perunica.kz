# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20150507_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='option2',
            field=models.ForeignKey(to='shop.GoodsGroup', verbose_name='Option 2', null=True, blank=True, related_name='o2'),
        ),
        migrations.AddField(
            model_name='goods',
            name='option3',
            field=models.ForeignKey(to='shop.GoodsGroup', verbose_name='Option 3', null=True, blank=True, related_name='o3'),
        ),
    ]
