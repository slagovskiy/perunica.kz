# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_order_orderbody_orderhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sended',
            field=models.BooleanField(default=False, verbose_name='Sended'),
        ),
        migrations.AddField(
            model_name='order',
            name='uuid',
            field=models.CharField(max_length=80, default='', verbose_name='UUID'),
        ),
    ]
