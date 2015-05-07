# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_goodsgroup_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='choice',
            field=models.ForeignKey(blank=True, to='shop.GoodsGroup', null=True, verbose_name='choice'),
        ),
    ]
