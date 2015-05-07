# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_goods_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='option1',
            field=models.ForeignKey(null=True, verbose_name='Option 1', related_name='o1', to='shop.GoodsGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='choice',
            field=models.ForeignKey(null=True, verbose_name='Choice', to='shop.GoodsGroup', blank=True),
        ),
    ]
