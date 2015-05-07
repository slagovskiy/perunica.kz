# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150506_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(verbose_name='Deleted', default=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('goods', models.ManyToManyField(to='shop.Goods')),
            ],
            options={
                'verbose_name': 'Goods group',
                'ordering': ['name'],
                'verbose_name_plural': 'Goods groups',
            },
        ),
    ]
