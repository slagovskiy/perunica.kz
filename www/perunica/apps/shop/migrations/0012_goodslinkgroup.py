# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20150507_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsLinkGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('goods', models.ManyToManyField(to='shop.Goods')),
                ('group', models.OneToOneField(to='shop.GoodsGroup')),
            ],
        ),
    ]
