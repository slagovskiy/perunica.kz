# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20150515_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbody',
            name='count_o1',
            field=models.FloatField(default=0, verbose_name='Count option 1'),
        ),
        migrations.AddField(
            model_name='orderbody',
            name='count_o2',
            field=models.FloatField(default=0, verbose_name='Count option 2'),
        ),
        migrations.AddField(
            model_name='orderbody',
            name='count_o3',
            field=models.FloatField(default=0, verbose_name='Count option 3'),
        ),
        migrations.AddField(
            model_name='orderbody',
            name='price_o1',
            field=models.FloatField(default=0, verbose_name='Price option 1'),
        ),
        migrations.AddField(
            model_name='orderbody',
            name='price_o2',
            field=models.FloatField(default=0, verbose_name='Price option 2'),
        ),
        migrations.AddField(
            model_name='orderbody',
            name='price_o3',
            field=models.FloatField(default=0, verbose_name='Price option 3'),
        ),
    ]
