# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150515_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbody',
            name='option1',
            field=models.ForeignKey(null=True, to='shop.Goods', related_name='o1', blank=True),
        ),
        migrations.AlterField(
            model_name='orderbody',
            name='option2',
            field=models.ForeignKey(null=True, to='shop.Goods', related_name='o2', blank=True),
        ),
        migrations.AlterField(
            model_name='orderbody',
            name='option3',
            field=models.ForeignKey(null=True, to='shop.Goods', related_name='o3', blank=True),
        ),
    ]
