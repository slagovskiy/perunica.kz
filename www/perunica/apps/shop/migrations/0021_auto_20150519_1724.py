# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20150515_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, 'Отменен'), (1, 'Новый'), (2, 'Готовится'), (3, 'Доставляется'), (4, 'Выдан')], verbose_name='Status'),
        ),
    ]
